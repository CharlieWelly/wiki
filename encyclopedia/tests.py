from django.test import TestCase
from . import forms
from django.forms.fields import Field
from django.forms import widgets

# Create your tests here.


class TestForms(TestCase):
    def setUp(self):
        self.form = forms.EditPage(initial={"title": "Java", "content": "This is Java"})

    def test_field(self):
        for i in self.form.fields.values():
            with self.subTest(i=i):
                self.assertIsInstance(i, Field)
                self.assertEqual(i.label, "title")
