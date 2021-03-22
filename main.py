from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initializing the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/lesson_3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db is an interface for interacting with our database
db = SQLAlchemy(app)


class Person(db.Model):
    # Optional, SQLALChemy choose the name of the class has the table or:
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'


db.create_all()


""" @app.route is a decorator that takes an input function index() 
as the callback that gets invoked when a request to (route /) comes in from a client."""


@app.route('/')
def index():
    person = Person.query.first()
    return 'Hello ' + person.name


if __name__ == '__main__':
    app.run()
