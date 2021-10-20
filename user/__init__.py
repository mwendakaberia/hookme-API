from app import db
from app.models import User
from flask import Blueprint
from flask_restful import reqparse

settings=Blueprint("settings",__name__,url_prefix="/settings")


@settings.route("/<userid>",strict_slashes=False,methods=["PUT"])
def settings2(userid):
    parser=reqparse.RequestParser()
    parser.add_argument("name")
    parser.add_argument("age")
    parser.add_argument("location")
    parser.add_argument("job")
    parser.add_argument("about")
    parser.add_argument("likes")
    parser.add_argument("imageurl")

    args=parser.parse_args()

    username=User.query.filter_by(UserName=args["name"]).first()
    if username:
        return {
            "message":"username already taken"
        },401

    result=User.query.filter_by(UserID=userid).first()

    if args["age"]:
        result.UserAge=args["age"]
    if args["location"]:
        result.Location=args["location"]
    if args["job"]:
        result.UserJob=args["job"]
    if args["about"]:
        result.About=args["about"]
    if args["likes"]:
        result.UserPriority=args["likes"]
    if args["name"]:
        result.UserName=args["name"]
    if args["imageurl"]:
        result.UserImageLink=args["imageurl"]
        
    db.session.add(result)
    db.session.commit()

    return {
               "Username": result.UserName,
               "Gender": result.UserGender,
               "ImageUrl": result.UserImageLink,
               "Age": result.UserAge,
               "Location": result.Location,
               "Job": result.UserJob,
               "About": result.About,
               "Interested In": result.UserPriority,
               "UserID":result.UserID,
           }, 201

