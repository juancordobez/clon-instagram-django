""" cloninstagram """
# Django
from django.http import HttpResponse
# Utilities
from datetime import datetime
import json


def hello_word(req):
    """ Return a greeting."""

    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now = datetime.now().strftime("%c")
    ))

def sorted_integers(req):
    """Return  a JSON response with sorted integers."""
    
    num_sort = sorted([int(i) for i in req.GET['numbers'].split(',')])

    data = {
        'status': 'ok',
        'numbers': num_sort,
        'message': 'Integers sorted successfully.'
    }
    
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json'
    )

def say_hi(req, name, age):
    """Return a greeting."""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to'.format(name)
    return HttpResponse(message)