#-*- coding: utf-8 -*-
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/..')

from django.test import TestCase
from django.utils.http import urlunquote

from maskurl.templatetags.maskurl import maskurl
from django.core.signing import loads

class tagmaskurlTestCase(TestCase):
    def setUp(self):
        pass

    def test_maskurl(self):
        result = maskurl("/newones/?category=81")

class middlewareunmaskurlTestCase(TestCase):
    def setUp(self):
        pass

    def test_unmaskurl(self):
        quoted_url = "/Im5ld29uZXMvP2NhdGVnb3J5PTgxIg%3A1" + \
                     "XZ0wX%3AWt9m66_JAjW12unX9ggCIBK9eMg"
        unquoted_url = urlunquote(quoted_url.lstrip('/'))
        unmasked_url = '/%s' % loads(unquoted_url)
