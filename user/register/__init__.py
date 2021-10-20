import base64
from flask import Blueprint
from flask_restful import reqparse
from app import db
from app.models import User

register=Blueprint("register",__name__,url_prefix="/register")


@register.route("/",strict_slashes=False,methods=["POST"])
def register2():
    parser=reqparse.RequestParser()
    parser.add_argument("name",required=True,help="Your Username")
    parser.add_argument("email", required=True, help="Your Email")
    parser.add_argument("gender", required=True, help="Your Gender")
    parser.add_argument("password", required=True, help="Your Password")
    parser.add_argument("imageurl", required=True, help="Your Username")

    args=parser.parse_args()

    encoded_password = str(base64.b64encode(args['password'].encode('utf-8')), 'utf-8')

    username=User.query.filter_by(UserName=args["name"]).first()
    if username:
        return {
            "message":"The username you provided is already taken"
        },401

    person=User(UserName=args["name"],UserEmail=args["email"],UserGender=args["gender"],UserPassword=encoded_password,UserImageLink=args["imageurl"])
    db.session.add(person)
    db.session.commit()

    return {
               "Username": person.UserName,
               "Gender": person.UserGender,
               "ImageUrl": person.UserImageLink,
               "Age": person.UserAge,
               "Location": person.Location,
               "Job": person.UserJob,
               "About": person.About,
               "Interested In": person.UserPriority,
               "UserID": person.UserID,
           },201