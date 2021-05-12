from . import api
from app.models import User, School


@api.route("/")
def index():
    ...


@api.route("/escolas")
def schools():
    ...
