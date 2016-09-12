/// <reference path="typings/tsd.d.ts" />

var exec = require('child_process').exec;
var fs = require('fs');
var async = require('async');
require('shelljs/global');

function setup() {
	rm('-rf', 'out');
	mkdir('-p', 'out/raw');
	mkdir('-p', 'out/proc');
}

function process(chapter) {
	async.waterfall([
		function (next) {
			var ch = chapter.toString();
			ch = ch.length < 2 ? '0' + ch : ch;
			var command = 'pandoc -s Python_Book/Text/M' + ch + '_SMIT8708_03_SE_C' + ch + '.docx -t rst -o out/raw/m' + chapter + '.rst';
			exec(command, function (error, stdout, stderr) {
				next(error);
			});
		},
		function (next) {
			fs.readFile('out/raw/m' + chapter + '.rst', 'utf8', next);
		},
		function (data, next) {
			data = data.replace(/\|image[0-9]+\|/g, '');
			data = data.replace(/.+media\/image[0-9]+\.jpg/g, '');
			data = data.replace(/\n\n+/g, '\n\n');
			next(null, data);
		},
		function (data, next) {
			fs.writeFile('out/proc/m' + chapter + '.rst', data, next);
		}
	], function (error) {
		if (error) {
			console.error(error);
			return;
		}
		console.log('Chapter ' + chapter + ' processed');
	});
}

setup();

[3,4,5,11,13].forEach(function (chapter) {
	process(chapter);
});