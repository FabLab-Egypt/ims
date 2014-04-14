# Fab Lab Egypt

## IMS - Internal Management Systems

> WIP

### Installation

Installation instaration on Unix/Linux systems.

1. Using Python 2.x
1. Install Virtualenv `$ pip install virtualenv`
1. Clone this repo.
1. `cd` to repo directory
1. Creat a virtualenv `$ virtualenv ims-env`
1. Activate the virtualenv `$ source ims-env/bin/activate`
1. Install modules for `requirements.txt`
2. open project directory `$ cd fablab_ims`
2. sync django DB `$ python manage.py syncdb`
2. start testing server `python manage.py runserver 8080`
2. You will be promt to creat a superuser, do so.
3. open web browser and open `http://127.0.0.1:8080/admin`
3. login, start testing 

> WIP

### Admin

> WIP

#### Django Suits

> WIP

##### Menu Icons

Since django suits offers a limited option when it comes to menu icons, a simple hack was implemented to add more options.

FontAwesome.io was injected to the `suits.css` file fount at `<pythonX.X>/site-packages/suit/static/suit/css/suit.css`

Note this hack will be lost on update, 