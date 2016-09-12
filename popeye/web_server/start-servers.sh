#!/bin/bash

trap ctrl_c INT

function ctrl_c() {
    echo
    echo "killing http server..."
    tmux kill-session -t textbook-server
    echo "killed"
    docker rm $(docker ps -a -q)
}

echo "Starting http server for static textbook pages..."
cd textbook/static;
tmux new -s textbook-server -d 'python -m SimpleHTTPServer';
echo "done"

echo "Starting node server for listing execution..."
echo "press ctrl-c to kill both"
cd ../../listing_exec_app;
node index.js;
