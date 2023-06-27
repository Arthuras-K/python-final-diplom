from django.urls import path, include
from rest_framework import routers

from .views import PartnerUpdate

app_name = 'backend'

router = routers.SimpleRouter()

urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('', include(router.urls)),
] + router.urls

