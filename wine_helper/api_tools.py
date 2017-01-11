#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests as re
from pprint import pprint

import Wine as W
import Criteria as C

# "Constants" (variables that should not change)
API_BASE_URL = "http://wine-helper-fake-api.herokuapp.com/public/api/wines"


def get_wines_by_criteria(criteria, limit=0):
    """
    Makes an API call with the given criteria and returns a list of wines
    (class Wine)
    """
    url = API_BASE_URL
    # setting limit
    query = "?limit={0}".format(limit)
    # setting criteria
    for criterion in criteria:
        # TODO: remove last &
        query += "&" + criterion.get_name() + "=" + criterion.get_value()
    pprint("[DEBUG] query")
    pprint(query)
    url += query

    response = re.get(url)
    data = response.json()
    wine_list = []
    for wine in data:
        wine_object = W.Wine(
            wine['appellation'].encode('utf-8'),
            wine['name'].encode('utf-8'),
            int(wine['vintage']),
            float(wine['price']),
            float(wine['globalScore']),
            {
                'fr': wine['color']['fr'].encode('utf-8'),
                'en': wine['color']['en'].encode('utf-8')
            },
            {
                'fr': wine['taste']['fr'].encode('utf-8'),
                'en': wine['taste']['en'].encode('utf-8')
            }
        )
        wine_list.append(wine_object)
    return wine_list


# TODO: review this function
def build_wine_list (data, limit):
    pprint("[DEBUG][api_tools.py][build_wine_list] data")
    pprint(data)
    criterion = data["criterion"]
    pprint("[DEBUG] WIT CRITERION")
    criteria_list = []
    crit = C.Criteria(criterion["name"], criterion["value"].encode('utf-8'))
    criteria_list.append(crit)
    pprint("[DEBUG] BUILT CRITERION")
    #pprint(criteria_list)
    return get_wines_by_criteria(criteria_list, limit)
