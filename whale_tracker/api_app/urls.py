from django.urls import path
from .views import TransactionViews

urlpatterns = [
    # path('cart-items/', CartItemViews.as_view())
    path('transactions/', TransactionViews.as_view()),
    path('transactions/<int:id>', TransactionViews.as_view()),
]