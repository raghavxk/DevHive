# DevHive

- DevHive is a social web app for developers. It allows users to showcase their projects, skills and connect with other developers.

- DevHive is built using Python-Django web framework.

## How to setup?

- Clone the repository.
- Create a virtual enviroment using command  `python3 -m venv venv`.
- Activate virtual environment by executing  `source venv/bin/activate`.
- Install dependencies by running command  `pip install -r requirements.txt`.
- Create a  `.env` file and setup all the environment variables.
- Your  `.env` file needs to declare following environment variables :

    ```
    SECRET_KEY=
    DB_NAME=
    DB_USER=
    DB_PASSWORD=
    DB_HOST=
    DEBUG_MODE=
    ```

- The project is setup to use a PostgreSQL instance by default. To use SQLite3 uncomment lines in `devsearch/settings.py` . Necessary comments have been added.

- Run `python manage.py makemigrations` followed by `python manage.py migrate` .
- Run `python manage.py runserver` to start the app. Voila!
