default: lint test

test:
	pytest

lint:
	flake8 *py tests/

clean:
	find . -name "*pyc" -delete
