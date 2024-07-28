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

`$ coverage run -m pytest`

#### Code Coverage Analysis

`$ coverage report`

### Version 1 API Endpoints

#### Auth Endpoints

| Method | Endpoint                        | Functionality                                                           |
| ------ | ------------------------------- | ----------------------------------------------------------------------- |
| `POST` | `/api/v1/chatbot/auth/register` | `User Registration:` Creates a new system user                          |
| `POST` | `/api/v1/chatbot/auth/login`    | `User Authentication:` Authenticates a user with login credentials      |
| `GET`  | `/api/v1/chatbot`               | `Landing Page:` This is the landing page upon successful authentication |
| `POST` | `/api/v1/chatbot/logout`        | `User Logout:` Revokes user access to the system                        |

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
  "code": 201,
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
  "code": 200,
  "message": "User authentication successful",
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMjAxMDg0NCwianRpIjoiMTQ3PjQ5YTAtNGY1ZS00MzhiLWE2NjgtNTHzNTdiM2JmNGQ2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluQGVjaXRpemVuLmNvbSIsIk5iZiI6MTcyMjAxMDg0NCwiY3NyZiI6IjE5ZTNkMDQ3LTY5ZWUtNGJjZC04ZDU0LTYzNjlmMjEzYTAzMiIsImV4cCI6MTcyMjAxMTc0NH0.DxcdXquE7iimUaGs_NmbIomypQ3nxaqCL5pQTBhbeRb"
}
```

##### Sample user logout success response body

```json
{
  "code": 200,
  "message": "logout successful"
}
```

##### Sample unauthorized access response with revoked access token

```json
{
  "msg": "Token has been revoked"
}
```
