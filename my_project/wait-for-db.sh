#!/bin/sh

# Espera a que la base de datos esté lista
while ! pg_isready -h db -p 5432 > /dev/null 2> /dev/null; do
    echo "Esperando a que la base de datos esté disponible..."
    sleep 2
done

exec "$@"
