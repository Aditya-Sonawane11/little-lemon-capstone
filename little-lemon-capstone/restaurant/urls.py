from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, BookingViewSet, RegisterView, ObtainAuthTokenView

router = DefaultRouter()
router.register("menu/items", MenuItemViewSet, basename="menu-item")
router.register("booking/tables", BookingViewSet, basename="booking")

urlpatterns = [
    path("", include(router.urls)),
    path("registration/", RegisterView.as_view(), name="registration"),
    path("token/login/", ObtainAuthTokenView.as_view(), name="token-login"),
]
