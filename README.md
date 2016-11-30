Deploy:

python manage.py loaddata users/fixtures/roles.json 


Api guide:

1. register user by link /api/users/

POST request with data 
{"password":12345, "role_name":"Manager", "username": "lalala2", "email": "newuser@im.ok"}

2. authentificate user need to send post request with parametres or use a basic authentification:
POST /api/token/
{"username": "lalala2", "password": 12345}

3. Get all users 
