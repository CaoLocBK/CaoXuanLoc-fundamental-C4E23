import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds159200.mlab.com:59200/movie

host = "ds159200.mlab.com"
port = 59200
db_name = "movie"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())

from mongoengine import Document, StringField, IntField
class Newbike(Document):
    model = StringField()
    dailyfee = StringField()
    image = StringField()
    year = IntField()

