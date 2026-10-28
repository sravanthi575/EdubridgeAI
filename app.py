import os

import click
from flask import Flask, render_template

from config import Config
from extensions import csrf, db, login_manager


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    os.makedirs(os.path.join(app.root_path, "instance"), exist_ok=True)

    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please log in to continue."
    login_manager.login_message_category = "info"

    import models  # noqa: F401  (registers tables)
    from routes.admin import bp as admin_bp
    from routes.ai_tutor import bp as ai_bp
    from routes.auth import bp as auth_bp
    from routes.career import bp as career_bp
    from routes.community import bp as community_bp
    from routes.courses import bp as courses_bp
    from routes.main import bp as main_bp
    from routes.paths import bp as paths_bp
    from routes.quizzes import bp as quizzes_bp
    from routes.scholarships import bp as scholarships_bp
    for bp in (main_bp, auth_bp, courses_bp, quizzes_bp, ai_bp, paths_bp,
               career_bp, scholarships_bp, community_bp, admin_bp):
        app.register_blueprint(bp)

    @app.after_request
    def security_headers(resp):
        resp.headers.setdefault("X-Content-Type-Options", "nosniff")
        resp.headers.setdefault("X-Frame-Options", "DENY")
        resp.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        return resp

    for code, msg in ((403, "You do not have permission to view this page."),
                      (404, "We could not find that page."),
                      (400, "That request could not be processed. Please go back and try again."),
                      (500, "Something went wrong on our side.")):
        app.register_error_handler(code, lambda e, code=code, msg=msg: (render_template("error.html", code=code, message=msg), code))

    @app.cli.command("seed")
    def seed_command():
        """Load starter courses and scholarships into an empty database."""
        from seed import seed_content
        seed_content()
        click.echo("Seed complete.")

    @app.cli.command("create-admin")
    @click.option("--email", prompt=True)
    @click.option("--name", prompt=True, default="Administrator")
    @click.password_option()
    def create_admin(email, name, password):
        """Create (or promote) an administrator account."""
        from models import User
        email = email.strip().lower()
        user = User.query.filter_by(email=email).first() or User(email=email)
        user.name, user.is_admin = name, True
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        click.echo(f"Admin ready: {email}")

    with app.app_context():
        db.create_all()
        if app.config.get("AUTO_SEED"):
            from seed import seed_content
            seed_content()
        _bootstrap_admin_from_env()
    return app


def _bootstrap_admin_from_env():
    from models import User
    email = (os.environ.get("ADMIN_EMAIL") or "").strip().lower()
    password = os.environ.get("ADMIN_PASSWORD") or ""
    if not email or not password or User.query.filter_by(email=email).first():
        return
    user = User(email=email, name=os.environ.get("ADMIN_NAME", "Administrator"), is_admin=True)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
