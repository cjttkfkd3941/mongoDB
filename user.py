# user.py

from post import *
from wall import *
from follow import *

def signup(db):
    '''
    1. Get his/her information.
    2. Check if his/her password is equal. Confirm the password.
    3. Check if the userid already exists.
    4. Make the user document.
    5. Insert the document into users collection.
    '''
    # id_input

    try:

        id = input("id: ")
        if id =="":
            print("A length of id should be at least 1")
            return False

        if db.users.find_one({"_id": id}):
            raise NameError
            # Check if the userid already exists.

        pw = input("password: ")
        if pw == "":
            print("A length of password should be at least 1")
            return False
        else:
            pw1 = input("input password again:")

            if pw != pw1:
                print("Wrong password! try again!")
                raise ValueError

            name = input("name: ")
            if name == "":
                raise ValueError

            db.users.insert_one({"_id": id, "password": pw, "name": name,"status_message":[] , "followings": [], "followers": []})
            return
    except NameError:
        print("The user id already exists. Please try again with another!\n")
        print()
    except:
        print("[signup]Error! Try again.")
        print()
        signup(db)



def signin(db):
    '''
    1. Get his/her information.
    2. Find him/her in users collection.
    3. If exists, print welcome message and call userpage()
    '''
    try:

        print("-------------[login]--------------")

        id = input("ID: ")
        if id =="":
            print("A length of id should be at least 1")
            return False

        if not db.users.find_one({"_id": id}):
            print("not exist!\n")
            raise ValueError

        pw = input("password:")

        if not db.users.find_one({"_id": id, "password": pw}):
            print("Wrong Password! try again!\n")
            raise ValueError

        print("Welcome!\n")

        userpage(db, id)
    except:
        print("[signin]Error! Try again!")
        signin(db)



def mystatus(db, user):
    '''
    print user profile, # followers, and # followings
    '''

    followers = db.users.find_one({"_id": user}, {"followers": 1,"_id":0})['followers']
    followings = db.users.find_one({"_id": user}, {"followings": 1,"_id":0})['followings']
    status_message = db.users.find_one({"_id": user}, {"status_message": 1,"_id":0})['status_message']

    while True:

        try:

            print("="*100)
            print("Profile: \n Status_message: {0} \n Followers: {1} \n Followings: {2}\n".format(status_message, len(followers), len(followings)))
            print("=" * 100)

            b = input("\nIf you want to go back, press enter key")
            if b == "":
                return
            else:
                print("Wrong input!")
        except ValueError:
            print("[mystatus]Error! Invalid input! try again\n")


def userpage(db, user):
    '''
    user page
    '''


    while True:
        try:
            print("-----[Welcome FIRA!!]-----\n"
                  "1. My status\n"
                  "2. News feed\n"
                  "3. Wall\n"
                  "4. Post\n"
                  "5. Follow\n"
                  "6. Unfollow\n"
                  "7. Searching\n"
                  "8. Logout\n")
            b = int(input("\nChoose one:"))
            if b == 1:
                mystatus(db, user)
            elif b == 2:
                newsfeed(db,user)
            elif b == 3:
                getPosts(db,user)
            elif b == 4:
                postInterface(db, user)
            elif b == 5:
                following_list = db.users.find_one({"_id": user})["followings"]
                if following_list:
                    print("Your followings : ", following_list)
                else:
                    print("You have no followings")
                following = input("Input userid to follow:")
                follow(db, user, following)
            elif b == 6:
                following_list = db.users.find_one({"_id": user})["followings"]
                if following_list:
                    print("Your followings : ", following_list)
                else:
                    print("You have no followings")
                following = input("Input userid to unfollow")
                unfollow(db, user, following)
            elif b == 7:
                findTag(db, user)
            elif b == 8:
                return
            else:
                print("Wrong input!\n")

        except ValueError:
            print('[userpage]Error! Invalid input! try again\n')
