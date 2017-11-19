default: lint test

test:
	bundle exec rspec

lint:
	flake8 *py tests/

install:
	bundle

solve:
	./towers console --discs $(or $(discs),3)
	
phat:
	python webserver.py &
	sleep 2
	./towers phat

fake-phat:
	python dummywebserver.py &
	sleep 2
	./towers phat

kill:
	kill `ps ax | grep webser | tr -s ' ' ' ' | cut -d ' ' -f 1`
