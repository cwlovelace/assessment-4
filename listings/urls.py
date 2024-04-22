from django.urls import path
from .views import CategoryList, CategoryDetail, PostList, PostDetail

# URL Patterns to establish nested routes categories>c_id>posts>p_id
urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('categories/<int:category_pk>/posts/', PostList.as_view(), name='post-list'),
    path('categories/<int:category_pk>/posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
]

