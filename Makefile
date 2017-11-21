default: lint test

test:
	bundle exec rspec

lint:
	flake8 *py tests/

install:
	sudo pip install -r requirements.txt
	bundle install

solve:
	./towers console --discs $(or $(discs),3)

solve-constrained:
		./towers console --discs $(or $(discs),3) --constrained

phat:
	bundle exec foreman start

foreman: install
	foreman export -a hanoi -u pi systemd /etc/systemd/system
	sudo systemctl daemon-reload
	sudo systemctl restart hanoi.target
