# Rakt_assignment_utkarsh
RAKT_assignment

## Features

- User Registration and Login
- User Authentication with JWT
- Dashboard for finding food trucks 
- RESTful API for frontend interaction
- CSRF protection
- Error handling and validation

### How to run the application.

Step 1:

* Clone the application to your local machine
 ```
clone https://github.com/utkarshagrawal2000/Rakt_assignment_utkarsh
```
* Go into Rakt directory in Rakt_assignment_utkarsh folder

Step 2:

* Create a virtual environment:

``` 
python -m venv venv
source venv/bin/activate   # On Windows use ./venv/Scripts/activate
```
<br>

Step 3:
* Install the dependencies from the requirements file

```
pip install -r requirement.txt
```
<br>
Step 4:

* Create a `.env` file in the root directory where manage.py is :

``` .env
'SECRET_KEY'='django-insecure-f1ricn$xd5jrkm&q++2)1xd3wd^lj$9z7g#*%aie$2ds6o$=2e'
'NAME'='foodtruck_db'
'USER'='root'
'PASSWORD'='root'
```
<br>
Step 5:

run the following commands:

```
python manage.py migrate
python manage.py runserver
```

*Access the application:
<br>
[http://127.0.0.1:8000](http://127.0.0.1:8000)

Importing Postman Collection

- Open Postman.
- Click on Import in the top left corner.
- Select the postman_collection.json file from your file system.
- The collection will be imported, and you can view and test the API endpoints.


*API details
To register the user with parameters(email,username,mobile,password,password2,tc) :
<br>
[http://127.0.0.1:8000/api/user/register/](http://127.0.0.1:8000/api/user/register/)

To login the user with parameters(credential(email/username/mobile) and password) :
<br>
[http://127.0.0.1:8000/api/user/login/](http://127.0.0.1:8000/api/user/login/)

*All the api needs to send access token 
<br>
To insert the  food trucks data use the api:
<br>
[http://127.0.0.1:8000/foodtruck/bulk_upload/](http://127.0.0.1:8000/foodtruck/bulk_upload/)
To retrieves the 5 nearest food trucks to a given latitude and longitude :
<br>
[http://127.0.0.1:8000/foodtruck/nearby_foodtrucks/37.76008693/-122.4188065/](http://127.0.0.1:8000/foodtruck/nearby_foodtrucks/37.76008693/-122.4188065/)

To retrieves thefood trucks for a given Food type :
<br>
[http://127.0.0.1:8000/foodtruck/filter_by_food_type/hot/](http://127.0.0.1:8000/foodtruck/filter_by_food_type/hot/)

To retrieves thefood trucks for a given zipcode:
<br>
[http://127.0.0.1:8000/foodtruck/filter_by_zipcode/28859/](http://127.0.0.1:8000/foodtruck/filter_by_zipcode/28859/)

To retrieves the 5 nearest food trucks to a given latitude and longitude and food type:
<br>
[http://127.0.0.1:8000/foodtruck/detailed_search/37.76008693/-122.4188065/hot/](http://127.0.0.1:8000/foodtruck/detailed_search/37.76008693/-122.4188065/hot/)

<br>


### Rationale

If i have more time i would like to do:
- Add all fiters in single form so user can choose what they want in single go.
- Show details of truck after the filter results.
- Design the frontend properly.
- Optimize the apis more throughly. 
