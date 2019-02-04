from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from bootstrap_datepicker_plus import DatePickerInput
from rfp_crud.models.rfp_model import Rfp

class RfpModelForm(forms.ModelForm):
    class Meta:
        model = Rfp
        fields = ['name', 'due_date', 'subject']
        widgets = {
            'due_date': DatePickerInput(format='%m/%d/%Y'),
            'subject': forms.Textarea
        }
        labels = {
            'name': 'Grants Title',
            'due_date': 'Grant Due Date',
            'subject': 'Description',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))