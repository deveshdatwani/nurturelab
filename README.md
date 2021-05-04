### This repository contains a django project work for Nurturelab's assignment

********************************************* 
Copy right claims reserved by Devesh Datwani. 

Author: Devesh Datwani
Date: 04/05/2021

**********************************************

The Django project strucure is as follows- 

    - assignment
      - advisor
        - admin.py
        - apps.py
        - forms.py
        - models.py
        - tests.py
        - views.py
      - assignment
        - asgi.py
        - settings.py
        - urls.py
        - wsgi.py
      - templates
        - static
        - base
        - book_call
        - get_advisors
        - get_bookings 
        - index
        - register_advisor
        - register_user
        - user_login
    - user
      - admin.py
      - apps.py
      - forms.py
      - models.py
      - tests.py
      - views.py
    - env
    - manage.py

### The templates folder

<p>I have built some templates and populated them with model data using the Django template engine just to visualize the data return. If anyone wishes to visualize, just uncomment the HttpResponse statment under every endpoint and comment out the JsonResonse statements.<p>

<p>A sample template has been shown below.<p>
<img src="https://github.com/deveshdatwani/nurturelab/blob/main/assets/sample.png" style="height: 300px; width: 600px;">


### endpoints 

<p>For simplicity's sake, I did not over complicate the API. A lot more functionality can be added to the given app, like hashing the password which is absolutely important by standard. But I have let such things go in order to deploy an MVP of the app on a heroku server. If the passwords are hashing and you still see this message, then I may have fixed it and not udpate the README.<p>

#### 1. /user/register/

Form requirements: name, email, passowrd

Returns json with status: "200_OK" and "user-id" code if required form is filled correctly or "400_BAD_REQUEST" if not. As of 04/06/2021, the response does not contain the JWT authentication.

#### 2. /advisor/register

<p>PS- I have purposely set a default value for the url of the photo in order to maintain simplicity of the webapp in the testing stage. The url is a png of an icon that represents a human being.</p>

Form requirements: name, photo_url

Returns json with status code: "200_OK" along with advisor "id" if required form is filled correctly or "400_BAD_REQUEST" if not.

#### 3. /user/login

Form requirements: email, password

Returns json with status code: "200_OK" and "user-id" if the form is filled correctly and the credentials match. If the credentials don't match then "401_AUTHENTICATION_ERROR" is returned, else "400_BAD_REQUEST" is returned. Again, this too does not contain the JWT token, which I will come back to in a while.

#### 4. user/<user-id>/advisors

Form requirements: nothing 

Returns: json of all advisors with their "name", "id" and "photo_url" along with status code: "200_OK"

#### 5. user/<user-id>/advisor/<advisor-id>/

Form requirements: booking time and date in string format (datetime format)

Returns: json of status: "200_OK" if the form is legit and the "booking-id"

#### 6. user/<user-id>/<advisor>/<booking>/

  Form requirements: none

  Returns: json format whose "body" key contains array of dictionaries each representing a booking with the relevant details.