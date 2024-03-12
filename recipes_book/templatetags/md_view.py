from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.filter(name='markdown')
def md_to_html(md_text: str):
    return mark_safe(markdown.markdown(md_text))


@register.filter(name='mark_safe')
def text_to_html(md_text: str):
    return mark_safe(md_text)
