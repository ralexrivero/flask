from flask import Flask, render_template, Blueprint

bp = Blueprint('urlshort', __name__)

@bp.route("/")
def hello():
    return render_template('home.html', name='Ronald')

@bp.route('/about')
def about():
    return "<p>This is a URL shortener</p>"

if __name__ == "__main__":
    bp.run(host='0.0.0.0')
