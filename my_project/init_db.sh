#!/bin/bash

# Esperar a que PostgreSQL pase el chequeo de salud
until pg_isready -h "db" -U "postgres"; do
  >&2 echo "Postgres está esperando para iniciar..."
  sleep 1
done

# Ejecutar el script de inicialización
psql -h "db" -U "postgres" -f /docker-entrypoint-initdb.d/init.sql
