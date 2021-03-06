# -*- coding: utf-8 -*-
"""
Tests for `djangocms_page_tags` module.
"""
from __future__ import absolute_import, print_function, unicode_literals

from django.core.cache import cache
from djangocms_helper.base_test import BaseTestCase


class BaseTest(BaseTestCase):
    """
    Base class with utility function
    """
    _pages_data = (
        {'en': {'title': 'page one', 'template': 'page_tags.html', 'publish': True},
         'fr': {'title': 'page un', 'publish': True},
         'it': {'title': 'pagina uno', 'publish': True}},
        {'en': {'title': 'page two', 'template': 'page_tags.html', 'publish': True},
         'fr': {'title': 'page deux', 'publish': True},
         'it': {'title': 'pagina due', 'publish': True}},
    )

    def setUp(self):
        super(BaseTest, self).setUp()
        cache.clear()
