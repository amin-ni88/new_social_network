# social_network

- cp `local_settings.py.example` to `local_settings.py`
- Install docker
- `docker-compose build --no-cache` to build images
- `docker-compose up -d` to run images
- `docker exec -it social_network-server-1 python manage.py showmigrations` to show migrations
- `docker exec -it social_network-server-1 python manage.py migrate` to migrate models to database
- `docker exec -it social_network-server-1 python manage.py createsuperuser` to create admin user
-
- `docker-compose logs --tail 1 -f nginx` to show nginx logs
- `docker-compose logs --tail 1 -f server` to show uwsgi logs