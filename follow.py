def follow(db, userid, following):
    """
    Get the followers.
    This function updates information that is user's followers or followings.
    Note that if a user asks following to someone, the follower's information should be also updated.
    Remember, you may regard duplicates and the situation that the follower does not exists.
    """

    try:
        if db.users.find_one({"_id":following}):
            if following in db.users.find_one({'_id': userid}, {'followings': 1, "_id": 0})['followings']:
                raise ValueError
            else:
                # 일단 팔로잉 명단에 있는가 확인,팔로워 명단에 있는가 확인
                # 그리고 둘다 명단에 없으면서 둘다 아이디가 존재해야 넣을수있음
                # 또 고려사항 뭐가 있지?
                db.users.update_one({'_id': userid}, {'$push': {'followings': following}})
                db.users.update_one({'_id': following}, {'$push': {'followers': userid}})
                print("Follow completed.")
        else:
            print("The id is not exist.")

    except ValueError:
        print("You are already following.")

        
def unfollow(db, userid, following):
    """
    Unfollow someone.
    A user hopes to unfollows follwings.
    You can think that this function is the same as the follow but the action is opposite.
    The information apply to followings and followers both.
    Again, the confimation is helpful whether the user really wants to unfollow others.
    """
    try:
        if db.users.find_one({"_id":following}):
            if following not in db.users.find_one({'_id':userid},{'followings':1,"_id":0})['followings']:
                raise ValueError
            else:
                # 이경우는반대지만 명단에 있는가 확인, 없는가 확인
                # 둘다 명단에 있으면서 존재해야 삭제 가능
                # 추가 고려사항 고민!
                db.users.update_one({'_id': userid}, {'$pull': {'followings': following}})
                db.users.update_one({'_id': following}, {'$pull': {'followers': userid}})
                print("Unfollow completed.")
        else:
            raise TypeError


    except ValueError:
        print("The id is not followed yet.")
    except TypeError:
        print("The id is not exist.")
    except:
        print("Error발생")