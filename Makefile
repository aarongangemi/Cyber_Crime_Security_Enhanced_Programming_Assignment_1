# Created by Kay Men Yap 19257442
# Last updated: 28/09/2020
# Purpose: To simplify the process of building the docker iamge and running the docker image
APP=isec3004.kaas.assignment

all: build

build:
	docker build --rm --tag=$(APP) .
	docker image prune -f

run:
	docker run -p 0.0.0.0:8000:8000/tcp -it --rm $(APP)

clean:
	docker image rm $(APP)
	docker system prune
