import os
import django
import random

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

# Initialize Django
django.setup()

from django.core.management.base import BaseCommand
from accounts.models import Profile
from blog.models import BlogPost
from likes.models import LikeDislike
from comments.models import Comment

class Command(BaseCommand):
    help = 'Creates a large dataset for the application'

    def handle(self, *args, **kwargs):
        self.create_profiles()
        self.create_blog_posts()
        self.create_comments()
        self.create_likes()
        print("Data population complete.")

    def create_profiles(self):
        profiles = []
        for i in range(1, 31):  # Creating 100 profiles
            profiles.append(Profile(username=f'user_{i}', email=f'user_{i}@example.com', bio=f'This is bio for user_{i}'))
        Profile.objects.bulk_create(profiles)
        print("Done with Profile")

    def create_blog_posts(self):
        authors = list(Profile.objects.all())
        blog_posts = []
        for i in range(1, 31):  # Creating 500 blog posts
            author = random.choice(authors)
            blog_posts.append(BlogPost(title=f'Blog Post {i}', content=f'This is the content of blog post {i}', author=author, status="P"))
        BlogPost.objects.bulk_create(blog_posts)
        print("Done with BlogPost")

    def create_comments(self):
        posts = list(BlogPost.objects.all())
        users = list(Profile.objects.all())
        comments = []
        for i in range(1, 21):  # Creating 2000 comments
            post = random.choice(posts)
            user = random.choice(users)
            comments.append(Comment(post=post, user=user, content=f'This is comment {i}'))
        Comment.objects.bulk_create(comments)
        print("Done with Comment")

    def create_likes(self):
        posts = list(BlogPost.objects.all())
        users = list(Profile.objects.all())
        likes = []
        for i in range(1, 31):  # Creating 3000 likes/dislikes
            post = random.choice(posts)
            user = random.choice(users)
            like_type = random.choice(["L", "D"])
            likes.append(LikeDislike(post=post, user=user, type=like_type))
        LikeDislike.objects.bulk_create(likes)
        print("Done with Like")