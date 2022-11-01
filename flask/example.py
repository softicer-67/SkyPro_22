from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to Flask!'


@app.route('/users')
def users():
    return 'Users', 302


@app.get('/users')
def users_get():
    return 'GET /users'


@app.post('/users')
def users_post():
    return 'POST / users'


@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'
