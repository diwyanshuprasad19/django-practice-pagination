from rest_framework.pagination import LimitOffsetPagination


class APIPagination(LimitOffsetPagination):

    def __init__(self, params):
        self.limit = int(params.get("limit", 25))
        self.offset = int(params.get("offset", 0))
        self.template = None

    def get_paginated_response(self, data):
        return {
            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        }

    def paginate_queryset(self, queryset, request):
        self.request = request
        self.count = self.get_count(queryset)
        if self.count > self.limit and self.template is not None:
            self.display_page_controls = True

        if self.count == 0 or self.offset > self.count:
            return []
        return list(queryset[self.offset:self.offset + self.limit])