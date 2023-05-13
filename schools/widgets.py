from datetime import date
from django import forms


class CustomDateInput(forms.DateInput):
    DATE_INPUT_WIDGET_REQUIRED_FORMAT = "%y-%m-%d"

    def __init__(self, attrs=None, format=None):
        attrs = attrs or {}
        attrs.update({'class': 'datepicker', "type": "date"})
        self.format = format or self.DATE_INPUT_WIDGET_REQUIRED_FORMAT
        super().__init__(attrs, format=self.format)


class PastDateField(CustomDateInput):
    def __init__(self, attrs=None, format=None):
        attrs = attrs or {}
        attrs.update({'max': date.today()})
        super().__init__(attrs, format=format)
