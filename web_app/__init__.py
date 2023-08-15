
from flask import Flask
from web_app.routes.home_routes import home_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.static_url_path = '/static'
    app.static_folder = 'static'
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)