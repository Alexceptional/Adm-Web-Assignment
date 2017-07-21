# Administrate Technical Exercise

## Exercise Details
*Please write a small web application that models an address book. Your solution should present a simple user-interface and
should persist the data, so that it is available after restarting any processes.*

*Your address book should list organisations and people. It should allow the user to see the names and contact details of
people in organisations, and to manage the people who are in an organisation. It should store a name and contact details for
each organisation.*

*Your address book should allow organisations and people to be created, edited and deleted.*

*The address book is for use by a single person; there is no need to build authentication and authorization in your submission.*

## My Approach

### Framework
I chose to write this exercise in Python (v3.4.3) and Django (v1.8.18). I chose to use these versions as they are what I am most familiar with. For a production-level project I would consider using a newer version of Django, such as v1.11 LTS.

I primarily used PyCharm (v5.0.5) as my IDE for editing and testing.

### Project Structure
This project uses a conventional Django project structure; a top-level directory containing the management module and two directories, 'addressbook' containing the settings file and root URL configuration, and the app directory, 'addresses', containing the project models, forms, views and HTML templates, along with static files.

#### Templates
The templates are structured with a single base template, *base.html*, containing the HTML headers and static imports, and all other templates extending the base template. This prevents unnecessary repetition of code.

#### Models
I chose to create three models; **Address**, **Person** and **Organisation**. The Address model is an abstract base class and does not actually generate a table when migrations are executed; it is only used for inheritance by the two other models. The Person class stores instances of people or contacts in the address book and the Organisation model stores instances of organisations.

I chose to create a many-to-one relation between the Person and Organisation models. This permits multiple people per organisation, but only one organisation per person. At a database level, this creates a foreign key in the person table which links to the primary key of the organisation.
This requirement is dependent on the precise definition of the task; one possible route of improvement of this address book is to allow people to be in multiple organisations, which would necessitate the use of a many-to-many relation.

#### Forms
I chose to use ModelForms for the task, as each form is directly related to its underlying model. Fields passed from the model, and their order, are specified in the forms Meta class. When rendering the forms in the templates I used a forloop counter and control flow to render the form into two columns.

#### Django Admin
The built-in Django admin interface is available, and can be used by navigating to `/admin` and logging in with username `admin` and password `letmein`. I have not implemented any customisation of the admin interface as the primary aim of this task was to build the front-end, with create, edit and update functionality, myself. The built-in Django authentication/authorization system is available through the admin interface; however this is not used by this project other than for the admin interface itself.

### Front End
The front end is written using HTML and CSS, with Bootstrap, JQuery and Datatables installed. 

Bootstrap is a fast, easy to use content framework; I chose to use this due to both my familiarity with it and its ease of use. I felt Datatables provide a great way to represent the address book data, with its search and pagination features, customisation, and integration with Bootstrap.

#### Installation
The static libraries I have use were installed using Bower directly into the static directory in the addresses app.

### Database
For a larger, production-level project I would choose to use either MySQL or PostrgeSQL, however for this exercise I chose to stick with the Django default of SQLite. This will allow me to commit the database file to version control to allow the persistence of data regardless of which environment the code is executed on, as required by the exercise. Using SQLite also prevents the need for the setup and configuration of a SQL service such as MySQL.

**Note** I would not normally submit the database file to VCS: this is purely for the purpose of this exercise.

### Tests
Due to the simplicity of this project I have not gone into any depth with unit testing, although I have added a small example of a simple unit test for the homepage, located in `addresses/tests.py`. Further testing would involve tests for all views, and use of fixtures (automated test data) for testing the contents of the response context.

## Running the Project
The web application can be executed in a development environment by running `python manage.py runserver` and navigating to http://127.0.0.1:8000. Alternatively, an IP address and port number can be specified in the format `python manage.py runserver 127.0.0.1:8000`.

### Apache & mod_wsgi
This project has been tested using Apache 2 and mod_wsgi for a more production-ready setup. In order for this to work, install the latest version of mod_wsgi and make sure `'mod_wsgi.server'` is included in the `INSTALLED_APPS` section in the Django settings file (`addresses/settings.py`). 

To run, first run the command `python manage.py collectstatic` which will fetch all static files into a single directory and allow the Apache server to serve them (the development server does this automatically). Then run the following command:

```
python manage.py runmodwsgi addresses/wsgi.py --port 8000 --server-name 127.0.0.1 --server-root /django/testserver/test_server --user sysdev --group sysdev --reload-on-changes
```

substituting `--user` and `--group` with the user to run the server, `--server-root` with the desired directory of the Apache instance to be created, and any IP or port desired. The web app can then be accessed at the specified address and port.

## Dependencies
This project only requires a single Python module:
* **Django==1.8.18**

If using mod_wsgi then the following is required:
* **mod-wsgi==4.5.17** (latest version)

