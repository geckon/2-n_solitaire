#  ___  _ __     _____       _ _ _        _
# |__ \| '_ \   / ____|     | (_) |      (_)
#    ) |_| |_| | (___   ___ | |_| |_ __ _ _ _ __ ___
#   / /         \___ \ / _ \| | | __/ _` | | '__/ _ \
#  / /_         ____) | (_) | | | || (_| | | | |  __/
# |____|       |_____/ \___/|_|_|\__\__,_|_|_|  \___|
#

init:
	pip install -r requirements.txt
	pip freeze

bandit:
	bandit -r solitaire.py twn_solitaire

pycodestyle:
	pycodestyle --exclude=venv --filename="*.py" .

pylint:
	pylint --reports=n solitaire.py twn_solitaire

pylint-error:
	pylint --reports=n --disable=C,R,W solitaire.py twn_solitaire

travis: bandit pycodestyle pylint-error
