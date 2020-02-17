import sys
import datetime
from pymongo import MongoClient

#####################################
# main program                      #
#####################################

mongoURL = sys.argv[1]
adminPwd = sys.argv[2]

client = MongoClient('mongodb://' + mongoURL + '/')

adminUser = {"type": "ADMIN",
             "isSuperAdmin": True,
             "defaultAccessLevel": "antenna",
             "authorizedAlgorithms": {
                 "density": "antenna"
             },
             "username": "admin",
             "token": "qwerty1234",
             "quota": 10,
             "currentQuota": 10,
             "created": datetime.datetime.utcnow()
             }

user_already_exists = client.opal.eae_users.find_one({"username": "admin"})
if not user_already_exists:
    client.opal.eae_users.insert_one(adminUser)

client.close()
