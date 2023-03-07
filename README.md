# URL Shortener
This is a URL shortening web application developed in Python using Django framework. It allows users to convert long URLs into short URLs, which are easier to share and remember.

# Functionality
Users can input long URLs and receive short URLs.
Users can input a short URL and be redirected to the corresponding long URL.
The web app uses base62 encoding to convert the database id of the long URL to a shorter and unique short URL.
Technologies Used
1. Python 3
2. Django 3
3. HTML, CSS, Bootstrap
4. SQLite3 database
5. Unit Testing

# Unit Testing
Unit tests have been implemented to test the functionality of the URL Shortener. 
Tests include:

1. Test if a short URL already exists in the database.
2. Test if a new short URL is created and saved to the database.
3. Test the function that generates short URLs using base62 encoding.
4. Test if the redirection to the long URL works properly.

# Deployment
This URL Shortener has been deployed on PythonAnywhere at https://boddy123.pythonanywhere.com/url_shorten/.

How it Works
When a user inputs a long URL, the URL Shortener checks if the long URL already exists in the database. If it exists, the web app returns the corresponding short URL. If it does not exist, the web app generates a new short URL using base62 encoding and saves the long URL and its corresponding short URL in the database. The user is then presented with the short URL.

When a user clicks a short URL, the web app looks up the corresponding long URL in the database and redirects the user to the long URL.

# Coverage Report
Name                                       Stmts   Miss  Cover
--------------------------------------------------------------
manage.py                                     12      2    83%
mysite/__init__.py                             0      0   100%
mysite/settings.py                            21      0   100%
mysite/urls.py                                 3      0   100%
url_shortener/__init__.py                      0      0   100%
url_shortener/admin.py                         3      0   100%
url_shortener/apps.py                          4      0   100%
url_shortener/migrations/0001_initial.py       5      0   100%
url_shortener/migrations/__init__.py           0      0   100%
url_shortener/models.py                        4      0   100%
url_shortener/tests.py                        68      0   100%
url_shortener/urls.py                          3      0   100%
url_shortener/views.py                        32      0   100%
--------------------------------------------------------------
TOTAL                                        155      2    99%
