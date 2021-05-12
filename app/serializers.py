from marshmallow_sqlalchemy.schema import load_instance_mixin
from app import ma
from app.models import User, School


class SchoolSchema(ma.SQLAlchemySchema):
    class Meta:
        model = School
        load_instance = True

    id = ma.auto_field()
    nome = ma.auto_field()
    tipo = ma.auto_field()
    telefone = ma.auto_field()
    email = ma.auto_field()
    logradouro = ma.auto_field()
    bairro = ma.auto_field()
    cidade = ma.auto_field()
    uf = ma.auto_field()
    cep = ma.auto_field()


school_schema = SchoolSchema()
schools_schema = SchoolSchema(many=True)
