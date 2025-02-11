from django.urls import include, path
from borrowing.views import BookViewSet, PaymentViewSet, BorrowingViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'borrowings', BorrowingViewSet, basename='borrowing')

urlpatterns = [
    path('api/', include(router.urls)),
]


app = "borrowing"