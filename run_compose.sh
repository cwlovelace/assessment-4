docker compose up -d
sleep 10
docker exec drf-wine-api-v1-api-1 python manage.py migrate
