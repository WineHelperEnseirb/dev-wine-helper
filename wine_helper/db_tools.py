#!/usr/bin/python
# -*- coding: utf-8 -*-

# System dependencies
from pprint import pprint

from models import Criterion, Search, User


def get_users ():
    """
    TODO: write description
    """
    try:
        users = User.objects.get()
        return users
    except User.DoesNotExist:
        return []


def get_user_by_id(fbid):
    """
    TODO: get description
    """
    try:
        user = User.objects.get(user_id=fbid)
    except User.DoesNotExist:
        user = None
    return user


def create_user(fbid):
    """
    TODO: write description
    """
    user = get_user_by_id(fbid)
    if user is None:
        pprint("[DEBUG][db_tools.py][create_user] user is None")
        user = User(user_id=fbid, current_search=Search(criteria=[]), searches=[])
        user.save()
    else:
        pprint("[DEBUG] create user else")


def close_search(fbid):
    """
    TODO: write description
    """
    user = get_user_by_id(fbid)
    if user is not None:
        if user.current_search is not None:
            user.searches.append(current_search)
            user.current_search = Search(criteria=[])
            user.modify()
            user.save()


def create_criterion(fbid, criterion):
    """
    TODO: write description
    """
    user = get_user_by_id(fbid)
    is_created = False
    if user is not None:
        pprint(">>>> [DEBUG][db_tools.py][create_criterion] current_search")
        for i in range(len(user.current_search.criteria)):
            if user.current_search.criteria[i]["name"] == criterion["name"]:
                pprint("[DEBUG] c.name: " + c["name"])
                pprint("[DEBUG] criterion.name: "  + criterion["name"])
                is_created = True
                user.current_search.criteria[i]["value"] = str(criterion["value"])
                user.update()
        if not is_created:
            cr = Criterion(criterion["name"], str(criterion["value"]))
            user.current_search.criteria.append(cr)
        user.save()


def get_criteria_data_by_id (fbid):
    """
    get current criteria: a list/array of all the criteria of the current search
    """
    user = get_user_by_id (fbid)
    if user is not None:
        return user.current_search.criteria
    else:
        return None
