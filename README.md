# Ecitizen Facebook Chatbot

## API

This project integrates the eCitizen Facebook page with ChatGPT to provide automated customer support

[![Build and Deploy](https://github.com/ecitizen-ke/ecitizen-fb-chatbot/actions/workflows/develop.yml/badge.svg?branch=develop)]

## Developer Technologies

The host environment must have the following tools running

- [x] MySQL
- [x] Docker

## Installation

1. Clone the repository
2. Navigate to the root directory of the cloned folder and launch your favorite terminal
3. Activate your local environment
4. Navigate to `backend` folder

   `$ cd backend`

5. Install project dependencies

   `$ pip install -r requirements.txt`

#### Configuring environment variables

Create your `.env` file in the `backend` directory and add the following variables

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

#### Analyze Code Coverage

`$ coverage report`

### Version 1 API Endpoints

#### Parties Endpoints : `/api/v1/`

| Method | Endpoint    | Functionality |
| ------ | ----------- | ------------- |
| `POST` | `/register` | Register User |
