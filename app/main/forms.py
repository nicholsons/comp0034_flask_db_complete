from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError

from app.models import Student


class SignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    student_ref = StringField('Student ID number',
                              validators=[DataRequired(message="Please enter your student ID number")])
    email = StringField('Email address', validators=[DataRequired(), Email(message='Valid email address required')])
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Sign Up')

    def validate_student_ref(self, student_ref):
        student = Student.query.filter_by(student_ref=student_ref.data).first()
        if student is not None:
            raise ValidationError(
                'An account is already registered for that student ID. Please use a different student reference number.')
