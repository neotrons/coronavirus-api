from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from ..models import Case
from .serializers import CaseSerializer


class CasesViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = CaseSerializer
    queryset = Case.objects.all()
    pagination_class = None
    search_fields = ('country_region', 'province_state')

