from __future__ import unicode_literals

from django.db import models
from mongoengine import *

class Criterion(EmbeddedDocument):
    name = StringField()
    value = DynamicField()

class Search(EmbeddedDocument):
    user_storyline = StringField()
    criteria = ListField(EmbeddedDocumentField(Criterion))

class User(Document):
    user_id = StringField()
    current_search = EmbeddedDocumentField(Search)
    searches = ListField(EmbeddedDocumentField(Search))
    meta = {'collection': 'users'}
