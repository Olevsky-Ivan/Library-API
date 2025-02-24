from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS
from rest_framework import viewsets

from lybrary.utils import delete_cache
from borrowing.models import Book, Borrowing, Payment
from borrowing.serializers import BookSerializer, PaymentSerializer, BorrowingSerializer


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class BaseCachedViewSet(viewsets.ModelViewSet):
    CACHE_KEY_PREFIX = None

    def clear_cache(self):
        delete_cache(self.CACHE_KEY_PREFIX)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        self.clear_cache()
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        self.clear_cache()
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        self.clear_cache()
        return response


class BookViewSet(BaseCachedViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser | ReadOnly]
    CACHE_KEY_PREFIX = "books_view"

    @method_decorator(cache_page(300, key_prefix=CACHE_KEY_PREFIX))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PaymentViewSet(BaseCachedViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAdminUser | ReadOnly]
    CACHE_KEY_PREFIX = "payments_view"

    @method_decorator(cache_page(300, key_prefix=CACHE_KEY_PREFIX))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class BorrowingViewSet(BaseCachedViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    permission_classes = [IsAdminUser | ReadOnly]
    CACHE_KEY_PREFIX = "borrowings_view"

    @method_decorator(cache_page(300, key_prefix=CACHE_KEY_PREFIX))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
