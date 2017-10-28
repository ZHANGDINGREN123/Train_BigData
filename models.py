from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from exts import db


class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String(11), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)


class SafeProblem(db.Model):
    __tablename__ = 'SafeProblem'
    I_SECURITYID = db.Column(db.Integer, primary_key=True)
    ID = db.Column(db.Integer)
    S_RESPONSIBILITYDEPT = db.Column(db.VARCHAR(20))
    S_RISKPOINT = db.Column(db.VARCHAR(20))
    S_HANDLEREASULT = db.Column(db.VARCHAR(20))
    D_CHECKDATE = db.Column(db.DATETIME)


class SafeNumber(db.Model):
    __tablename__ = "SafeNumber"
    DEPT_NAME = db.Column(db.VARCHAR(20), primary_key=True)
    TIME = db.Column(db.DATETIME, primary_key=True)
    PROBLEM_TYPE = db.Column(db.VARCHAR(20), primary_key=True)
    NUMBER = db.Column(db.INT)
