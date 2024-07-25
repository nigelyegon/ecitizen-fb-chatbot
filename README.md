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

#### Configuring environment variables

1. Create an `.env file` in the `backend` directory
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

#### Analyze Code Coverage

`$ coverage report`

### Version 1 API Endpoints

#### Auth Endpoints

| Method | Endpoint                | Functionality     |
| ------ | ----------------------- | ----------------- |
| `POST` | `/api/v1/auth/register` | User Registration |
