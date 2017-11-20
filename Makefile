default: lint test

test:
	bundle exec rspec

lint:
	flake8 *py tests/

install:
	bundle

solve:
	./towers console --discs $(or $(discs),3)

solve-constrained:
		./towers console --discs $(or $(discs),3) --constrained

phat:
  bundle exec foreman start

kill:
	kill `ps ax | grep webser | tr -s ' ' ' ' | cut -d ' ' -f 1`
