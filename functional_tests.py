'''
To run functional tests:
python3 manage.py test functional_tests
'''

import sys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_view_home_page(self):
        # Come to check out portfolio home page
        self.browser.get(self.server_url)

        # see that the title mentiosn portfolio
        self.assertIn('Finders Keepers', self.browser.title)

        # And the basic elements are rendered
        self.browser.find_element_by_id('map')
        self.browser.find_element_by_id('message')
        self.browser.find_element_by_id('fusion_table')

    def test_layout_and_styling(self):
        self.browser.get(self.server_url)

        h1 = self.browser.find_element_by_tag_name('h1')

        self.assertEqual(h1.value_of_css_property(
            'color'), 'rgba(255, 255, 255, 1)')
