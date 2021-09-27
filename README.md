# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

Within the '.env' file replace the token and key with your own, which are available from https://trello.com/app-key. This will be available to you once you've created an account at www.trello.com

You'll also need to update your board and list-id values within the './to_app/utils/classfunct.py' module to match those that are automatically created when you setup your first Trello board. This application uses a single BOARD_ID and three list ids: DONE_LISTID, TODO_LISTID and DOING_LISTID

More information regarding the rest APIs used within this application can be found at: https://developer.atlassian.com/cloud/trello/rest/api-group-actions
 

## Documentation

within /docs an attempt of the creation of a system context, 
container and component diagram, following the C4 model, exists for 
the readers viewing.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Docker Production and Development Images

Please clone the relevant github application as appropriate:

example: git clone https://github.com/lawrencemark/DevOps-Course-Starter

To keep secrets, keys and tokens secure please create a .env file within the directory that you launch the 'docker run' command from to be succesful in making rest calls to Trello:

key=yourtrellokeygoeshere
token=yourtrellotokengoeshere

To build the relevant production and development image please use the following docker commands:

## PRODUCTION BUILD
```bash
docker build . -t todo-app:prod --target=production
```
## DEVELOPMENT BUILD
```bash
docker build . -t todo-app:dev --target=development

```
## TEST BUILD
```bash
docker build . -t todo-app:test --target=test

To execute and load the container with the correct parameters please use those below:
```
## PRODUCTION RUN
```bash
docker run -d -p 5000:5000 --env-file .env todo-app:prod
```
## DEVELOPMENT RUN
```bash
docker run -d --name developmentImage -p 5000:5000 --env-file .env --mount type=bind,source=$(pwd)/,target=/srv/www todo-app:dev

Instigate tests: docker exec -it developmentImage "pytest" "--disable-pytest-warnings" "/srv/www/todo_app/tests"

For docker compose, please use: docker-compose -p DevOps up --detach
```

## TEST RUN
```bash
docker run -d --name TravisCIImage -p 5000:5000 --env-file .env --mount type=bind,source=$(pwd)/,target=/srv/www todo-app:test

Instigate tests: docker exec -it TravisCIImage "pytest" "--disable-pytest-warnings" "/srv/www/todo_app/tests"
