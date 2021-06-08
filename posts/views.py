"""Posts views."""
# Django
from django.shortcuts import render

# Utilities
from datetime import datetime

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Juan Kike',
            'picture': 'http://picsum.photos/60/60/?image=1003',

        },
        'timestamp': datetime.now().strftime("%c"),
        'photo': 'http://picsum.photos/800/600/?image=703',
    },
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Juan Kike',
            'picture': 'http://picsum.photos/60/60/?image=1010',

        },
        'timestamp': datetime.now().strftime("%c"),
        'photo': 'http://picsum.photos/800/800/?image=704',
    },
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Juan Kike',
            'picture': 'http://picsum.photos/60/60/?image=1022',

        },
        'timestamp': datetime.now().strftime("%c"),
        'photo': 'http://picsum.photos/500/700/?image=722',
    },
    
]



# Create your views here.
def list_posts(req):
    """List existing posts."""
    return render(req, 'feed.html', { 'posts': posts })