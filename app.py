from flask import Flask, request, render_template
from flask.wrappers import Response
import git


app = Flask(__name__)



@app.route('/update_server', methods=['POST'])
def webhook():
    print('here I am')
    if request.method == 'POST':
        repo = git.Repo('/home/SNG77/techtechtech')
        print(repo)
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400


@app.route('/')
def index():
    return render_template("index.html")