from django.urls import path
from rest_framework.routers import DefaultRouter
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

from .views import PartnerUpdate, ProductInfoViewSet, RegisterAccount, ConfirmAccount, LoginAccount, PartnerState, AccountDetails, ContactView, PartnerOrders, BasketView, OrderView


app_name = 'backend'

router = DefaultRouter()
router.register(r'product', ProductInfoViewSet, basename='products') # Путь для работы с товарами  

urlpatterns = [      
    path('user/register', RegisterAccount.as_view(), name='user-register'), # Путь для регистрации пользователя   
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'), # Путь для подтверждения аккаунта пользователя  
    path('user/login', LoginAccount.as_view(), name='user-login'),  # Путь для авторизации пользователя
    path('user/details', AccountDetails.as_view(), name='user-details'), # Путь для работы со параметрами пользователя
    path('user/password_reset', reset_password_request_token, name='password-reset'), # Путь для сброса пароля пользователя
    path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'), # Путь для подтверждения сброса пароля пользователя    
    path('user/contact', ContactView.as_view(), name='user-contact'), # Путь для работы с контактами
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'), # Путь для обновления прайса от поставщика   
    path('partner/state', PartnerState.as_view(), name='partner-state'), # Путь для работы со статусом поставшика
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'), # Путь для получения заказов поставшика
    path('basket', BasketView.as_view(), name='basket'), # Путь для работы с корзиной    
    path('order', OrderView.as_view(), name='order'), # Путь для работы с заказами
] + router.urls
