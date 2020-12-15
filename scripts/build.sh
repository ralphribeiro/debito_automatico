#!/bin/bash

# Build e roda contain
docker-compose up -d

# Hack to wait for postgres container to be up before running alembic migrations
sleep 5;

# Create secret_key
myVar=$(openssl rand -hex 32)
export SECRET_KEY=$myVar

# Run migrations
docker-compose run --rm backend alembic upgrade head

# Create initial data
docker-compose run --rm backend python3 app/initial_data.py