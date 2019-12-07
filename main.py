# main.py
from pymongo import MongoClient
from user import *

client = MongoClient()
db = client.sns_project

def mainpage(db):
    '''
    call signup() or signin()
    '''
    print("\n\n\n\n\n[[**---Wellcome to Mongo SNS---**]]\n"
          "\n--------[ Menu ]--------\n"
          "\n1.Sign up\n"
          "2.Sign in\n"
          "3.Exit\n")

    try:

        sign = int(input("\nchoose one:"))
        if sign == 1:
            signup(db)
        elif sign == 2:
            signin(db)
        elif sign == 3:
            exit()
        else:
            print("[M_Error]Wrong input! try again.\n")
    except ValueError:
        print('[M_Error]Invalid input! try again\n')
    mainpage(db)


if __name__ == "__main__":
    '''
    call mainpage()
    '''
    if db.users.find()==[]:
        db.users.insert_one(
            {"_id": 'root', "password": 'root', "name": 'root', "status_message": [], "followings": [], "followers": []})

    if db.posts.find()==[]:
        db.posts.insert_one(
        {"_id": 0, "Title": '공지사항', "Text": '인덱스를 위한글', "Date": '2000-10-12 22:16:10', "Writerid": 'root', "Writername": 'root',"tags":[],
         "comment": []})
        db.posts.create_index([("Writerid", 1), ("_id", -1)])

    mainpage(db)
