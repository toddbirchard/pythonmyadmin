# PythonMyAdmin

![Python](https://img.shields.io/badge/Python-^3.10-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-2.2.5-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Dash](https://img.shields.io/badge/Dash-v^2.14.0-blue.svg?longCache=true&logo=python&longCache=true&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-^3.1.1-red.svg?longCache=true&style=flat-square&logo=scala&logoColor=white&colorA=4c566a&colorB=bf616a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c)
[![GitHub Issues](https://img.shields.io/github/issues/toddbirchard/pythonmyadmin.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b)](https://github.com/toddbirchard/pythonmyadmin/issues)
[![GitHub Stars](https://img.shields.io/github/stars/toddbirchard/pythonmyadmin.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b)](https://github.com/toddbirchard/pythonmyadmin/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/toddbirchard/pythonmyadmin.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b)](https://github.com/toddbirchard/pythonmyadmin/network)

Lightweight Python GUI for exploring and modifying data in database. Spoof of PhpMyAdmin - not affiliated in any way.

## Getting Started

Replace the values in **.env.example** with your values and rename this file to **.env**:

* `FLASK_APP`: Entry point of your application (should be `wsgi.py`).
* `FLASK_DEBUG`: The environment to run your app in (either `development` or `production`).
* `SECRET_KEY`: Randomly generated string of characters used to encrypt your app's data.
* `SQLALCHEMY_DATABASE_URI`: Connection URI of a SQL database

*Never to commit secrets saved in `.env` files to Github.*

### Environment Variables

Get up and running with `make deploy`:

```shell
<<<<<<< HEAD
git clone https://github.com/hackersandslackers/flask-blueprint-tutorial.git
cd flask-blueprint-tutorial
make deploy
=======
$ git clone https://github.com/toddbirchard/pythonmyadmin.git
$ cd pythonmyadmin
$ make deploy
>>>>>>> feature/update-dash-dependencies
```
