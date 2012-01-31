from django import template

register = template.Library()

# Facebook

def fb_like_box(context, href):
    o = {'href': href}
    attrs = ['width', 'show_faces', 'stream', 'header', 'force_wall']
    for attr in attrs:
        if attr in context: o[attr] = context[attr]
    return o
    
register.inclusion_tag('sitewidgets/facebook/like_box.inc.html', 
        takes_context=True)(fb_like_box)

# Twitter

def twtr_profile(context, username):
    o = {'username': username}
    attrs = ['rpp', 'interval', 'width', 'height', 'shell_background',
             'shell_color', 'tweets_background', 'tweets_color', 
             'tweets_links', 'scrollbar', 'loop', 'live', 'hashtags', 
             'timestamp', 'avatars', 'behavior']
    for attr in attrs:
        if attr in context: o[attr] = context[attr]
    return o
    
register.inclusion_tag('sitewidgets/twitter/profile.inc.html', 
        takes_context=True)(twtr_profile)
