'''
To run unit tests:
python3 manage.py test location_finder
'''

import json

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

import location_finder.views as views
from location_finder.models import Location


class PageViewTest(TestCase):

    def test_index_url_resolves_to_index_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, views.index)

    def test_index_view_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    '''
    def test_edit_location_resolves(self):
        json_data = json.dumps(
            {'lat':40.7307,
            'lon':-73.9946,
            'address': 'Greenwich Village, New York, NY, USA'})
        response = self.client.post(
            '/content/edit_location/',
            str(json_data),
            content_type='application/json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
            )
        self.assertEqual(response.status_code, 200)

    def test_edit_location_view_adds_location(self):
        self.assertEqual(len(Location.objects.all()), 0)
        json_data = json.dumps(
            {'lat':40.7307,
            'lon':-73.9946,
            'address': 'Greenwich Village, New York, NY, USA'})
        response = self.client.post(
            '/content/edit_location/',
            json_data,
            content_type='application/json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
            )
        self.assertEqual(len(Location.objects.all()), 1)
        first_location = Location.objects.all()[0]
        self.assertEqual(first_location.lat, 40.7307)
        self.assertEqual(first_location.address[:5], 'Green')
    '''
    def test_can_delete_all_saved_locations(self):
        self.assertEqual(len(Location.objects.all()), 0)
        loc_1 = Location(
            lat=40.7307,
            lon=-73.9946,
            address='Greenwich Village, New York, NY, USA')
        loc_1.save()
        loc_2 = Location(
            lat=40.7307,
            lon=-73.9946,
            address='Greenwich Village, New York, NY, USA')
        loc_2.save()
        self.assertEqual(len(Location.objects.all()), 2)

        response = self.client.post(
            '/content/delete_all_locations/')
        self.assertEqual(len(Location.objects.all()), 0)


class ModelTest(TestCase):

    def test_can_create_location(self):
        location = Location(
            lat=40.7307,
            lon=-73.9946,
            address='Greenwich Village, New York, NY, USA')
        location.save()

    def test_cant_create_empty_location_address(self):
        location = Location(lat=40.7400, lon=-60.0000, address='')
        with self.assertRaises(ValidationError):
            location.save()
            location.full_clean()

    def test_cant_create_empty_location_lat_lon(self):
        location = Location(
            lat=None,
            lon=None,
            address='Greenwich Village, New York, NY, USA')
        with self.assertRaises(IntegrityError):
            location.save()
            location.full_clean()
