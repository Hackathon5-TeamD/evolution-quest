
from wtforms.form import Form
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from wtforms import ValidationError
from flaskr.models import User

#ログイン画面で利用
class LoginForm(Form):
    username = StringField('名前: ', validators=[DataRequired()])
    password = PasswordField('パスワード: ', validators=[DataRequired()])
    submit = SubmitField('ログイン')
    
#登録画面で利用
class RegisterForm (Form):
    # email = StringField('メール: ', validators=[DataRequired(), Email()])
    username = StringField('名前: ', validators=[DataRequired()])
    password = PasswordField(
        'パスワード: ', validators=[DataRequired(), EqualTo('password_confirm', message='パスワードが一致しません')]
    )
    password_confirm = PasswordField('パスワード確認: ', validators=[DataRequired()])
    submit = SubmitField('登録')
    
    def validate_username(self, field):
        if User.select_by_username(field.data):
            raise ValidationError('その名前は既に登録されています')
        
    