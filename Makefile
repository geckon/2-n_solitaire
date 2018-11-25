init:
	pip install -r requirements.txt

pycodestyle:
	pycodestyle --exclude=venv --filename="*.py" .

pylint:
	pylint --reports=n solitaire.py twnsol

pylint-error:
	pylint --reports=n --disable=C,R,W solitaire.py twnsol

