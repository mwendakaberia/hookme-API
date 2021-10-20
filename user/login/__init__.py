import base64
from app.models import User
from flask_restful import reqparse
from flask import Blueprint

login=Blueprint("login",__name__,url_prefix="/login")


@login.route("/",strict_slashes=False,methods=["POST"])
def login2():
    parser=reqparse.RequestParser()
    parser.add_argument("name",required=True,help="Enter your Username")
    parser.add_argument("password", required=True, help="Enter your Password")

    args=parser.parse_args()

    valid=User.query.filter_by(UserName=args["name"]).first()

    if not valid:
        return {
            "message":"wrong username"
        },401

    encoded_password = str(base64.b64encode(args['password'].encode('utf-8')), 'utf-8')

    if valid.UserPassword==encoded_password:
        return {
            "Username":valid.UserName,
            "Gender":valid.UserGender,
            "ImageUrl":valid.UserImageLink,
            "Age":valid.UserAge,
            "Location":valid.Location,
            "Job":valid.UserJob,
            "About":valid.About,
            "Interested In":valid.UserPriority,
            "UserID": valid.UserID,
        },200
    else:
        return {
                   "message": "wrong password"
               }, 401