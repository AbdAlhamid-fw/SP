from djangochannelsrestframework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models import Sales
from ..serializers import SalesSerializer


class SalesView(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = (AllowAny,)
