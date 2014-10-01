#-*- coding: utf-8 -*-
from django.template import Library
from django.core.signing import dumps
from django.utils.http import urlquote, urlunquote
from django.core.urlresolvers import reverse as url_reverse
from django import VERSION

DJANGO_VERSION = int("".join(map(str, VERSION[:3])))

register = Library()

@register.assignment_tag
def maskurl(given_url, *args, **kwargs):
    """
    Probable usage:
    - {% url 'main' %} ->
            {% maskurl 'main' %}
    - {% url 'list' 4 %} ->
            {% maskurl 'main' 4 %}
    - {% url 'list' 'blah' %} ->
            {% maskurl 'main' 'blah' %}
    - {% url 'list' object.id %} ->
            {% maskurl 'main' object.id %}
    - {% url 'list' obj1.id obj2.id %} ->
            {% maskurl 'main' obj1.id obj2.id %}
    - {% url 'list' obj1.name|title obj2.id|lower %} ->
            {% maskurl 'main' obj1.id|title obj2.id|lower %}
    - {{ reversed_url }} ->
            {% maskurl reversed_url %}

    After Django 1.7.0 version url built in
    templatetag returns quoted paths by default
    """

    maskedurl = ""
    match = given_url.find("/") == -1
    if match:
        reversed_url = url_reverse(given_url, args=args, kwargs=kwargs)
        resolved_url = urlunquote(reversed_url)
        maskedurl = dumps(resolved_url.lstrip('/'))
    else:
        maskedurl = dumps(url.lstrip('/'))

    if DJANGO_VERSION >= 170:
        maskedurl = urlquote(maskedurl)

    return '/%s' % maskedurl
