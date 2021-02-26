from flask import Flask, request, jsonify, render_template, redirect, session

from models import db, connect_db, Drug,  Pharmacy, Price
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///drugs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def show_home():
    """Return Homepage"""
    return redirect('/register')


""" @app.route('/register', methods=['GET', 'POST'])
def register_user():
    

    if "username" in session:
        return redirect(f'/{session["username"]}')

    form = UserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        user = User.register(username, password, email, first_name, last_name)

        # Handle Duplicate Username
        user_obj = User.query.filter_by(username=username).first()
        if user_obj:
            form.username.errors = [
                f'username "{username}" already exists. Please choose another.']
            return render_template('/register.html', form=form)

        db.session.add(user)
        db.session.commit()

        session['username'] = user.username
        return redirect(f'/{user.username}')

    else:
        return render_template('/register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_user():
    
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            session['username'] = user.username
            return redirect(f'/{user.username}')
        else:
            form.username.errors = [
                'Invalid username/password. Please try again.']
            return render_template('/login.html', form=form)

    return render_template('/login.html', form=form)


@app.route('/logout')
def logout_user():
    session.pop('username')

    return redirect('/login')


@app.route('/<username>')
def show_user_home(username):
    if "username" not in session or username != session['username']:
        raise Unauthorized()

    user = User.query.get(username)
    form = DeleteForm()

    #drug_obj = Price.query.filter_by(drug_name=drug_name)

    return render_template('/home.html', user=user, form=form) """


@app.route('/drugs/<int:id>', methods=['GET'])
def get_drug(id):
    drug = Drug.query.get_or_404(id)
    return jsonify(drug=drug.serialize())
