import pymongo
from pymongo import MongoClient


host = 'localhost'
port = 27017

client = MongoClient(host, port)
db = client.database

def _insert_user_id_to_db():
    with open('resources/user_id.txt') as f:
        data = f.readlines()
    uid = [i.split('\n')[0] for i in data]
    print(uid)
    for id in uid:
        db['sojo_fb_uid'].insert_one({'fb_user_id': id})

def get_one_uid():
    res = db['sojo_fb_uid'].find_one()
    _id, result = res['_id'], res['fb_user_id']
    del_stat = db['sojo_fb_uid'].delete_one({"_id": _id})
    return str(result)

def push_one_uid(_user_id):
    db['sojo_fb_uid'].insert_one({'fb_user_id': _user_id})

def push_one_user_profile(uid, data):
    db['sojo_fb_profile'].insert_one({'_id': uid, "profile": data})

def main():
    # _insert_user_id_to_db()
    pass
if __name__ == '__main__':
    main()



