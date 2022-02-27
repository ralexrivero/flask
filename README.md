# flask

Flask essential

## installation

Flask dependencies:
    ``werkzeug``
    ``jinja``
    ``markupsafe``
    ``itsdangerous``
    ``click``

virtual environment
``mkdir shortener``
``cd url_shortener``
``pip3 install pipenv``
``pipenv install``

activate the virtual environment

``pipenv shell``

``pipenv install flask``

confirm installation
``flask --version``

## prepare the virtual environment

``sudo netstat -tulpn``
``export FLASK_APP=hello``
``flask run --port 8000``

## allows port in ufw

``sudo ufw allows 8000``

## Development environment

export FLASK_ENV=development

## install gunicorn

``pipenv install guinicorn``

run it

``gunicorn "hello:create_app()" -b 0.0.0.0``