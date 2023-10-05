# quiz-app
A Django based application with user authentication that enables users to answer certain puzzles and obtain scores accordingly.

## Steps to running the app locally
On Windows, run the following commands in the command prompt or `cmd` terminal.

- Clone this repository using `git clone https://github.com/Hi-TechMissile/quiz-app.git`
- `cd quiz-app`
- Create a Python virtual environment: `python -m venv myenv`
- Activate the environment: `myenv\Scripts\activate`
- `cd server`
- Install Django using pip (`pip` required): `pip install Django`
- Start the development server: `python manage.py runserver`

### To access the site locally as an administrator
- `cd server`
- Create a superuser: `python manage.py createsuperuser`
- Start the development server: `python manage.py runserver`
- Go to http://localhost:3000/admin to log in with your superuser credentials and make changes to the site's data.
