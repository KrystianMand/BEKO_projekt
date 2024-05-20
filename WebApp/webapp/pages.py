import json
from flask import Blueprint, render_template, request, session, redirect, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from webapp.models import GatewaysModel, AnimationsModel

ANIMATIONS_JSON_PATH = 'webapp/resources/animations.json'

bp = Blueprint("pages", __name__)

test_animations = {'First': 'First content', 'Second': 'Secondcontent'}

# with open(ANIMATIONS_JSON_PATH, 'r') as f:
#     test_animations = json.load(f)

users = {}

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/animations", methods=['GET', 'POST'])
def animations():
    if request.method == 'GET':
        return render_template("pages/animations.html", animations=test_animations)

    elif request.method == 'POST':
        message = "Animation sent!"
        return render_template("pages/animations.html", animations=test_animations, message=message)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('pages.home'))
        else:
            flash('Invalid username or password')
    
    return render_template('pages/login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users:
            flash('Username already exists')
        else:
            hashed_password = generate_password_hash(password)
            users[username] = {'password': hashed_password}
            flash('Registration successful, please log in')
            return redirect(url_for('pages.login'))
    
    return render_template('pages/register.html')

@bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('pages.login'))


@bp.route("/gateways", methods=['GET', 'POST'])
def gateways():
    if request.method == 'GET':
        gateways = GatewaysModel.query.all()
        print(gateways)
        gateways = [
            {
                "id": gateway.id,
                "ip": gateway.ip,
                "location": gateway.location
            } for gateway in gateways]
        
        return render_template("pages/gateways.html", gateways=gateways)

    elif request.method == 'POST':
        selected_gateways = [key for key in request.form.keys() if key.startswith('gateway_')]
        selected_gateways_ids = [request.form[key] for key in selected_gateways]

        return render_template("pages/gateways.html")
        