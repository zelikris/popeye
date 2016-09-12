all: rebuild

clean:
	find . -type f -name '*.pyc' -delete
	rm -rf textbook/static/sphinx;
	rm -rf listing_exec_app/public
	cd listing_exec_app; npm uninstall `ls -1 node_modules | tr '/\n' ' '`;
	rm -rf listing_exec_app/node_modules

rebuild: clean
	cd textbook; sphinx-build sphinx-src static/sphinx
	cd textbook/static; python insert-listings.py
	cd listing_exec_app; npm install; ./deploy_docker.sh; mkdir -p public/png; mkdir -p public/gif;
