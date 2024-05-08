from rest_framework.response import Response
from rest_framework.views import APIView
from .pagination import APIPagination
from .serializers import MyModelSerializer
from .models import MyModel

class MyModelListView(APIView):
    pagination_class = APIPagination

    def get(self, request, format=None):
        # Get the query parameters
        limit = request.GET.get('limit', None)
        offset = request.GET.get('offset', None)

        # Convert string parameters to integers if provided
        if limit is not None:
            try:
                limit = int(limit)
            except ValueError:
                return Response({"error": "Invalid limit value. Limit must be an integer."}, status=400)
        
        if offset is not None:
            try:
                offset = int(offset)
            except ValueError:
                return Response({"error": "Invalid offset value. Offset must be an integer."}, status=400)

        # Create an instance of the pagination class with the provided parameters
        paginator = self.pagination_class(request.GET, limit=limit, offset=offset)
        queryset = MyModel.objects.all()

        # Paginate the queryset using custom pagination class
        paginated_queryset = paginator.paginate_queryset(queryset, request)

        serializer = MyModelSerializer(paginated_queryset, many=True)

        # Construct the custom response
        response_data = {
            'count': paginator.count,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
            'results': serializer.data
        }

        return Response(response_data)
    
# to only see limit =2 http://127.0.0.1:8000/myapp/data/?limit=2 see like this use params