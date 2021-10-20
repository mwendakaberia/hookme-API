from app import db


deleteforme=db.Table("deleteforme",
                     db.Column("UserID",db.Integer, db.ForeignKey("user.UserID")),
                     db.Column("MessageID",db.Integer,db.ForeignKey("messages.MessageID"))
                     )


class User(db.Model):
    #__tableName__ = "User"
    UserID=db.Column(db.Integer,primary_key=True)
    UserName=db.Column(db.String,nullable=False)
    UserEmail=db.Column(db.String,nullable=False)
    UserGender=db.Column(db.String,nullable=False)
    UserAge=db.Column(db.String)
    Location=db.Column(db.String)
    UserJob = db.Column(db.String)
    About = db.Column(db.String)
    UserPriority = db.Column(db.String)
    UserPassword = db.Column(db.String, nullable=False)
    UserImageLink=db.Column(db.String,nullable=False)

    #Relationships
    message_user_rltn=db.relationship("Messages",backref="message_userid")
    matches_user_rltn=db.relationship("Matches",backref="matches_userid")
    delete_message_rltn=db.relationship("Messages",secondary=deleteforme,backref=db.backref("delete_message",lazy="dynamic"))


class Chats(db.Model):
    ChatID=db.Column(db.Integer,primary_key=True)
    SenderID=db.Column(db.Integer,db.ForeignKey("user.UserID"))
    ReceiverID=db.Column(db.Integer,db.ForeignKey("user.UserID"))
    Read_Unread = db.Column(db.Boolean, nullable=False, default=False)
    Deleted=db.Column(db.Boolean,nullable=False,default=False)
    Deleted_By=db.Column(db.Integer)

    #Relationships
    message_chat_rltn=db.relationship("Messages",backref="message_chatid")


class Messages(db.Model):
    MessageID=db.Column(db.Integer,primary_key=True)
    ReceiverID=db.Column(db.Integer,nullable=False)
    Message=db.Column(db.String,nullable=False)
    TimeSent=db.Column(db.DateTime,nullable=False)
    DeleteForEveryone=db.Column(db.Boolean,default=False)
    UserID=db.Column(db.Integer,db.ForeignKey("user.UserID"))
    ChatID=db.Column(db.Integer,db.ForeignKey("chats.ChatID"))


class Matches(db.Model):
    MatchID=db.Column(db.Integer,primary_key=True)
    ReceiverID=db.Column(db.Integer,nullable=False)
    Connected=db.Column(db.Boolean,default=False)
    User_id = db.Column(db.Integer, db.ForeignKey("user.UserID"))





