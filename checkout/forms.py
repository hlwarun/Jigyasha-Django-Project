from django import forms
from checkout.models import BillingAddress

class BillingDetailsForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['first_name', 'last_name', 'company_name', 'phone', 'email', 'country', 'province',
                  'district', 'city', 'address_line_01', 'address_line_02', 'zip_code', 'order_notes']

        PROVINCE_CHOICE = (
                                ('01', '01'),
                                ('02', '02'),
                                ('03', '03'),
                                ('04', '04'),
                                ('05', '05'),
                                ('06', '06'),
                                ('07', '07')
                          )

        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control', 'id':'first', 'placeholder':'First Name *'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control', 'id':'first', 'placeholder':'Last Name *'}),
            'company_name' : forms.TextInput(attrs={'class':'form-control', 'id':'company', 'placeholder':'Company Name'}),
            'phone' : forms.TextInput(attrs={'class':'form-control', 'id':'number', 'placeholder':'Phone Number *'}),
            'email' : forms.TextInput(attrs={'class':'form-control', 'id':'email', 'placeholder':'Email Address *'}),
            'country' : forms.Select(choices=(('Nepal', 'Nepal'),), attrs={'class':'country_select', 'placeholder':'Country *'}),
            'province' : forms.Select(choices=PROVINCE_CHOICE, attrs={'class':'country_select', 'placeholder':'Province *'}),
            'district' : forms.TextInput(attrs={'class':'form-control',  'id':'city', 'placeholder':'District *'}),
            'city' : forms.TextInput(attrs={'class':'form-control',  'id':'city', 'placeholder':'Town/City *'}),
            'address_line_01' : forms.TextInput(attrs={'class':'form-control', 'id':'add1', 'placeholder':'Address Line 01 *'}),
            'address_line_02' : forms.TextInput(attrs={'class':'form-control', 'id':'company', 'placeholder':'Address Line 02'}),
            'zip_code' : forms.TextInput(attrs={'class':'form-control', 'id':'zip', 'placeholder':'Zip/Post Code'}),
            'order_notes' : forms.Textarea(attrs={'class':'form-control', 'id':'message', 'rows':'1', 'placeholder':'Order Notes'}),
        }
