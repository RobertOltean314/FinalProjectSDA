from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from transactions.forms import TransactionForm, TransactionUpdateForm, CategoryForm
from transactions.models import Transaction
from django.utils import timezone
from datetime import datetime


class TransactionListView(LoginRequiredMixin, ListView):
    template_name = 'transactions/list_of_transactions.html'
    model = Transaction
    form_class = TransactionForm
    context_object_name = 'all_transactions'


class TransactionCreateView(LoginRequiredMixin, CreateView):
    template_name = 'transactions/create_transaction.html'
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy('list-of-transactions')

    def get_initial(self):
        initial = super().get_initial()
        initial['month'] = datetime.now().month  # Set initial value for 'month' field
        return initial

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['category'] = CategoryForm(self.request.POST)
        else:
            data['category'] = CategoryForm()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        category = context['category']
        if category.is_valid():
            category = category.save(commit=False)
            category.user = self.request.user
            category.save()
            form.instance.category = category
        form.instance.month = form.cleaned_data['display_date'].month  # Extract month from display_date
        return super().form_valid(form)


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'transactions/update_transaction.html'
    model = Transaction
    form_class = TransactionUpdateForm
    success_url = reverse_lazy('list-of-transactions')


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'transactions/delete_transaction.html'
    model = Transaction
    success_url = reverse_lazy('list-of-transactions')
