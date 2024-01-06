from django.test import TestCase
from myapp.models import models
# Create your tests here.
 # Thay yourapp và YourModel bằng tên thực của ứng dụng và model của bạn


class YourModelTestCase(TestCase):
    def test_syntax_errors(self):
        with self.assertRaises(SyntaxError):
            exec('def some_syntax_error()')

        with self.assertRaises(SyntaxError):
            exec('if true print("Hello")')

