#! /usr/bin/env sh
#set -e

python /app/app/celeryworker_pre_start.py

celery -A app.core.celery_app worker -l info -Q main-queue -c 1
