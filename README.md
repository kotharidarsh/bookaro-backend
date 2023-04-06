# bookaro-backend

Setup Steps:
1. Create a Python virtualenv and install dependencies from requirements.txt
pip install -r requirements.txt
2. You will need to setup mysql, rabbitmq and redis locally
3. Open Terminal and navigate to backend/app and edit the .env files accordingly
4. Open Terminal and navigate to backend/app folder
5. Execute the following command: 
celery -A app.core.celery_app worker -l info queues=argon-authentication-service
6. Open a new Terminal and navigate to backend/app folder
7. Execute the following command: 
uvicorn app.main:app --host=0.0.0.0 --port=8001 --reload

The first command starts celery worker and the second command starts the fastapi uvicorn server
In order to spawn different services, edit the APP_MODULE variable in the .env file
current acceptable values:
