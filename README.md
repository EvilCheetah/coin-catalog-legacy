## Installation
1. Clone the Repository:  
	`git clone https://github.com/EvilCheetah/CoinCatalog.git`
2. Create Virtual Environment:  
	`python -m venv ENV_NAME`  
3. Activate Virtual Environment:  
	`source ENV_NAME/bin/activate`  
4. Change directory to **server/**:  
	`cd server/`
5. Use **requirements.txt** to install dependencies:  
	`pip install -r requirements.txt`  
6. Change directory to **Django_Server/**:  
	`cd Django_Server/`
7. Make migrations for the coin_catalog app:
	`python manage.py makemigrations coin_catalog`
	`python manage.py migrate coin_catalog`
##  Usage
After completing **Installation process**, you can Run Django server:  
	`python manage.py runserver`
