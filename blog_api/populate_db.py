import os
import django

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
    help = 'Creates application data'

    def handle(self, *args, **kwargs):
        self.create_blog_posts()
        self.create_comments()
        self.create_likes()
        self.create_profiles()
        print("Data population complete.")

    def create_blog_posts(self):
        blog_posts = [
            ("My First Blog Post", "This is my first blog post. I'm excited to share my thoughts with you."),
            ("Why I Love Coding", "Coding is my passion. I love solving problems and creating something from scratch."),
            ("My Favorite Programming Languages", "I love programming in Python, JavaScript, and HTML/CSS."),
            ("How to Learn Coding", "Learning to code can be challenging, but with persistence and dedication, anyone can do it."),
            ("My Coding Journey", "I've been coding for a few years now, and I'm excited to share my journey with you."),
            ("The Importance of Debugging", "Debugging is an essential part of coding. It helps you identify and fix errors."),
            ("My Favorite Coding Tools", "I love using Visual Studio Code, GitHub, and Stack Overflow."),
            ("How to Stay Motivated While Coding", "Staying motivated while coding can be challenging, but with the right mindset and strategies, you can overcome obstacles."),
            ("The Benefits of Coding", "Coding has many benefits, including improved problem-solving skills, creativity, and career opportunities."),
            ("My Favorite Coding Books", "I love reading 'Clean Code' by Robert C. Martin, 'The Pragmatic Programmer' by Andrew Hunt and David Thomas, and 'Code Complete' by Steve McConnell."),
            ("How to Learn New Programming Languages", "Learning new programming languages can be challenging, but with the right resources and strategies, you can overcome obstacles."),
            ("The Importance of Testing", "Testing is an essential part of coding. It helps you ensure that your code works as expected."),
            ("My Favorite Coding Communities", "I love participating in coding communities, including GitHub, Stack Overflow, and Reddit's r/learnprogramming."),
            ("How to Overcome Coding Challenges", "Overcoming coding challenges requires persistence, dedication, and the right mindset."),
        ]
        
        author = Profile.objects.get(id=1)
        for title, content in blog_posts:
            BlogPost.objects.create(title=title, content=content, author=author, status="P")
        print("Done with BlogPost")

    def create_comments(self):
        comments = [
            (1, 1, "This is a great blog post! I loved reading it."),
            (1, 2, "I agree with the author. Coding is an amazing skill to have."),
            (2, 1, "Thanks for sharing your favorite programming languages!"),
            (2, 3, "I'm a big fan of Python too! It's such a versatile language."),
            (3, 1, "Learning to code can be tough, but it's worth it in the end."),
            (3, 2, "I completely agree. Coding has opened up so many opportunities for me."),
            (4, 1, "Thanks"),
            (5, 1, "This is a great post! I loved reading it."),
        ]
        
        for post_id, user_id, content in comments:
            Comment.objects.create(post=BlogPost.objects.get(id=post_id), user=Profile.objects.get(id=user_id), content=content)
        print("Done with Comment")

    def create_likes(self):
        likes = [
            (1, 1, "L"), (1, 2, "L"), (2, 1, "L"), (3, 1, "D"),
            (4, 2, "L"), (5, 1, "L"), (6, 2, "D"), (7, 1, "L"),
        ]
        
        for post_id, user_id, like_type in likes:
            LikeDislike.objects.create(post=BlogPost.objects.get(id=post_id), user=Profile.objects.get(id=user_id), type=like_type)
        print("Done with Like")

    def create_profiles(self):
        profiles = [
            ("john_doe", "john.doe@example.com", "I'm a software developer with a passion for coding."),
            ("jane_smith", "jane.smith@example.com", "I'm a web developer with a love for designing user interfaces."),
            ("bob_johnson", "bob.johnson@example.com", "I'm a data scientist with a passion for machine learning."),
            ("alice_williams", "alice.williams@example.com", "I'm a cybersecurity expert with a focus on penetration testing."),
            ("mike_davis", "mike.davis@example.com", "I'm a DevOps engineer with a passion for automation and efficiency."),
            ("emily_chen", "emily.chen@example.com", "I'm a front-end developer with a love for designing responsive user interfaces."),
            ("david_lee", "david.lee@example.com", "I'm a back-end developer with a focus on building scalable APIs."),
            ("sophia_patel", "sophia.patel@example.com", "I'm a full-stack developer with a passion for building complex web applications."),
            ("kevin_white", "kevin.white@example.com", "I'm a technical writer with a focus on documenting software development processes."),
            ("olivia_martin", "olivia.martin@example.com", "I'm a UX designer with a passion for creating user-centered designs."),
        ]
        
        for username, email, bio in profiles:
            Profile.objects.create(username=username, email=email, bio=bio)
        print("Done with Profile")
