from django import forms


class FormByPk(forms.Form):
    id = forms.IntegerField(min_value=1, label='Contract id')
