from django import template

register = template.Library() # this code adds this tag to the library of tags in django

@register.filter
def only_active_comments(comments):
    return comments.filter(active=True) # we could use this too, comments.exclude(active=False)