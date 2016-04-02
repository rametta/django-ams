from django.test import TestCase

class GalleryTest(TestCase):
    def test_index(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)

    def test_faq(self):
        r = self.client.get('/faq/')
        self.assertEqual(r.status_code, 200)