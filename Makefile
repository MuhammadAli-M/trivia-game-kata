.PHONY: test test-cov test-mon test-docker

test:
	python3 -m pytest tests/

test-cov:
	python3 -m pytest --cov=app tests/

test-mon:
	ptw --runner "pytest --picked --testmon"

test-docker:
	./docker_test.sh
