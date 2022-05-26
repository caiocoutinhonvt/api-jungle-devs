up:
	docker-compose up

down:
	docker-compose down

build:
<<<<<<< HEAD
	docker exec web pip install -r requirements.txt
	docker exec web pip install --upgrade pip
	docker exec web python3 manage.py migrate

test:
	docker exec web python3 manage.py test
=======
	docker exec jungle pip install -r requirements.txt
	docker exec jungle pip install --upgrade pip
	docker exec jungle python3 manage.py migrate

test:
	docker exec jungle python3 manage.py test
>>>>>>> 552d4c350106bbe0a27c4ced3ebc402d6e53c48b

logs:
	docker-compose logs -f --tail 100

run:
<<<<<<< HEAD
	docker exec web -it run $(command)

attach:
	docker attach web
=======
	docker exec -it run $(command)

attach:
	docker attach jungle
>>>>>>> 552d4c350106bbe0a27c4ced3ebc402d6e53c48b
