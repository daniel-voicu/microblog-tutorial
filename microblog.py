from app import db, cli, create_app
from app.models import User, Post, Notification, Message, Task

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message, 'Notification': Notification, 'Task': Task}


if __name__ == "__main__":
    app.run(debug=True)

###### Another way of running ######
# # Linux
# # (venv) $ export FLASK_APP=microblog.py
#
# # Microsoft Windows
# # (venv) $ set FLASK_APP=microblog.py
#
# # (venv) $ flask run
