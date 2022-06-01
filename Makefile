up:
	docker-compose up

down:
	docker-compose down

build:
	docker exec web pip install -r requirements.txt
	docker exec web pip install --upgrade pip
	docker exec web python3 manage.py migrate

test:
	docker exec web python3 manage.py test --noinput

logs:
	docker-compose logs -f --tail 100

run:
	docker exec web -it run $(command)

connect:
	docker exec -it web /bin/bash

coverage:
	docker exec web coverage run manage.py test
	docker exec web coverage report
	docker exec web coverage html

