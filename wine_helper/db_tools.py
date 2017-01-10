from models import Criterion,Search,User
from pprint import pprint



def get_user_by_id (fbid):
    try:
        user = User.objects.get(user_id=fbid)
    except User.DoesNotExist:
        user = None
    return user

def create_user (fbid):
    user = get_user_by_id(fbid)
    if user == None:
        pprint("[DEBUG] USER CREATED WITH FBID: " + fbid + "\n")
        user = User(user_id=fbid, current_search=Search(criteria=[]), searches=[])
    else:
        pprint("[DEBUG] create user else")

def close_search (fbid):
    user = get_user_by_id(fbid)
    if user != None:
        if user.current_search != None:
            user.searches.append(current_search)
            user.current_search = Search(criteria=[])
            user.modify()
            user.save()

def create_criterion (fbid,criterion):
    user = get_user_by_id(fbid)
    is_created = False
    if user != None:
        current_search = user.current_search
        for c in current_search:
            if c['name'] == criterion['name']:
                is_created = True
                c['value'] = criterion['value']
        if not is_created:
            cr = Criterion(criterion["name"],criterion["value"])
            user.criteria.append(cr)
        user.modify()
        user.save()


create_user(0)
create_user(1)
create_user(1)
create_user(2)
