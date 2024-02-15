import os
import random
import json
import datetime
from faker import Faker

from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User

from blog.models import Post, Comment


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'alphasite.settings')
fake = Faker()



def user_generator(fake=fake, count=1, commit=False, json_file=None, password='password123', **kwargs):
    user_data = [
        {
            'username': fake.user_name(),
            'first_name': fake.first_name().capitalize(),
            'last_name': fake.last_name().capitalize(),
            'email': fake.email(),
        }
        for _ in range(count)
    ]

    for item in user_data:
        data = {**item, **kwargs}
        user = User(**data)
        user.set_password(password)
        if commit:
            user.save()

        if json_file:
            try:
                with open(json_file, 'w') as file:
                    file.write(json.dumps(data))
            except:
                pass
        yield user



def text_content(fake=fake, count=1, min_paragraphs=1, max_paragraphs=12, min_sentences=5, max_sentences=15, maximum_chars=10240):

    for _ in range(count):
        paragraphs = []
        paragraph_count = random.randint(min_paragraphs, max_paragraphs)
        for p in range(paragraph_count):
            sent_count = random.randint(min_sentences, max_sentences)
            paragraphs.append(f'\t{fake.paragraph(nb_sentences=sent_count)}')

        content = '\n'.join(paragraphs)
        if len(content) > maximum_chars:
            content = content[:maximum_chars]
        yield content







def post_generator(fake=fake, count=1, commit=False, json_file=None, author=None, **kwargs):
    post_data = [
        {
            'title': fake.bs().title(),
            'publish': fake.date_time_this_month(before_now=True),
            'author': author,
            'body': list(text_content(min_paragraphs=4))[0],
            'status': Post.Status.PUBLISHED
        }
        for _ in range(count)
    ]

    for item in post_data:
        data = {**item, **kwargs}
        post = Post(**data)

        post.author = fake.random_element(User.objects.all())
        post.slug = slugify(post.title)
        if commit:
            post.save()

        if json_file:
            try:
                with open(json_file, 'w') as file:
                    file.write(json.dumps(data))
            except:
                pass
        yield post



