# posts/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
from posts.models import Post
import random

User = get_user_model()

class Command(BaseCommand):
    help = "ایجاد داده‌های فیک برای کاربران و پست‌ها"

    def handle(self, *args, **kwargs):
        fake = Faker('fa_IR')  # فارسی سازی داده‌ها

        # ایجاد ۲ کاربر
        users = []
        for _ in range(2):
            user = User.objects.create_user(
                username=fake.unique.user_name(),
                email=fake.unique.email(),
                password='testpass123'
            )
            users.append(user)
            self.stdout.write(self.style.SUCCESS(f'کاربر {user.username} ایجاد شد'))

        # ایجاد ۱۰ پست تصادفی
        statuses = ['draft', 'published']
        for _ in range(10):
            Post.objects.create(
                author=random.choice(users),
                title=fake.sentence(nb_words=6),
                content=fake.paragraph(nb_sentences=10),
                status=random.choice(statuses)
            )
        self.stdout.write(self.style.SUCCESS('۱۰ پست با موفقیت ایجاد شدند'))