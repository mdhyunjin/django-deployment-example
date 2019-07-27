from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    return value.replace(arg,'')

@register.filter(name='word_count')
def word_count(value):
    return len(value.split(' '))

#register.filter('cut',cut)
