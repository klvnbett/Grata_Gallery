# MY GALLERY

## Author
Kipkemoi Bett

## Description
MyGallery is a personal gallery django application that allows users display their photos for others to see.
This  displays my gallery  and with photo's category,  name, location,  title and time past since it was posted. The project usesadmin dashboard to add data.

As a user of the web application you will be able to:

1. Views various photos
2. Views photo details


## Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.6 manage.py runserver`
* Access the live site using the local host provided
* Create your superuser account `python manage.py createsuperuser` inside virtual environment.
* Add data from admin dashboard

### Prerequisites
* python3.6
* virtual environment
* pip
* postgresql

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY = 'your secret key'
DEBUG=True
DB_NAME='gallery'
DB_USER='<your database name>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='*'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.8 manage.py check
python manage.py makemigrations news
python3.8 manage.py sqlmigrate news 0001
python3.8 manage.py migrate
```

#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)



## Testing the Application
`python manage.py test 
        
## Built With

* [Python3.6](https://docs.python.org/3/)
* Django==3.2.5
* Postgresql 
* Boostrap
* HTML
* CSS


### License

* LICENSED UNDER [MIT]