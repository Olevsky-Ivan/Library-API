from django.db import models
from decimal import Decimal
from django.conf import settings

class Book(models.Model):

    class CoverType(models.TextChoices):
        HARD = "HARD", "Hardcover"
        SOFT = "SOFT", "Softcover"


    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    cover = models.CharField(max_length=4, choices=CoverType.choices)
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal("0.00"))

    def __str__(self):
        return self.title


class Borrowing(models.Model):
    borrow_date = models.DateField(null=False)
    expected_return_date = models.DateField(null=False)
    actual_return_date = models.DateField(null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"User {self.user.id} borrowed {self.book.title}"


class Payment(models.Model):
    class PaymentStatus(models.TextChoices):
        PENDING = "PD", "Pending"
        PAID = "PA", "Paid"

    class PaymentType(models.TextChoices):
        PAYMENT = "PAY", "Payment"
        FINE = "FINE", "Fine"

    status = models.CharField(max_length=4, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    type = models.CharField(max_length=4, choices=PaymentType.choices)
    borrowing = models.ForeignKey(Borrowing, on_delete=models.CASCADE)
    session_url = models.URLField()
    session_id = models.CharField(max_length=255, unique=True)
    money_to_pay = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))

    def __str__(self):
        return f"Payment {self.id}: {self.get_type_display()} - {self.get_status_display()}"
