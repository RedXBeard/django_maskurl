#-*- coding: utf-8 -*-
from django.core.urlresolvers import resolve
from django.core.signing import dumps, loads
from django.utils.http import urlunquote


class MaskMiddleware(object):
    def process_response(self, response):
        # TODO: all href attributes or any other should
        #       be found in context and masked
        raise NotImplementedError

class UnMaskURLMiddleware(object):
    def process_request(self, request):
        """
        Url built in templatetag returns quoted url paths so as maskedurl
        after Django 1.7.0 then in any case unquotation operation must
        applied first otherwise real url path never be found
        then resolve operation to find the view and also given args
        after all result can be served.
        """
        unquoted_url = urlunquote(request.path.lstrip('/'))
        try:
            unmasked_url = '/%s' % loads(unquoted_url)
            # request url field should be kept as original
            # For some reasons; request url field can be used
            request.url = unmasked_url
            # Function will be called after resolved version of url is found.
            func, args, kwargs = resolve('/%s' % unmasked_url)
        except:
            # if there are pure urls then they all must be passed.
            func, args, kwargs = resolve('/%s' % unquoted_url)
        kwargs['request'] = request
        func(*args, **kwargs)
