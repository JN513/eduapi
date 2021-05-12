from . import api
from flask import request, jsonify
from app.models import User, School
from app.serializers import schools_schema


@api.route("/")
def index():
    ...


@api.route("/escolas")
def schools():
    uf = request.args.get("uf") if request.args.get("uf") else "all"
    tipo = request.args.get("tipo") if request.args.get("tipo") else "all"
    cep = request.args.get("cep") if request.args.get("cep") else "all"
    cidade = request.args.get("cidade") if request.args.get("cidade") else "all"

    escolas = School.query

    if tipo != "all":
        escolas = escolas.filter_by(tipo=tipo)

    if cep != "all":
        escolas = escolas.filter_by(cep=cep)

        return jsonify(schools_schema.dump(escolas))

    if uf != "all":
        escolas = escolas.filter_by(uf=uf)

    if cidade != "all":
        escolas = escolas.filter_by(cidade=cidade)

    return jsonify(schools_schema.dump(escolas))
