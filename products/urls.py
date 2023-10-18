from django.urls import path

from .views import ProductListView, ProductDetailView, CommentCreateView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('commnet/<int:pk>/', CommentCreateView.as_view(), name='comment_create'), # this url is sending the pk for the view
]