Task manager

This project is using python 3.5, django 1.10.1, celery 4.0.0

Here 3 main models: User, Project, Task
 User can has 2 roles: Developer, Manager (user has fk on model Role)

Deploy:

python manage.py migrate
python manage.py loaddata users/fixtures/roles.json
to start server run: python manage.py runserver

run celery to send notifications in different windows:
    celery -A task_manager worker -l info
    celery -A task_manager beat -l info -S django
    
    **to setup timedelta go to notifications/tasks.py file and change interval

Api guide:

1. User API guide:
    1. 1. register user by link /api/users/
        POST request with data 
        {"password":12345, "role_name":"Manager", "username": "lalala2", "email": "newuser@im.ok"}
    
    1. 2. get user by link /api/users/{parametres}
    parametres like "?username__startswith=lalal&email=newuser@im.ok"
    
    1. 3. delete, get or update user by link /api/users/<username>/

2. Project API guide:
    2. 1. add project by link /api/projects/
        POST request with data 
        {"name":"Project1", "description": "It's new project", "users": "[1,2,3]"}
    
    2. 2. get projects by link /api/projects/{parametres}
    parametres like "?name__startswith=lalal&description__startswith=It's%20new"
    
    2. 3. delete, update or get project by link /api/projects/<id>/

3. Task API guide:
    2. 1. add task by link /api/tasks/
        POST request with data 
        {"name":"Task1", "description": "It's new task", "project": 1,
        "assigned":1}
    
    2. 2. get tasks by link /api/tasks/{parametres}
    parametres like "?name__startswith=Task1&description__startswith=It's%20new"
    
    2. 3. delete, update or get task by link /api/tasks/<id>/

