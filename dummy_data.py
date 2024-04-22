from django.core.management.base import BaseCommand
from django.utils import timezone
from listings.models import Category, Post
import random

class Command(BaseCommand):
    help = 'Populates the database with placeholder data for categories and posts'

    def handle(self, *args, **kwargs):
        # Create 10 categories
        categories = []
        for i in range(10):
            category = Category.objects.create(
                name=f'Category {i+1}',
                description=f'Description for Category {i+1}',
                created_at=timezone.now(),
                updated_at=timezone.now()
            )
            categories.append(category)
        
        # Create 10 posts
        for i in range(10):
            Post.objects.create(
                title=f'Post Title {i+1}',
                content=f'This is post content for post {i+1}.',
                category=random.choice(categories),  # Randomly assign a category
                created_at=timezone.now(),
                updated_at=timezone.now()
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with placeholder data.'))
