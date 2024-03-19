from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Travel

# Create your views here.
@api_view()
def get_destinations_view(request):
    destinations = Travel.objects.values_list('city', flat=True)
    destinations = list(dict.fromkeys(list(destinations)))
    return Response(destinations)

