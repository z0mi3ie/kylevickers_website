#Native imports
import logging

# 3rd Party imports
from flask import Flask
from flask import render_template
from flask import request

# Local imports
from pr.pr import strip_git_info

# Logging setup
log = logging.getLogger('werkzeug')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/pull", methods=['POST', 'GET'])
def pull():
    # Create the pull request
    if request.method == 'POST':
        raw_branch = request.form['git_branch_url']
        git_stripped = strip_git_info(raw_branch)

        print(git_stripped)

        return render_template('pull/pr.html',
                ticket_number=request.form['ticket_number'],
                ticket_title=request.form['ticket_title'],
                ticket_url=request.form['ticket_url'],
                summary=request.form['summary'],
                review_a=request.form['review_a'],
                review_b=request.form['review_b'],
                setup=request.form['setup'],
                test=request.form['test'],
                verify=request.form['verify'],
                git_user=git_stripped['username'],
                git_repo=git_stripped['repo'],
                git_branch=git_stripped['branch'],
                git_host=git_stripped['host'],
        )

    # Display the PR template
    if request.method == 'GET':
        return render_template('pull/pull.html')


# Start the debug server
if __name__ == "__main__":
    # Set debug mode on
    app.debug = True
    log.debug('new message')

    # Start the app
    app.run()
