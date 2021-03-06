from flask import Flask

from toga_flask import TogaApp

from freedom import app as freedom

app = Flask(__name__, static_folder='../static')

app.add_url_rule('/', view_func=TogaApp.as_view("foo", app_module=freedom))


if __name__ == '__main__':
    app.run(port=8081, debug=True)
