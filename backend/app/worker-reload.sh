#! /usr/bin/env bash
set -e

python /app/app/celeryworker_pre_start.py

watchmedo auto-restart --recursive -d /app/ -p '*.py' -- celery -A app.core.celery_app worker -l info -Q main-queue -c 1