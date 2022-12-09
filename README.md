# wakanda


install docker

clone the wakanda repo

go to repo and type these commands


1) docker-compose -f docker-compose.yml -d 

- "docker ps" command to check containers are up and running


2) docker exec -it wakanda_be python3 manage.py makemigrations
3) docker exec -it wakanda_be python3 manage.py migrate




########
To create super user

docker exec -it wakanda_be python3 manage.py createsuperuser


sample end point
localhost:8000/sample

Django admin end point
localhost:8000/admin