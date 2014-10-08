django_maskurl
==============
[![Build Status](https://travis-ci.org/RedXBeard/django_maskurl.svg?branch=master)](https://travis-ci.org/RedXBeard/django_maskurl) 
[![Downloads](https://pypip.in/download/django-maskurl/badge.svg?period=day)](https://pypi.python.org/pypi/django-maskurl/)
[![Latest Version](https://pypip.in/version/django-maskurl/badge.svg)](https://pypi.python.org/pypi/django-maskurl/)
[![Supported Python versions](https://pypip.in/py_versions/django-maskurl/badge.svg)](https://pypi.python.org/pypi/django-maskurl/)
[![License](https://pypip.in/license/django-maskurl/badge.svg)](https://pypi.python.org/pypi/django-maskurl/)


Masking url's on templates not to show exact path, hiding them all except get params.

Installing
----------
```
pip install django-maskurl
```
Then add <code>maskurl.middleware.UnMaskURLMiddleware</code> to the end of your <code>MIDDLEWARE_CLASSES</code>.

```
MIDDLEWARE_CLASSES = (
    'dikeyshop.syncer.middlewares.SyncerMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    ...
    'maskurl.middleware.UnMaskURLMiddleware',
  )
```

Usage
-----
To mask a url on a template simply at the top, before all html codes <code>{% load maskurl %}</code> line must be placed, as following;

```
{% load maskurl %}
  <title>...
...
```

Then requested urls on that html file should be one of the following formats;
```
- {% url 'main' %}
- {% url 'list' 4 %}  
- {% url 'list' 'blah' %}
- {% url 'list' object.id %}  
- {% url 'list' obj1.id obj2.id %}  
- {% url 'list' obj1.name|title obj2.id|lower %}
- {{ reversed_url }}
```

Those can be converted as following;
```
- {% maskurl 'main' %}
- {% maskurl 'main' 4 %}
- {% maskurl 'main' 'blah' %}
- {% maskurl 'main' object.id %}
- {% maskurl 'main' obj1.id obj2.id %}
- {% maskurl 'main' obj1.id|title obj2.id|lower %}
- {% maskurl reversed_url %}
```

get params can also be added after the closing curly bracket.
