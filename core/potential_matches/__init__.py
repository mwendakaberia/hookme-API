from flask import Blueprint
from flask_restful import fields,marshal_with

potential_matches=Blueprint("potential_matches",__name__,url_prefix="potential_matches")

resource_fields={
    "UserID":fields.Integer,
    "UserName":fields.String,
    "UserGender":fields.String,
    "UserAge":fields.String,
    "Location":fields.String,
    "UserJob":fields.String,
    "About":fields.String,
    "UserImageLink":fields.String
}


@potential_matches.route("/",strict_slashes=False,methods=["GET"])
@marshal_with(resource_fields)
def options():
    pass