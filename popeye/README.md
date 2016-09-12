# Popye
CS 3300 Online Book Project

# Dependencies:
* make
* nodejs
* npm
* docker
* tmux (only if using start_servers.sh)
* python 2.7
* sphinx and sphinx_rtd_theme
  - `pip install --upgrade sphinx_rtd_theme` to get the most up to date version

# Simple Instructions to configure and run servers
1. Run it on some sort of linux box, it'll just be easier
2. Make sure all dependencies are installed
3. Clone the repository (https://github.gatech.edu/apujari6/POPYE) <- **this will need moved when apujari6 graduates**
4. open a terminal and execute the following commands
  - `cd POPYE/web_server`
  - `make rebuild`
  - `start_servers.sh`
5. open a browser and navigate to localhost:8000/sphinx

# Detailed Instructions to configure and run servers
1. Complete steps 1 to 3 above
2. run the listing execution app server by executing the following commands:
  - `cd ./POPYE/web_server/listing_exec_app`
  - `mkdir -p public/png && mkdir public/gif`
  - `docker build -t anaconda-lib .`
  - `npm install`
  - `nodejs index.js` *note this will run the server and block the current terminal*
3. run the textbook app server by executing the following commands:
  - `cd ./POPYE/web_server/textbook`
  - `sphinx-build sphinx-src static/sphinx`
  - `cd static`
  - `python insert-listings.py`
  - `python -m SimpleHTTPServer` or start any other web server you like here

#Direction for other teams
* Text team:
  - rst files should be named `m<chapter>.rst` (eg `m11.rst`), and placed in `web_server/textbook/sphinx-src/docs/`
  - If the rst's reference images, be sure the image paths are valid from this directory
  - Add each new rst to `web_server/textbook/sphinx-src/index.rst` as `docs/m11` for example
* Library team:
  - `lib` and `object` directories, and anything else related to actual code execution should live in `web_server/listing_exec_app/`
  - Code listings (eg `Figure_11_1.py`) should go to `web_server/textbook/static/default_code/`
  - `figures.py` belongs in `web_server/textbook/static/`
