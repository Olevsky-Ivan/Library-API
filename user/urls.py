from django.urls import include, path
from rest_framework.routers import DefaultRouter
from user.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='book')

urlpatterns = [
    path('api/', include(router.urls)),
]

app = "user"
