DOCKER_IMAGE="twstrike/coy-testing"

default:
	behave

deps:
	pip install behave

docker-build:
	docker build -t $(DOCKER_IMAGE) .

docker-term:
	docker run -it -v $(shell pwd):/src $(DOCKER_IMAGE) /bin/bash

docker-run:
	docker run -t -v $(shell pwd):/src $(DOCKER_IMAGE)

