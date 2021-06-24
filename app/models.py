from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255),nullable=False)
    lastname = db.Column(db.String(255),nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    secure_password = db.Column(db.String(255), nullable=False)
    profile_pic_path = db.Column(db.String())
    roles_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.secure_password, password)

    def save_u(self):
        db.session.add(self)
        db.session.commit()

    def _repr_(self):
        return f'User {self.username}'


class Admin (UserMixin, db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    secure_password = db.Column(db.String(255), nullable=False)
    profile_pic_path = db.Column(db.String())
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.secure_password, password)

    def save_a(self):
        db.session.add(self)
        db.session.commit()

    def _repr_(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='roles', lazy="dynamic")
    admin = db.relationship('Admin', backref='roles', lazy="dynamic")

    def _repr_(self):
        return f'User {self.name}'