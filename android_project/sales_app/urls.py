from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers
from . import view
from .apis.sales import SalesView
from .apis.sales_person import SalesPersonView

router = DefaultRouter()
router1 = DefaultRouter()
router.register(r'sales', SalesView)
router1.register(r'sales_person', SalesPersonView)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(router1.urls)),
    path('login/', view.login, name='login'),
    path('register/', view.register, name='register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
 ]