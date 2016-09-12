Rope = require('jumprope');
fs = require('fs');

var args = process.argv.slice(2);

// how to use (example): 
// node main.js chapter1.rst diction.txt

function replace(r, replacedPattern, replacement) {
	var pattern = new RegExp(replacedPattern, 'g');
	var match;
	while ((match = pattern.exec(r.toString())) !== null) {
		var start = match.index;
		var text = match[0];
		var end = start + text.length;
		r.del(start, text.length);
		r.insert(start, replacement);
	}
}

fs.readFile(args[0], 'utf8', function (err,data) {
	if (err) {
		return console.log(err);
	}
	var text = new Rope(data);	
	
	var rl = require('readline').createInterface({
		input: require('fs').createReadStream(args[1])
	});
	
	var oldTag = /<old>(.*?)<\/old>/;
	var newTag = /<new>(.*?)<\/new>/;
	
	rl.on('line', function (line) {
		var replacedPattern = line.match(oldTag)[1];
		var replacementText = line.match(newTag)[1];
		replace(text, replacedPattern, replacementText);
		
	});
	rl.on('close', function () {
		console.log(text.toString());
	})
});
