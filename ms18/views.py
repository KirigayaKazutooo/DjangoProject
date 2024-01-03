from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Product



def home(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'ms18/home.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'ms18/home.html' # ms18/product_list.html
    context_object_name = 'products'
    ordering = ['-date_posted']
    

class ProductDetailView(DetailView):
    model = Product
    

class ProductCreateView(LoginRequiredMixin ,CreateView):
    model = Product
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin ,CreateView):
    model = Product
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'ms18/about.html', {'title': 'About'})