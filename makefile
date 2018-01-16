bootstrap:
	# assert we are in a (virtual) env with python 3.6
setup: bootstrap
	# pip install -r requirements.txt
update:
	# pass
server:
	export FLASK_APP=./webapp/app.py; flask run
heroku-local:
	heroku local web
test:
	python monitor.py
cibuild:
	# pass
console:
	# pass
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
test-api:
	curl -i \
	-X POST -F 'response_url=http://localhost:5000/echo' \
	http://localhost:5000/guides
	curl -i \
	-X POST -F 'text=queues' -F 'response_url=http://localhost:5000/echo' \
	http://localhost:5000/guides
	curl -i \
	-X POST -F 'text=review' -F 'response_url=http://localhost:5000/echo' \
	http://localhost:5000/guides
	curl -i \
	-X POST -F 'text=daily' -F 'response_url=http://localhost:5000/echo' \
	http://localhost:5000/guides
	curl -i http://localhost:5000/search?query=wall \
	curl -i http://localhost:5000/search?query=thiz_duz_not_exizt