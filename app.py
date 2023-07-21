from flask import Flask, request, url_for
from markupsafe import escape

app = Flask(__name__)

#######################################################################################################################
#                                                   ROUTING                                                           #
#######################################################################################################################
@app.route("/")
def index():
    return 'Index Page'

# @app.route("/login")
# def login():
#     return 'login'

@app.route("/hello")
def hello():
    return "Hello, World"

#######################################################################################################################
#                                                   VARIABLES                                                         #
#######################################################################################################################

@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return f'{username}\'s profile'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

#######################################################################################################################
#                                                   Unique URLs                                                       #
#######################################################################################################################

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


#######################################################################################################################
#                                                   HTTPS Methods                                                     #
#######################################################################################################################

def do_the_login():
    return 'Do the login'


def show_the_login_form():
    return 'Show the login form'


# Using the `methods` argument

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

# using shortcut for decorating routes with get(), post()

@app.get('/login')
def login_get():
    return show_the_login_form()


@app.post('/login')
def login_post():
    return do_the_login()


#######################################################################################################################
#                                                   URL Building                                                      #
#######################################################################################################################

with app.test_request_context():
    print(url_for('index'))
    # print(url_for('login'))
    # print(url_for('login', nest='/'))
    print(url_for('profile', username='John Doe'))