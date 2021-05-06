### This repository contains a Django project for Nurturelab's internship assignment

********************************************* 
Copy right claims reserved by Devesh Datwani. 

Author: Devesh Datwani
Date: 04/05/2021

**********************************************

#### Stuff pending: 

  <ul>
    <li>JWT authentication</li>
  </ul>

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

<p>Though not required, I wrote html for some basic templates and that populate through the Django template engine so as to not have the hassle of using postman. If you wish to render the returned data in Http template, under the view functions(wherever valid), uncomment the HttpResponse statment and comment out the JsonResonse.<p>

<p>A sample template has been shown below.<p>
<img src="https://github.com/deveshdatwani/nurturelab/blob/main/assets/sample.png" style="height: 300px; width: 600px;">


### Endpoints 

<p>I did not over complicate the API,which goes to say that a lot more functionality could be added to the application, e.g hashing the password which is standard. I have however looked over these to get the mvp running as soon as possible. If the passwords are hashing and you still see this, then I must have fixed it and not udpated theREADME.<p>

#### 1. /user/register/

Form requirements: name, email, passowrd
Method: POST

Returns json with status: "200_OK" and "user-id" code if required form is filled correctly or "400_BAD_REQUEST" if not. As of 04/06/2021, the response does not contain the JWT authentication.

#### 2. /advisor/register/

<p>PS- I have purposely set a default value for the url of the photo in order to maintain simplicity of the webapp in the testing stage. The url is a png of an icon that represents a human being.</p>

Form requirements: name, photo_url
Method: POST

Returns json with status code: "200_OK" along with advisor "id" if required form is filled correctly or "400_BAD_REQUEST" if not.

#### 3. /user/login/

Form requirements: email, password
Method: POST

Returns json with status code: "200_OK" and "user-id" if the form is filled correctly and the credentials match. If the credentials don't match then "401_AUTHENTICATION_ERROR" is returned, else "400_BAD_REQUEST" is returned. Again, this too does not contain the JWT token, which I will come back to in a while.

#### 4. user/<user-id>/advisors/

Form requirements: None 
Method: GET

Returns: json of all advisors with their "name", "id" and "photo_url" along with status code: "200_OK"

#### 5. user/<"user-id">/advisor/<"advisor-id">/

Form requirements: booking time and date in string format (datetime format)

Returns: json of status: "200_OK" if the form is legit and the "booking-id"

#### 6. user/<"user-id">/advisor/booking/

  Form requirements: none
  Method = GET

  Returns: json format whose "body" key contains array of dictionaries each representing a booking with the relevant details.
