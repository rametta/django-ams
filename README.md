# Django AMS

The Art Management System is a Python webapp built on Django.
Created by Jason Rametta, Oscar Bobadilla, Akshar Patel for our BTM495 class at Concordia University.

## Running on localhost

In order to run this application on your local machine. You will need the following installed:
- [Python](https://www.python.org/) 2 or 3
- Python [Virutal Environment](https://docs.python.org/3/library/venv.html)

Once those are installed, create a folder on your local machine and [git clone](https://git-scm.com/docs/git-clone) this repo into there.
Then create a virtual environment and activate it. If you are running Python 2, use easy_install to install [pip](https://pypi.python.org/pypi/pip) into your environment. If you're running Python 3, then pip is automatically installed.
Pip is a package manager for python projects and will be used to install the required dependencies for this application.
Once pip is ready, install the requirements by running `pip install -r requirements.txt` in your command line and virtual environment.
At that point Django, Pillow and a bunch of other dependencies will be downloaded to your local machine and you will be ready to create a local database.

[PostgreSQL](http://www.postgresql.org/) is the recommended dbms for this project but many others will work aswell. Once a database is configured, link it together in the settings.py file then from the command line run `python manage.py makemigrations` then run `python manage.py migrate`. This will set up all the necessary tables in your database for use in the application. You are now ready to start the server.

Run `python manage.py runserver` in your command line and then open your browser to http://127.0.0.0:8000 to view the site locally hosted on your machine. It will have all the same features as the web version.

One last thing is to create a superuser in order to start creating users within the app. Run `python manage.py createsuperuser` and follow the instructions. Use that account to login the site and access the backend at http://127.0.0.0:8000/admin/
