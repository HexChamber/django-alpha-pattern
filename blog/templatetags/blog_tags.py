from django import template
from django.utils.html import format_html
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
