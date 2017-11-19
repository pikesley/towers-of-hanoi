default: lint test

test:
	bundle exec rspec

lint:
	flake8 *py tests/

run:
	python towers.py $(discs)

phat:
	python webserver.py &
	sleep 2
	./towers
