from flask import Flask
from data import db_session
from data.jobs_api import blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.debug = True


def main():
    db_session.global_init('db/jobs.db')
    app.register_blueprint(blueprint)
    app.run('127.0.0.1', 8080)


if __name__ == '__main__':
    main()
