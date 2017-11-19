default: lint test

test:
	pytest

lint:
	flake8 *py tests/

clean:
	find . -name "*pyc" -delete
	find . -name __pycache__ -exec rm -r {} \;

run:
	python towers.py $(discs)

phat:
	python webserver.py &
	sleep 1
	python phanoi.py
