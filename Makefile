All: start-local

build:
	docker build -t vestbirk-nginx nginx

start-local:
	docker-compose up -d nginx

stop:
	docker-compose down

