from django import forms

class Currency1(forms.Form):
    name = forms.CharField(label='Desired Currency', max_length=100)

    def clean_renewal_date(self):
        data = self.cleaned_data['name']
        
        #Check that it has no spaces
        return data