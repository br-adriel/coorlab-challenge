from datetime import datetime
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

@api_view(['post'])
def travel_options_view(request):
    # check if required data is passed
    if any(field not in request.data.keys() for field in ['date', 'city']):
        return Response(status=400)
    
    # parse date string sended on request to datetime type
    # the travel date consider end of day for same day travel situation
    parsed_date = request.data['date'].split('-')
    travel_date = datetime(
        int(parsed_date[0]), 
        int(parsed_date[1]), 
        int(parsed_date[2]), 
        23, 59, 59
    )
    
    today = datetime.now()
    if travel_date < today:
        return Response(status=400)
    
    hours_to_travel = travel_date  - today

    query = Travel.objects.filter(
        city__iexact=request.data['city'],
        duration__lte=hours_to_travel
    )
    best_option = query.order_by('duration').first()
    cheapest_option = query.order_by('price_econ').first()
    
    serialized_response = {
        'best_option': None if best_option is None else TravelSerializer(best_option).data,
        'cheapest_option': None if cheapest_option is None else TravelSerializer(cheapest_option).data
    }
    return Response(serialized_response)