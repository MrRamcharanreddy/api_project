from django.test import TestCase, Client

class APITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_total_items(self):
        response = self.client.get('/api/total_items/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('total_items', data)

        # Add more assertions to validate the response data and behavior

    def test_nth_most_total_item(self):
        response = self.client.get('/api/nth_most_total_item/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('nth_most_total_item', data)

        # Add more assertions to validate the response data and behavior

    def test_percentage_of_department_wise_sold_items(self):
        response = self.client.get('/api/percentage_of_department_wise_sold_items/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('percentage_of_department_wise_sold_items', data)

        # Add more assertions to validate the response data and behavior

    def test_monthly_sales(self):
        response = self.client.get('/api/monthly_sales/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('monthly_sales', data)

        # Add more assertions to validate the response data and behavior
