from django import template

register = template.Library()

def fb_like_box(context, href):
    attrs = ['width', 'show_faces', 'stream', 'header', 'force_wall']
    o = {'href': href}
    print context
    for attr in attrs:
        if attr in context: o[attr] = context[attr]
    print o
    return o
    
register.inclusion_tag('sitewidgets/facebook/like_box.inc.html', 
        takes_context=True)(fb_like_box)

