import os
from app import create_app, db

app = create_app()

if os.environ.get("ENV") == "development" and __name__ == "__main__":
    app.run()
