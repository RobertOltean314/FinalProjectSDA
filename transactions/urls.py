from django.urls import path
from transactions import views

urlpatterns = [
    path('create_transaction/', views.TransactionCreateView.as_view(), name='create-transaction'),
    path('list_of_transactions/', views.TransactionListView.as_view(), name='list-of-transactions'),
    path('update_student/<int:pk>/', views.TransactionUpdateView.as_view(), name='update-student'),
    path('delete_student/<int:pk>/', views.TransactionDeleteView.as_view(), name='delete-student'),
]
