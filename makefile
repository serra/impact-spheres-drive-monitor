bootstrap:
	# assert we are in a (virtual) env with python 3.6
	pip install -r requirements.txt
setup: bootstrap
	#
update:
	# pass
server:
	export FLASK_DEBUG=1; export FLASK_APP=./webapp/app.py; flask run
heroku-local:
	heroku local web
test:
	nosetests tests
cibuild:
	# pass
console:
	# pass
html-docs:
	cd docs; make html
check-environment:
	robot ./docs/development.rst
clear-cache:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf
notify-marijn:
	# send msg to marijn's dm.
	# This must be on the same line, otherwise notify.py runs in a new env
	export SLACK_CHANNEL_TO_NOTIFY="D5RBMJ8RF"; python notify.py
notify-impact-spheres:
	export SLACK_CHANNEL_TO_NOTIFY="G7B5DUUC8"; python notify.py
auth-slack:
	export FLASK_APP=./slack/oauth.py; flask run
auth-contentful:
	export FLASK_APP=./content/oauth.py; flask run
auth-google:
	python ./google/oauth.py
test-webapp:
	clear
	robot ./docs/functionality.rst
test-api:
	curl -i http://localhost:5000/search?query=thiz_duz_not_exizt
