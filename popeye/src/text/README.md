Instructions
==

Installation
--

Install [Node.js](https://nodejs.org/en/)  
Install [Pandoc](http://pandoc.org/installing.html)

Open a command line and enter
```
npm install
```

Running
--

Open a command line and enter
```
node app.js
```

The program will output files to the folder out

The folder proc will contain the processed rst files and the folder raw
will contain the raw rst files

Developing
--

If you use [VSCode](https://code.visualstudio.com/) for developing,
then installing TypeScript definitions will help with development

To install:  
Open a command line and enter
```
npm install -g tsd
tsd install
```

Now the TypeScript definitions will be installed in the folder typings