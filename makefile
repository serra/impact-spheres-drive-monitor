bootstrap:
	# assert we are in a (virtual) env with python 3.6
setup: bootstrap
	# pip install -r requirements.txt
update:
	# pass
server:
	export FLASK_APP=./app.py; flask run
test:
	python monitor.py
cibuild:
	# pass
console:
	# pass
notify-marijn:
	# send msg to marijn's dm.
	# This must be on the same line, otherwise notify.py runs in a new env
	export SLACK_CHANNEL_TO_NOTIFY="D5RBMJ8RF"; python notify.py
notify-impact-spheres:
	export SLACK_CHANNEL_TO_NOTIFY="G7B5DUUC8"; python notify.py
auth-slack:
	export FLASK_APP=./slack/oauth.py; flask run
auth-google:
	python ./google/oauth.py