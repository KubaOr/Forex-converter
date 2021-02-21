from app import app
from unittest import TestCase

app.config['TESTING'] = True


def test_main_form(self):
    with app.test_client() as client:
        res = client.get('/')
        html = res.get_data(as_text=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn('<form action="/result">', html)

# def test_convert_submit(self):
#     with app.test_client() as client:
#         res = client.get('/result', data=)
#         html = res.get_data(as_text=True)

#         self.assertEqual(res.status_code, 200)
#         self.assertIn(',  html)
