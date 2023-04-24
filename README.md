# Incling Pre Task
This project is a Django 3.1 based API that includes two models: Task and Tile. The models are configured to meet the following requirements:

A Task object has a title, an order field, a description, and a type (such as survey, discussion, diary).<br>
A Tile object has a launch date and a status (live, pending, or archived).<br>
A Tile can contain one or many Tasks, but a Task can only belong to a single Tile.<br>

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
This project requires the following:

* Django 3.1
* Django Rest Framework 3.11.0

### Installing
1. Clone the repository to your local machine.
```
git clone https://github.com/ucefe/django-pre-task.git
```

2. Install the required dependencies.
```
pip install -r requirements.txt
```

### Running the Application

1. Run the migrations.
```
python manage.py migrate
```

2. Create a superuser.
```
python manage.py createsuperuser
```

3. Start the development server.
```
python manage.py runserver
```

Access the API in your browser at http://localhost:8000/.

## API Endpoints

The API exposes the following endpoints:

/tiles/: GET and POST for Tile objects.<br>
/tiles/{id}/: GET, PUT, PATCH, and DELETE for a single Tile object.<br>
/tasks/: GET and POST for Task objects.<br>
/tasks/{id}/: GET, PUT, PATCH, and DELETE for a single Task object.
