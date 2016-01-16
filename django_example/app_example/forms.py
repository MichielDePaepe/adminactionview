from django import forms
from adminactionview.forms import IntermediateAdminForm

class AddAdminForm(IntermediateAdminForm):
    number_to_add = forms.IntegerField()
