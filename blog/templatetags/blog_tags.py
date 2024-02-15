from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.db.models import Count

import markdown

from blog.models import Post



register = template.Library()


@register.filter(name='indented')
def indent_text(text, classes=''):
    classes = 'indented ' + classes
    text = text.replace('\t', f'<p class="{classes}">')
    text = text.replace('\n', '</p>')
    if not text.endswith('</p>'):
        text += '</p>'

    return format_html(text)


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
