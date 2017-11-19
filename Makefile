default: lint test

test:
	bundle exec rspec

lint:
	flake8 *py tests/

solve:
	./towers console --discs $(discs)

phat:
	python webserver.py &
	sleep 2
	./towers
