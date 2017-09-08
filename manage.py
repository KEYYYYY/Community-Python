from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from app.auth.modles import User
from app.home.models import Article, Follow, Comment

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(
        app=app,
        db=db,
        User=User,
        Article=Article,
        Follow=Follow,
        Comment=Comment
    )


if __name__ == '__main__':
    manager.run()
