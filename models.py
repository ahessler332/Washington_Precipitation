#from .auth.models import User, AnonymousUser





# Define your models here.
# You can also define them inside a package and import them here.
# This is only a convenience so that all your models are available from a single module.


from datetime import datetime

from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy.ext.orderinglist import ordering_list

from app import db


class User(db.Model):
    """
        Represents a user (teacher).
        ...
        Attributes
        ----------
        id: int
            the user's ID in the database.
        username: str
            the user's chosen username.
        email: str
            the email associated with the user's account.
        image_file: str
            represents the file uploaded for their profile picture.
        password: str
            the user's chosen password.
        classrooms: list(Classroom)
            a list of the user's created classrooms (see Classroom below).
        quizzes: list(Quizzes)
            a list of the user's created quizzes (see Quiz below).
        Methods
        -------
        get_reset_token(expires_sec=1800):
            Returns: a token to reset the user's password.
        verify_reset_token(token):
            verifies the token supplied in order to reset the password.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    classrooms = db.relationship('Classroom', backref='owner', cascade="all, delete, delete-orphan")
    quizzes = db.relationship('Quiz', backref='owner', cascade="all, delete, delete-orphan")


    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


 