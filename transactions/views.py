from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from transactions.forms import TransactionForm, TransactionUpdateForm
from transactions.models import Transaction


class TransactionListView(LoginRequiredMixin, ListView):
    template_name = 'transactions/list_of_transactions.html'
    model = Transaction
    context_object_name = 'all_transactions'


class TransactionCreateView(LoginRequiredMixin, CreateView):
    template_name = 'transactions/create_transaction.html'
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy('transactions')


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'transactions/update_transaction.html'
    model = Transaction
    form_class = TransactionUpdateForm
    success_url = reverse_lazy('list-of-transactions')


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'transactions/delete_transaction.html'
    model = Transaction
    success_url = reverse_lazy('list-of-transactions')
