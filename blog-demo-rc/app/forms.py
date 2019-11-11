from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo


class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(2, 20, message='二到二十字符')])
    password = PasswordField(validators=[DataRequired(), Length(2, 20, message='二到二十字符')])
    code = StringField(validators=[DataRequired(), Length(min=4, max=4)])
    remember = BooleanField()
    submit = SubmitField()

    def code(self, field):
        print(session.get('code'))
        if field.data != session.get('code'):
            raise ValidationError(message='验证码错误')


class RegisterForm(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(2, 20, message='二到二十字符')])
    password = PasswordField(validators=[DataRequired(), Length(2, 20, message='二到二十字符')])
    password2 = PasswordField(validators=[DataRequired(), Length(2, 20, message='二到二十字符'), EqualTo('password')])
    code = StringField(validators=[DataRequired(), Length(min=4, max=4)])
    submit = SubmitField()

    def code(self, field):
        print(session.get('code'))
        if field.data != session.get('code'):
            raise ValidationError(message='验证码错误')


class UpdateForm(FlaskForm):
    title = StringField(validators=[DataRequired(), Length(4, 64, message='4到64字符')])
    head = StringField(validators=[DataRequired(), Length(4, 64, message='4到64字符')])
    body = StringField(validators=[DataRequired()])
    submit = SubmitField()


class AddForm(FlaskForm):
    title = StringField(validators=[DataRequired(), Length(4, 64, message='4到64字符')])

    head = StringField(validators=[DataRequired(), Length(4, 64, message='4到64字符')])
    body = StringField(validators=[DataRequired()])
    submit = SubmitField()
