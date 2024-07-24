import os
import sys


os.environ.setdefault('DJANGO_SETTINGS_MODULE','mytestapp.settings')

import django
django.setup()


import random
from mytestapp.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','social','Marketplace','News','Games']


def add_topics():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):

    for entry in range(n):
        top = add_topics()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.name()


        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url, name=fake_name)[0]
        accr = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]
if __name__ == '__main__':
    print("scripting")
    populate(20)
    print("completed")
