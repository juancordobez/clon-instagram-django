"""Posts views."""
# Django
from django.http import HttpResponse

# Create your views here.
def list_posts(req):
    """List existing posts."""
    posts = [1,2,4]
    return HttpResponse(str(posts))