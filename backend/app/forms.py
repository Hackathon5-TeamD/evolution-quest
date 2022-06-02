from wsgiref.validate import validator
from wtforms.form import Form
from wtforms.filds import StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from wtforms import ValidationError
from backend.app.model import User

class LoginForm(Form):
    password = PasswordField('パスワード: ', validators=[DataRequired()])
    submit = SubmitField('ログイン')

class RegisterForm(Form):
    username = StringField('名前: ', validators=[DataRequired()])
    password = PasswordField(
        'パスワード: ', validators=[DataRequired(), EqualTo('password_confirm', message='パスワードが一致しません。')])
    password_confirm = PasswordField('パスワード確認: ', validators=[DataRequired()])
    submit = SubmitField('登録')
    
    
    