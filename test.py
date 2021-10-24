#!/usr/bin/env python3

import inspect
import os
os.environ.setdefault( "DJANGO_SETTINGS_MODULE", "settings" )
from django.db import connection
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# App-specific imports
from standalone.models import Test

def clean_data():
    Test.objects.all().delete()

def test_setup():
    try:
        clean_data()
        test = Test( name = "name" )
        test.save()
        assert Test.objects.count() > 0
        print( "Django Model setup completed." )
        clean_data()
    except AssertionError as exception:
        print( "Django Model setup failed with error:" )
        raise Exception
    except:
        print( "Unexpected error" )

test_setup()