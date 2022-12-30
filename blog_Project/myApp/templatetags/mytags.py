from django import template
from myApp.models import Post
from django.db.models import Count

register = template.Library() #default template tag = total_posts

@register.simple_tag # using register variable we are accessing simple_tag
def total_posts():
    return Post.objects.count() # return total no. of posts

@register.inclusion_tag('myApp/latest_post.html')
def show_latest_posts(count = 3):
    latest_posts = Post.objects.order_by('-publish')[:count] #collect the posts based on latest published date wrt specified count
    return {'latest_posts' : latest_posts}

@register.simple_tag
def get_most_commented_posts(count = 2):
    return Post.objects.annotate(total_comments = Count('comments')).order_by('-total_comments')[:count]