# Ecitizen Facebook Chatbot

## API

This project integrates the eCitizen Facebook page with ChatGPT to provide automated customer support

![Build](https://github.com/ecitizen-ke/ecitizen-fb-chatbot/actions/workflows/develop.yml/badge.svg?branch=)

## Prerequisite Technologies

The following tools should be preinstalled in the target host

- [x] MySQL version 8.0.36
- [x] Docker version 27.1.1
- [x] Python version 3.12.3
- [x] Pip version 24.1.2

## Installation

1. Clone the repository
2. Launch terminal and navigate to the root directory of the cloned folder
3. Create and activate a virtual environment
4. Navigate to `backend` folder

   `$ cd backend`

5. Install project dependencies

   `$ pip install -r requirements.txt`

#### Database Setup

Create the database `your-development-db` in the host machine

#### Configuring environment variables

1. Create an `.env` file in the `backend` directory
2. Add the following variables

```
CONFIG_MODE=development
TEST_DATABASE_URL=mysql+pymysql://user:password@localhost:3306/your-test-db
DEVELOPMENT_DATABASE_URL=mysql+pymysql://user:password@localhost:3306/your-development-db
SQLALCHEMY_TRACK_MODIFICATIONS=False
```

#### Running the application

`$ flask --app run --debug run`

#### Testing

##### Configuring test environment variables

1. Create an `pytest.ini` file in the `backend` directory
2. Add the following variables

```
[pytest]
addopts = -p no:warnings
env=
    CONFIG_MODE=testing
    TEST_DATABASE_URL=mysql+pymysql://user:password@localhost:3306/your-test-db
    DEVELOPMENT_DATABASE_URL=''
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY=my-sweet-secret-do-not-tell
    JWT_SECRET_KEY=my-sweet-jwt-secret-do-not-tell
    JWT_BLACKLIST_ENABLED=True
    JWT_BLACKLIST_TOKEN_CHECKS="['access', 'refresh']"
```

`$ coverage run -m pytest -v`

#### Code Coverage Analysis

`$ coverage report`

### Version 1 API Endpoints

#### Auth Endpoints

| Method | Endpoint                        | Functionality                               |
| ------ | ------------------------------- | ------------------------------------------- |
| `POST` | `/api/v1/chatbot/auth/register` | `User Registration:` Creates a new user     |
| `POST` | `/api/v1/chatbot/auth/login`    | `User Authentication:` Authenticates a user |
| `GET`  | `/api/v1/chatbot`               | `Index Page:` The landing page route        |
| `POST` | `/api/v1/chatbot/auth/logout`   | `User Logout:` Revokes user access          |
| `POST` | `/api/v1/chatbot/auth/refresh`  | `Refresh:` Regenerates user access tokens   |

#### Server Requests and Responses

##### Sample user registration request body

```json
{
  "email": "test@ecitizen.co.ke",
  "password": "testpassword"
}
```

##### Sample user registration success response body

```json
{
  "status_code": 201,
  "message": "User registration successful"
}
```

##### Sample user authentication request body

```json
{
  "email": "test@ecitizen.co.ke",
  "password": "testpassword"
}
```

##### Sample user authentication success response body

```json
{
  "status_code": 200,
  "message": "User authentication successful",
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMjAxMDg0NCwianRpIjoiMTQ3PjQ5YTAtNGY1ZS00MzhiLWE2NjgtNTHzNTdiM2JmNGQ2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluQGVjaXRpemVuLmNvbSIsIk5iZiI6MTcyMjAxMDg0NCwiY3NyZiI6IjE5ZTNkMDQ3LTY5ZWUtNGJjZC04ZDU0LTYzNjlmMjEzYTAzMiIsImV4cCI6MTcyMjAxMTc0NH0.DxcdXquE7iimUaGs_NmbIomypQ3nxaqCL5pQTBhbeRb",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCIoZmFsc2UsImlhdCI6MTcytjIxNjYwMywianRpJjoiYWRlYzkyNzMtZjUzZi00OWMxLWFmMmItMDkwZDcyOGU0ODFlIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiJhZG1pbkBlY2l0aXplbi5jb20iLCJuYmYiOjE3MjIyMTY2MDMsImNzcmYiOiI3MDcyMjMyYS03MjA4LTRiOWQtYjllYi1jODZiYTEzNDU4YWEiLCJleNAiOjE3MjQ4MDg2MDN9.Q79STusDl1E8bnrGWEcAHzsdrFHLVRdJw3rTVTT1hpx"
}
```

##### Sample user logout success response body

```json
{
  "status_code": 200,
  "message": "logout successful"
}
```

##### Sample unauthorized access response with revoked access token

```json
{
  "msg": "Token has been revoked"
}
```

##### Sample unauthorized access response with expired access token

```json
{
  "msg": "Token has expired"
}
```

##### Sample access token regeneration using refresh tokens

```json
{
  "access_token": "eyJhbGciOiJIUrI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwMjIxOTQxNCwianRpIjoiM2Q5MDY3N2QtMmM2Yi00ZDY1LWFkODctMzM3MjBkODJkNDYyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImBkbWluQGVjaXRpemVuLmNvbSIsIm5iZiI6MTcyMjIx8TQxNCwiY3NyZiI6IjZiMPk1NWE0LWM2ZjYtNDFjNi04ZWQwLTA2MGQ3ZDliMjQxYSIsImV4cCI6MTcyMjIyMDMxNH0.w49lTF6RmkZSlybJKWBcNPhlvtEdkN3atPODu05F5AX",
  "status_code": 200
}
```
