from django.test import TestCase

# Create your tests here.


class AddrViewTests(TestCase):

    def test_homepage_resp(self):

        resp = self.client.get('/')

        self.assertEqual(resp.status_code, 200)
        self.assertTrue('people' in resp.context)
        self.assertTrue('orgs' in resp.context)
