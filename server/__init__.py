from flask import Flask, request
from urllib.parse import urlsplit
from datetime import datetime
from flask_login import LoginManager, current_user
from flask_migrate import Migrate
from .models import db, User, Short_URL
from .appConfig import config_dict
from .routes import endpoints



def init_app(*args, ver:int = 1, config=config_dict['prod'], **kwargs):
    app = Flask(*args, **kwargs)
    app.config.from_object(config)


    
    db.init_app(app)
    migrate = Migrate(app, db)
    
    with app.app_context():
        db.create_all()
    
    login_manager = LoginManager()
    login_manager.login_view = 'endpoints.login_endpoint'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user_func(id):
        return User.query.get(int(id))

   
    app.register_blueprint(endpoints)

    @app.context_processor
    def contexts():
        def esc_url(url: str):
            url_path = urlsplit(url).path + '?' + urlsplit(url).query if urlsplit(url).query else urlsplit(url).path
            url = request.url_root[:-1] + url_path if request.url_root.endswith('/') else request.url_root + url_path
            url = url.replace('https:', '').replace('http:', '')
            return url

        return dict(
            esc_url=esc_url,
            current_year=datetime.now().strftime('%Y'),
            app_version=ver,
            user=current_user,
        )
    @app.shell_context_processor
    def make_shell_context():
        return {
        'db': db,
        'User': User,
        'Short_URL': Short_URL
    }
    return app