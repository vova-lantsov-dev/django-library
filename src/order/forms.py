from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "email", "phone"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "phone": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            )
        }

    def save(self, book):
        book.left -= 1
        book.save()
        customer = Customer(
            name=self.cleaned_data["name"],
            email=self.cleaned_data["email"],
            phone=self.cleaned_data["phone"],
            book=book
        ).save()
        return customer
