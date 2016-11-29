Deploy:

python manage.py loaddata users/fixtures/roles.json 


Api guide:

1. register user by link /api/register/

POST request with data 
{"password":12345, "role_name":"Manager", "username": "lalala2"}

2. authentificate user need to send post request with parametres or use a basic authentification:
/api/token/
{"username": "lalala2", "password": 12345}

3.
