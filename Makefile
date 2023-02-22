init:
	pip install -r requirements.txt

init-dev:
	pip install -r requirements-dev.txt

test: init-dev
	flake8 ./googlechatbot --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 ./googlechatbot --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
	python -m pytest tests