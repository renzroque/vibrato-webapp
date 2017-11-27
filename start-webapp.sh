#!/bin/bash

echo 'Starting containers...'
docker-compose up -d && sleep 10

echo 'Preparing DB...'
docker exec vibrato-webapp python3 manage.py migrate && sleep 10

echo 'Start data generator...'
docker exec vibrato-webapp python3 data_generator.py