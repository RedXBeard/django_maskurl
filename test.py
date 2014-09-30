#-*- coding: utf-8 -*-
import django
from django.conf import settings
from django.test.simple import DjangoTestSuiteRunner

class Testing(object):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }

    MIDDLEWARE_CLASSES = (
        'middleware.UnMaskURLMiddleware',
    )

    INSTALLED_APPS = (
        'maskurl',
    )

    TEST_RUNNER = 'django.test.runner.DiscoverRunner'

    settings.configure(
        DEBUG=True,
        DATABASES=DATABASES,
        MIDDLEWARE_CLASSES=MIDDLEWARE_CLASSES,
        TEST_RUNNER=TEST_RUNNER,
        INSTALLED_APPS=INSTALLED_APPS,
    )

    def __init__(self):
        django.setup()
        self.run_test()

    def run_test(self):
        test_runner = DjangoTestSuiteRunner(verbosity=1)
        failures = test_runner.run_tests(settings.INSTALLED_APPS)
        if failures:
            sys.exit(failures)


if __name__ == '__main__':
    Testing()
