DOCKER_IMAGE="twstrike/coy-testing"

default:
	behave

deps:
	pip install behave

test: coyim-bin
	docker run -t \
		--privileged=true \
		-v $(shell pwd):/src \
		-v $(shell pwd)/dogtail-root:/tmp/dogtail-root \
		-e COYIM_PATH=/src/coyim-bin \
		$(DOCKER_IMAGE) behave

docker-build:
	docker build -t $(DOCKER_IMAGE) .

docker-term:
	docker run -it -v $(shell pwd):/src $(DOCKER_IMAGE) /bin/bash

docker-run: coyim-bin
	docker run -it \
		--privileged=true \
		-v $(shell pwd):/src \
		-v $(shell pwd)/dogtail-root:/tmp/dogtail-root \
		-e COYIM_PATH=/src/coyim-bin \
		$(DOCKER_IMAGE) $(RUN)

coyim-bin:
	docker run -t \
		--privileged=true \
		-v $(shell pwd):/src \
		-v $(shell pwd)/dogtail-root:/tmp/dogtail-root \
		-e COYIM_PATH=/src/coyim-bin \
		$(DOCKER_IMAGE) /bin/build-coy

