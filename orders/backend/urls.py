from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PartnerUpdate, ProductInfoViewSet, BasketView, OrderView, RegisterAccount, ConfirmAccount


app_name = 'backend'

router = DefaultRouter()
router.register(r'product', ProductInfoViewSet, basename='products')

urlpatterns = [      
    path('user/register', RegisterAccount.as_view(), name='user-register'), # Путь для регистрации пользователя   
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'), # Путь для подтверждения аккаунта пользователя    
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'), # Путь для обновления прайса от поставщика    
    path('basket', BasketView.as_view(), name='basket'), # Путь для просмотра корзины    
    path('order', OrderView.as_view(), name='order'), # Путь для просмотра заказа
] + router.urls

