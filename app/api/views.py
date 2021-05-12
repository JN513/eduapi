from . import api
from app.models import User, School

@api.route("/")
def index():
    ...