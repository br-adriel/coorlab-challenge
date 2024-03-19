from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Travel
from .serializers import TravelSerializer

# Create your views here.
@api_view()
def get_destinations_view(request):
    destinations = Travel.objects.values_list('city', flat=True)
    destinations = list(dict.fromkeys(list(destinations)))
    return Response(destinations)

@api_view()
def get_all_view(request):
    travels = Travel.objects.all()

    paginator = PageNumberPagination()
    paginated_data = paginator.paginate_queryset(travels, request)
    
    serializer = TravelSerializer(paginated_data, many=True)
    return paginator.get_paginated_response(serializer.data)
