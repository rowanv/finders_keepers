'''
To run unit tests:
python3 manage.py test location_finder
'''


from django.test import TestCase
from django.core.urlresolvers import resolve
from django.test.client import RequestFactory

import location_finder.views as views


class PageViewTest(TestCase):

    def test_index_url_resolves_to_index_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, views.index)

    def test_index_view_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

