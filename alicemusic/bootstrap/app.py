from flask import Flask


def create_app(config_filename=None):
    app = Flask(__name__)
    if config_filename:
        app.config.from_pyfile(config_filename)

    # from yourapplication.model import db
    # db.init_app(app)

    from alicemusic.view import downloader
    # from yourapplication.views.frontend import frontend
    app.register_blueprint(downloader)
    # app.register_blueprint(frontend)

    return app
