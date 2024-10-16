SERVICE = bot

DOCKER_COMPOSE_FILE = docker-compose.yml

.PHONY: build up down logs restart

build:
	@echo "Building $(SERVICE)..."
	docker compose -f $(DOCKER_COMPOSE_FILE) build $(SERVICE)

up:
	@echo "Starting $(SERVICE)..."
	docker compose -f $(DOCKER_COMPOSE_FILE) up -d $(SERVICE)

down:
	@echo "Stopping $(SERVICE)..."
	docker compose -f $(DOCKER_COMPOSE_FILE) down

logs:
	@echo "Displaying logs for $(SERVICE)..."
	docker compose -f $(DOCKER_COMPOSE_FILE) logs -f $(SERVICE)

restart:
	@echo "Restarting $(SERVICE)..."
	docker compose -f $(DOCKER_COMPOSE_FILE) restart $(SERVICE)
