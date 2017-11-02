bootstrap:
	# init venv with python 3.6
	# pip install -r requirements.txt
setup: bootstrap
update:
	# pass
server:
	# pass
test:
	# send msg to marijn's dm. 
	# This must be on the same line, otherwise notify.py runs in a new env
	export SLACK_CHANNEL_TO_NOTIFY="D5RBMJ8RF"; python notify.py
cibuild:
	# pass
console:
	# pass
notify-impact-spheres:
	export SLACK_CHANNEL_TO_NOTIFY="G7B5DUUC8"; python notify.py