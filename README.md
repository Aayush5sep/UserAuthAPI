# User Authentication API


A Django & Django-REST framework based API backend system to authenticate user (register, login, logout & profile etc.). Implements Django Rest Simple JWT (JSON Web Token) for secured token implementation.

## Installation
This app requires python to run on your server/localhost.

#### 1. Clone the project on your local computer.

```sh
git clone https://github.com/Aayush5sep/UserAuthAPI.git
```

### 2. Install the dependencies and devDependencies.

```sh
pipenv install -r requirements.txt
pipenv shell
```
>Any other virtual environments may also work. 
>The requirements.txt file contains all the packages that need to be installed.

### 3. Generate  a Secret Key.

- Create a new secret key for django with a secret key generator, like [Djecrety](https://djecrety.ir/).
- Set this secret key value for `DJANGO_KEY` in .env file.
- > Note: `ROTATE_REFRESH_ACCESS_TOKENS` can be changed as well in .env.

### 4. Migrate the project.
Run the following commands in terminal.
```sh
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the project.
Run the following command in terminal to start the server.
```sh
python manage.py runserver
```

## Usage
> Any `API Platform` or `Frontend Tech` can be used to test out the backend features.

We have used `POSTMAN` to check the working of our backend.
You can access the [API collection here](https://www.postman.com/aerospace-saganist-90809/workspace/django-jwt-user-auth-api-test/collection/21641473-38b8913f-3697-4263-9026-1e29d5374cbc?action=share&creator=21641473) to run on your localhost.

![Postman](https://drive.google.com/uc?id=1yBzYAcuSVCChvVbAe5xP2wok1N9WhISG)

The `request` & `response` format has been shown respectively in RESTful Endpoints.

## RESTful Endpoints

| Request | URL | Usage |
| ------ | ------ | ------ |
| POST | api/user/register/ | Register New User |
| POST | api/user/login/ | Login User |
| POST | api/user/logout/ | Logout User |
| POST | api/user/refresh/ | Refresh Access Token |
| GET | api/user/profile/ | Get User Profile Details |
| PUT | api/user/profile/ | Update User Profile Details |
| POST | api/user/profile/ | Add User Profile Details |
| GET | api/manage/flush/tokens/ | Clear Blacklisted Tokens |


### - Register New User 
`POST [api/user/register]`
```sh
JSON Body
{
    "username": "",
    "email": "",
    "password": "",
    "cf_password": ""
}
```
```sh
JSON Response
{
    "access": "access_token",
    "refresh": "refresh_token"
}
```
![Register User](https://drive.google.com/uc?id=17ESMJWF9bhoMFGXsZQcqBmfV9oiauxmJ)


### - Login User 
`POST [api/user/login/]`
```sh
JSON Body
{
    "username": "",
    "password": ""
}
```
```sh
JSON Response
{
    "access": "access_token",
    "refresh": "refresh_token"
}
```
![Login User](https://drive.google.com/uc?id=177HqR_1Z-M_YV7NR_3pXw0RpyeX5M1Ma)


### - Logout User 
`POST [api/user/logout/]`
```sh
JSON Body
{
    "access": "access_token"
}

Authorization
Bearer + access_token
```
```sh
JSON Response
{
    "msg": "Logged Out"
}
```
![Logout User](https://drive.google.com/uc?id=1yZhNfd7XxSxROZ_a6x5UjEyJAcv66X00)


### - Refresh Access Token 
`POST [api/user/refresh/]`
```sh
JSON Body
{
    "refresh": "refresh_token"
}
```
```sh
JSON Response
{
    "access": "access_token"
}
```
![Refresh Token](https://drive.google.com/uc?id=1DZHsDRvhq9NrFG7LIbZG8F9YRJcMlmpM)


### - Get User Profile Details 
`GET [api/user/profile/]`
```sh
Authorization
Bearer + access_token
```
```sh
JSON Response
{
    "first_name": "",
    "last_name": "",
    "about": "",
    "phone": "",
    "country": ""
}
```
![Get Profile](https://drive.google.com/uc?id=17lKkKP-5ksoksX1cLgXiVYpML-jVGd0G)


### - Update User Profile Details 
`PUT [api/user/profile/]`
```sh
JSON Body
{
    "first_name": "",
    "last_name": "",
    "about": "",
    "phone": "",
    "country": ""
}

Authorization
Bearer + access_token
```
```sh
JSON Response
{
    "first_name": "",
    "last_name": "",
    "about": "",
    "phone": "",
    "country": ""
}
```
![Update/Create Profile](https://drive.google.com/uc?id=1PNTHrUhlCTkULJYck6huU2JfA4Dpi0hg)


### - Add User Profile Details 
`POST [api/user/profile/]`
```sh
JSON Body
{
    "first_name": "",
    "last_name": "",
    "about": "",
    "phone": "",
    "country": ""
}

Authorization
Bearer + access_token
```
```sh
JSON Response
{
    "first_name": "",
    "last_name": "",
    "about": "",
    "phone": "",
    "country": ""
}
```

### - Clear Blacklisted Tokens 
`GET [api/manage/flush/tokens/]`
```sh
{
    "msg": "Expired & Blacklisted Tokens have been Flushed"
}
```
![Flush Expired/Blacklisted Tokens](https://drive.google.com/uc?id=1mDb2_MkstzgBNXTerQGow6P4eSZwZ14s)


> Check out more projects by `Aayush Goyal` at [Aayush5sep][aayush]




[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen)

   [git-repo]: <https://github.com/Aayush5sep/UserAuthAPI>
   [aayush]: <https://github.com/Aayush5sep>
