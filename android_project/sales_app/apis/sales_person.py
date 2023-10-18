from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from ..models import SalesPerson
from ..serializers import SalesPersonSerializer


class SalesPersonView(viewsets.ModelViewSet):
    queryset = SalesPerson.objects.all()
    serializer_class = SalesPersonSerializer
    permission_classes = (AllowAny,)
