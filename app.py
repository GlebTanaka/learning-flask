from flask import Flask, request, url_for, render_template, redirect
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

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', name=name)


#######################################################################################################################
#                                                   HTML Escaping                                                     #
#######################################################################################################################


@app.route("/<name>")
def escape_rout(name):
    return f"Hello, {escape(name)}!"


#######################################################################################################################
#                                                   VARIABLES                                                         #
#######################################################################################################################

@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return f'{escape(username)}\'s profile'


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

# @app.get('/login')
# def login_get():
#     return show_the_login_form()
#
#
# @app.post('/login')
# def login_post():
#     return do_the_login()

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


#######################################################################################################################
#                                                   Process Requests                                                  #
#######################################################################################################################


@app.route('/query-example')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')
    # if key doesn't exist, returns a 400, bad request error
    framework = request.args['framework']
    # if key doesn't exist, returns None
    website = request.args.get('website')
    return '''
            <h1>The language value is: {}</h1>
            <h1>The framework value is: {}</h1>
            <h1>The website value is: {}</h1>'''.format(language, framework, website)


@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '''
                <h1>The language value is: {}</h1>
                <h1>The framework value is: {}</h1>'''.format(language, framework)

    # otherwise handle the GET request
    return '''
            <form method="POST">
                  <div><label>Language: <input type="text" name="language"></label></div>
                  <div><label>Framework: <input type="text" name="framework"></label></div>
                  <input type="submit" value="Submit">
            </form>'''


@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()
    # If key is not present in JSON object, request will fail
    # language = request_data['language']
    # framework = request_data['framework']
    # # two keys are needed  because of the nested object
    # python_version = request_data['version_info']['python']
    # # an index is needed because of the array
    # examples = request_data['examples'][0]
    # boolean_test = request_data['boolean_test']

    language = None
    framework = None
    python_version = None
    examples = None
    boolean_test = None

    if request_data:
        if 'language' in request_data:
            language = request_data['language']

        if 'framework' in request_data:
            framework = request_data['framework']

        if 'version_info' in request_data:
            if 'python' in request_data['version_info']:
                python_version = request_data['version_info']['python']

        if 'examples' in request_data:
            if (type(request_data['examples']) == list) and (len(request_data['examples']) > 0):
                examples = request_data['examples'][0]

        if 'boolean_test' in request_data:
            boolean_test = request_data['boolean_test']

    return '''
            The language value is: {}
            The framework value is: {}
            The Python version is: {}
            The item a t index 0 in the example list is: {}
            the boolean value is: {}'''.format(language, framework, python_version, examples, boolean_test)


#######################################################################################################################
#                                                   URL Building                                                      #
#######################################################################################################################

with app.test_request_context():
    print(url_for('index'))
    # print(url_for('login'))
    # print(url_for('login', nest='/'))
    print(url_for('profile', username='John Doe'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
