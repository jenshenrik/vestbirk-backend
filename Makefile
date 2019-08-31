All: start-local

build:
	docker build -t vestbirk-api vestbirk/
	docker tag vestbirk-api cloud.canister.io:5000/jenshenrik/vestbirk-api
	docker build -t vestbirk-nginx nginx/
	docker tag vestbirk-nginx cloud.canister.io:5000/jenshenrik/vestbirk-nginx

start-local:
	docker-compose up -d nginx

stop:
	docker-compose down

