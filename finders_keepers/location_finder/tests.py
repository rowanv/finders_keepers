'''
To run unit tests:
python3 manage.py test location_finder
'''


from django.test import TestCase
from django.core.urlresolvers import resolve
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

import location_finder.views as views
import location_finder.models as models

class PageViewTest(TestCase):

    def test_index_url_resolves_to_index_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, views.index)

    def test_index_view_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

class ModelTest(TestCase):

    def test_can_create_location(self):
        location = models.Location(
            lat=40.7307,
            lon=-73.9946,
            address='Greenwich Village, New York, NY, USA')
        location.save()

    def test_cant_create_empty_location_address(self):
        location = models.Location(lat=40.7400, lon=-60.0000, address='')
        with self.assertRaises(ValidationError):
            location.save()
            location.full_clean()

    def test_cant_create_empty_location_lat_lon(self):
        location = models.Location(
            lat=None,
            lon=None,
            address='Greenwich Village, New York, NY, USA')
        with self.assertRaises(IntegrityError):
            location.save()
            location.full_clean()
