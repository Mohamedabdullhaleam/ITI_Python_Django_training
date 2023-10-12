from django import forms
from homepage.models import category,Course

# class CategoriesModelForm(forms.ModelForm):
#     class Meta:
#         model = category
#         fields = '__all__'
#
#
#     def clean_name(self):
#         name = self.cleaned_data['name']
#         if category.objects.filter(name=name).exists():
#             raise forms.ValidationError("This name already exists")
#         return name

class StudentForm(forms.Form):

    name = forms.CharField(label="Name")
    price = forms.IntegerField(label="price", required=False)
    image = forms.ImageField(label="Image", required=False)
    description = forms.CharField(label="desc")
    categ = forms.ModelChoiceField(queryset=category.objects.all(), label="Track", required=False)
    no_items = forms.IntegerField(label="no_items",required=False)
    # isvalid , validate --> expected result
    # validate inputs
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     # check if email exists in students --> data not valid
    #     if Student.objects.filter(email=email).exists():
    #         raise forms.ValidationError("Email already exists before")
