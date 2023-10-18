from typing import Any
from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404, reverse

from .models import Product, Comment
from .forms import CommentForm

class ProductListView(generic.ListView):
    model = Product
    queryset = Product.objects.filter(active=True)  # for not showing notactive products
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    
class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'  
    
    def get_context_data(self, **kwargs: Any):  # this function is for sending forms in detail view 
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
    
    
class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    
    def form_valid(self, form):
        obj = form.save(commit=False) # it means save the form and return me an object but does not save the form in database
        obj.author = self.request.user
        product_id = int(self.kwargs['pk'])
        product = get_object_or_404(Product, pk=product_id)
        obj.product = product
        return super().form_valid(form)
    
    # def get_success_url(self):
    #     return reverse('product_list')