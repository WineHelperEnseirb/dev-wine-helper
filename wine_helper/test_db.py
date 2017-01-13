# coding: utf-8

import json

from django.test import TestCase, Client
from django.urls import reverse

import mock

from mongoengine import *
from django.test import TransactionTestCase
from db_tools import *

from mongoengine import connect

client = Client()

class DBTest(TestCase):
    nb_test_passed = 0
    nb_test = 5

    def test_add_user(self):
        create_user("1")
        create_user("2")
        create_user("3")
        create_user("3")
        users = get_users()
        self.assertEqual(len(users),3)
        self.assertEqual(users[0].user_id,"1")
        self.assertEqual(users[1].user_id,"2")
        self.assertEqual(users[2].user_id,"3")
        self.assertFalse(user[0] is None)
        print("TEST PASSED: test_add_user \n")
        nb_test_passed = nb_test_passed + 1

    def test_get_user(self):
        fbid = "1"
        create_user(fbid)
        user = get_user_by_id(fbid)
        no_user = get_user_by_id(-1)
        self.assertFalse(user is None)
        self.assertTrue(no_user is None)
        print("TEST PASSED: test_get_user \n")
        nb_test_passed = nb_test_passed + 1

    def test_create_criterion(self):
        fbid = "1"
        criterion1 = {"name":"color","value":"rouge"}
        criterion2 = {"name":"price","value":"10"}
        create_user(fbid)
        create_criterion(fbid,criterion1)
        user = get_user_by_id(fbid)
        self.assertTrue(user.current_search.criteria[0]["name"] == "color")
        self.assertTrue(user.current_search.criteria[0]["value"] == "rouge")
        create_criterion(fbid,criterion2)
        user = get_user_by_id(fbid)
        self.assertTrue(user.current_search.criteria[1]["name"] == "price")
        self.assertTrue(user.current_search.criteria[1]["value"] == "10")
        criterion1["value"] = "blanc"
        create_criterion(fbid,criterion1)
        user = get_user_by_id(fbid)
        self.assertTrue(user.current_search.criteria[0]["name"] == "color")
        self.assertTrue(user.current_search.criteria[0]["value"] == "blanc")
        print("TEST PASSED: test_create_criterion \n")
        nb_test_passed = nb_test_passed + 1

    def test_get_criteria_by_id(self):
        fbid = "1"
        create_user(fbid)
        criterion1 = {"name":"color","value":"rouge"}
        criterion2 = {"name":"price","value":"10"}
        create_criterion(fbid,criterion1)
        create_criterion(fbid,criterion1)
        criteria = get_criteria_data_by_id(fbid)
        self.assertEqual(len(criteria),2)
        print("TEST PASSED: test_get_criteria_by_id \n")
        nb_test_passed = nb_test_passed + 1

    def test_close_search(self):
        fbid = "1"
        create_user(fbid)
        criterion1 = {"name":"color","value":"rouge"}
        criterion2 = {"name":"price","value":"10"}
        create_criterion(fbid,criterion1)
        create_criterion(fbid,criterion1)
        user = get_user_by_id(fbid)
        old_search = user.current_search[:]
        close_search(fbid)
        user = get_user_by_id(fbid)
        self.assertTrue(user.current_search == [])
        self.assertTrue(user.searches[len(user.searches) - 1] == old_search)
        print("TEST PASSED: test_close_search \n")
        nb_test_passed = nb_test_passed + 1

    def test_print_results:
        print ("\n Nombre de succès/Nombre de tests : " + nb_test_passed+ "/" + nb_test)
