import os
from app import create_app, db
from app.models import User, School

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "User": User,
        "School": School,
    }


if os.environ.get("ENV") == "development" and __name__ == "__main__":
    app.run()
