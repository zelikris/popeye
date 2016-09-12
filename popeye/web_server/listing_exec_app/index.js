var express = require('express');
var bodyParser = require('body-parser')
var uuid = require('uuid');

var app = express();
app.use(bodyParser.json());
app.use(function (req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', '*');

    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');

    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With, content-type');

    res.setHeader('Access-Control-Allow-Credentials', true);

    next();
});

app.post('/', function (req, res) {

    var proc_uuid = uuid.v1();
    console.log(proc_uuid);

    var code = getImports() + req.body["code"] + ";\n" + getImgSave(proc_uuid);

    console.log(code);

    var json;

    var process = new run_cmd(
        'docker', ['run', '--name', proc_uuid, 'anaconda-lib', 'python', '-c', code],
        function (text) {
            console.log('program response: ' + text);

            var splitted = text.split("<OUTPUTEND>");
            console.log('python output: ' +  splitted[0]);
            console.log('python json: ' + splitted[1]);

            try {
                json = JSON.parse(splitted[1]);
            } catch (err) {
                res.status(500);
                return;
            }
            var filepath = json['filepath'];
            json['stdout'] = splitted[0];
            var sent = false;
            if (json['isfigure'] == "True")
            {
                var save_path;
                if  (json['isanim'] == "True") {
                    save_path = 'public/gif';
                } else {
                    save_path = 'public/png';
                }
                var cp = new run_cmd(
                    'docker', ['cp', proc_uuid + ':' + filepath, save_path],
                    function (text) {
                        if (!sent) {
                            sent = true;
                            res.statusCode = 200;
                            console.log("sending img response");
                            res.json(JSON.stringify(json));
                        }
                    },
                    function (text) {
                        if (!sent) {
                            res.status(500);
                        }
                    }
                );
            }
            else
            {
                if (!sent) {
                    sent = true;
                    res.statusCode = 200;
                    console.log("sending no img response");
                    res.json(JSON.stringify(json));
                }
            }

            // remove the docker container
            var rm = new run_cmd(
                'docker', ['rm', proc_uuid],
                function (text) {
                   console.log('rm response: ' + text);
                },
                function (text) {
                    console.log('error removing docker container');
                }
            );
        },
        function (text) {
            res.status(500);
            return;
        }
    );
});

app.use(express.static(__dirname + '/public'));

var server = app.listen(3300, function() {
    var host = server.address().address;
    var port = server.address().port;

    console.log('Example app listening at http://%s:%s', host, port);
});

function run_cmd(cmd, args, out_callback, err_callback) {
    var spawn = require('child_process').spawn;
    var child = spawn(cmd, args);
    var resp = "";
    var err = "";
    child.stdout.on('data', function (buffer) { resp += buffer.toString(); });
    child.stdout.on('end', function() { out_callback(resp); });
    child.stderr.on('data', function (buffer) { err += buffer.toString(); });
    child.stderr.on('end', function() { if (err !== "") err_callback(err); });
}

function getImports() {
    return 'import os.path;\nimport matplotlib;\nmatplotlib.use("Agg");\n';
}

function getImgSave(filename) {
    return 'import json;\n'
        + 'from lib.anim import *;\n'
        + 'from lib.plot import *;\n'
        + 'save_path = "";\n'
        + 'if isanimated():\n'
        + '    save_path = \"/gif/\" + \"' + filename + '\";\n'
        + '    #save_anim(anim, save_path);\n'
        + '    save_path = save_path + \".gif\";\n'
        + 'elif isplotted():\n'
        + '    matplotlib.pyplot.tight_layout(pad=0.4, w_pad=0.5, h_pad=2.0);\n'
        + '    save_path = \"/png/\" + \"' + filename + '.png\";\n'
        + '    matplotlib.pyplot.savefig(save_path);\n'
        + 'respDict = {};\n'
        + 'respDict["isfigure"] = str(isplotted() or isanimated());\n'
        + 'respDict["isanim"] = str(isanimated());\n'
        + 'respDict["filepath"] = save_path;\n'
        + 'print "<OUTPUTEND>" + json.dumps(respDict);\n'
}

