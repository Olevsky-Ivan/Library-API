from django.contrib import admin

from borrowing.models import Borrowing, Book, Payment

@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display = ("borrow_date", "expected_return_date", "actual_return_date", "book", "user")
    search_fields = ("borrow_date", "book__title", "user__username")
    list_filter = ("borrow_date", "book", "user")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "cover", "inventory", "daily_fee")
    search_fields = ("title", "author__name", "cover")
    list_filter = ("author",)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("status", "type", "borrowing", "session_url", "session_id", "money_to_pay")
    search_fields = ("type", "borrowing__book__title")
    list_filter = ("status", "type")

