from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PartnerUpdate, ProductInfoViewSet, BasketView, OrderView


app_name = 'backend'

router = DefaultRouter()
router.register(r'product', ProductInfoViewSet, basename='products')

urlpatterns = [
    # Путь для обновления прайса от поставщика
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    # Путь для просмотра корзины
    path('basket', BasketView.as_view(), name='basket'),
    # Путь для просмотра заказа
    path('order', OrderView.as_view(), name='order'),
] + router.urls

