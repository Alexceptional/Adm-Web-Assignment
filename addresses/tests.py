from django.test import TestCase


class AddrViewTests(TestCase):

    def test_homepage_resp(self):

        """
        Simple unit test for the homepage. The test checks that the view returns HTTP 200 and
         that the context data contains 'people' and 'orgs' keys.
        """

        resp = self.client.get('/')

        self.assertEqual(resp.status_code, 200)
        self.assertTrue('people' in resp.context)
        self.assertTrue('orgs' in resp.context)
