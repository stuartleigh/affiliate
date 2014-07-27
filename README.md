# Affiliate site

A django app that can serve multiple domains with different content. Used for the purpose of creating affiliate advertising sites.

## Installation instructions

### Requirements

* Python 2.7
* git
* virtualenv(:wrapper)

git clone https://github.com/stuartleigh/affiliate.git

`sudo apt-get install mysql-server`

`sudo apt-get install libmysqlclient-dev`

`sudo apt-get install python-dev`

(temporarily, until Django 1.7 gets out of RC and we can upgrade.)
`pip install https://www.djangoproject.com/download/1.7c1/tarball/`

`pip install -r requirements.txt`

rename affiliate/environment.py.example to affiliate/environment.py and set correct value for your environment.

Create your database `CREATE DATABASE affiliate CHARACTER SET utf8;`

./manage.py migrate

./manage.py createsuperuser --username=<user> --email=<email>

to access the admin site you'll need at least one site registered in the db.

```python
from affiliate.site.models import Site
Site(name="localhost", domain="localhost").save()
```