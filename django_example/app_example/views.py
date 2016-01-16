from adminactionview.views import IntermediateAdminView

from .forms import AddAdminForm

# Create your views here.

class AddAdminView(IntermediateAdminView):
    Form = AddAdminForm
    template_name = 'app_example/add.html'
        
    short_description = "Add a number"
    action_name = "add_a_number"

    def actionOnEntry(self, entry, form):
        # Get the data from the form
        number_to_add = form.cleaned_data['number_to_add']
        # Do the updates to the entry
        entry.value = entry.value + number_to_add
        # Save the entry
        entry.save()
