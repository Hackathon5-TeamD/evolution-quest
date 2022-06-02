from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user
from backend.app.forms import LoginForm, RegisterForm
from backend.app.model import User

bp = Blueprint('app', __name__, url_prefix='')

@bp.route('/')
def home():
    return render_template('home.html')

#ログインしてないと実行されない(login_userが実行されていない)
#ログインしていない場合はlogin関数に飛ばされる
@bp.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@bp.route('/logout')
@login_required
def logout_user():
    logout_user()
    return redirect(url_for('app.home'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.methods == 'POST' and form.validate():
        user = User.select_by_username(form.username.data)
        if user and user.validate_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if not next:
                netx = url_for('app.welcome')
            return redirect(next)
    return render_template('login.html', form = form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.methods == 'POST' and form.validate():
        user = User(
            username = form.username.data,
            password = form.password.data
        )
        user.add_user()
        return redirect(url_for('app.login'))
    return render_template('register.html', form =form)

@bp.route('/user')
@login_required
def user():
    return render_template('user.html')