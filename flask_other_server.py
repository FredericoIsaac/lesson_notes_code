from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the app
app = Flask(__name__)
# Connect Database with the app
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/lesson_3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Given an instance of the SQLAlchemy class from Flask-SQLAlchemy
db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    # Print Class specification
    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'


# Create all the tables
db.create_all()

person = Person(name='Boob')
db.session.add(person)
db.session.commit()


@app.route('/')
def index():
    # Return first row of the query "SELECT * FROM persons"
    person_query = Person.query.first()
    return 'Hello World'


if __name__ == "__main__":
    app.run(debug=True)
