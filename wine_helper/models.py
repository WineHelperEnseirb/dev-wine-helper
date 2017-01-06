from __future__ import unicode_literals

from django.db import models
from mongoengine import *

class Search(Document):
    user_id = StringField()
