from django import template

register = template.Library()

@register.inclusion_tag('views/partials/form_input.html')
def form_input(elem, attrs=''):
    return {'elem':elem, 'attrs':attrs}
