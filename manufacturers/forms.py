from django import forms
from .models import UtilityConsumption

class UtilityConsumptionForm(forms.ModelForm):
    class Meta:
        model = UtilityConsumption
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, (forms.CheckboxInput, forms.RadioSelect, forms.FileInput)):
                field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        utility_type = cleaned_data.get('utility_type') 
        other_name = cleaned_data.get('other_utility_name')

        for field_name in ['quantity_used', 'value_ksh', 'max_capacity_required']:
            value = cleaned_data.get(field_name)

            if value is not None and value <= 0:
                self.add_error(field_name, f"{field_name} must be greater than 0")

        if utility_type == 'other' and not other_name:
            self.add_error('other_utility_name', 'please specify the utility name.')

        return cleaned_data

    
