from django.core.management.base import BaseCommand
from django.utils import timezone
from listings.models import Category, Post
import random

class Command(BaseCommand):
    help = 'Populates the database with placeholder data for categories and posts'

    def handle(self, *args, **kwargs):
        # Create 10 categories using get_or_create to avoid duplicates
        categories = []
        for i in range(10):
            category, created = Category.objects.get_or_create(
                name=f'Category {i+1}',
                defaults={
                    'description': f'Description for Category {i+1}.',
                    'created_at': timezone.now(),
                    'updated_at': timezone.now()}
            )
            categories.append(category)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {category.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Category already exists: {category.name}'))

        # Create 10 posts, each linked to a random category
        for i in range(10):
            post, created = Post.objects.get_or_create(
                title=f'Post Title {i+1}',
                defaults={
                    'content': f'This is post content for post {i+1}.',
                    'category': random.choice(categories),
                    'created_at': timezone.now(),
                    'updated_at': timezone.now()
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created post: {post.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Post already exists: {post.title}'))

        self.stdout.write(self.style.SUCCESS('Finished populating the database with placeholder data.'))

