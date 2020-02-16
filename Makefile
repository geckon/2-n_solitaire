#  ___  _ __     _____       _ _ _        _
# |__ \| '_ \   / ____|     | (_) |      (_)
#    ) |_| |_| | (___   ___ | |_| |_ __ _ _ _ __ ___
#   / /         \___ \ / _ \| | | __/ _` | | '__/ _ \
#  / /_         ____) | (_) | | | || (_| | | | |  __/
# |____|       |_____/ \___/|_|_|\__\__,_|_|_|  \___|
#

init:
	poetry install

bandit:
	poetry run bandit -r solitaire.py twn_solitaire

pycodestyle:
	poetry run pycodestyle --exclude=venv --filename="*.py" .

pylint:
	poetry run pylint --reports=n solitaire.py twn_solitaire

pylint-error:
	poetry run pylint --reports=n --disable=C,R,W solitaire.py twn_solitaire

travis: bandit pycodestyle pylint-error
