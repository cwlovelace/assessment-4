from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer

# APIViews for Category
class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save() # Establish category data for use in response
            return Response({
                "message": f"Category ID:  {category.id} / Category Name: {category.name} has been created.",
                "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Category, pk=pk)

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            updated_at = now() # Sets updated time to current time as of save
            return Response({
                "message": f"Category ID: {category.id} / Category Name: {category.name} has been updated at {updated_at}.",
                "data": serializer.data
                }, status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk) # establishes category data for use in response prior to deleton.
        category.delete()
        return Response(f"Category ID: {category.id} / Category Name: {category.name} has been deleted.")

# APIViews for Post
class PostList(APIView):
    def get(self, request, category_pk):
        posts = Post.objects.filter(category_id=category_pk)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, category_pk):
        category = get_object_or_404(Category, pk=category_pk) # Gets category and ensures it exists
        request.data['category'] = category_pk # takes category from URL parameter
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            return Response({
                "message": f"Post ID: {post.id} was created within {category.name} category (Category ID: {category.id}).",
                "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(APIView):
    def get_object(self, category_pk, pk):
        try:
            return Post.objects.get(pk=pk, category_id=category_pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, category_pk, pk):
        post = self.get_object(category_pk, pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, category_pk, pk):
        category=get_object_or_404(Category, pk=category_pk)
        post = self.get_object(category_pk, pk)
        # added line below to handle error: {"category":["This field is required."]}%. Since the request could contain the category, this ensures the category_pk lines up with the request.
        request.data['category'] = category_pk
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            post.category_id = category_pk
            serializer.save()
            updated_at = now()
            return Response({
                "message": f"Post ID {post.id} within {category.name} category has been updated at {updated_at}.",
                "data":serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_pk, pk):
        post = self.get_object(category_pk, pk)
        post_id = post.id
        category=get_object_or_404(Category, pk=category_pk)
        post.delete()
        return Response(f"Post {post_id} within {category.name} category has been deleted.")

