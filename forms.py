from django import forms
from .models import StudentApplication, DonationRecord

class StyledFormMixin:
    def style_fields(self):
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs.setdefault("rows", 4)
        return self

class StudentApplicationForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = [
            "full_name", "age", "email", "phone", "current_region", "current_city",
            "preferred_safe_region", "school_or_university", "education_level",
            "people_at_risk", "urgency", "situation", "needs", "safe_contact_method",
            "consent_to_contact",
        ]
        widgets = {
            "consent_to_contact": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "situation": forms.Textarea(attrs={"placeholder": "Tell us what is happening and why relocation or support is needed."}),
            "needs": forms.Textarea(attrs={"placeholder": "Share only what feels safe to share."}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.style_fields()
        self.fields["full_name"].label = "Your name"
        self.fields["situation"].label = "Your situation"
        self.fields["consent_to_contact"].label = "It is safe for the association to contact me using the method I selected."
        self.fields["consent_to_contact"].required = True

class DonationForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = DonationRecord
        fields = ["donor_name", "donor_email", "amount_etb", "bank_or_channel", "reference_number", "message"]
        widgets = {"message": forms.Textarea(attrs={"rows": 3, "placeholder": "Optional message"})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.style_fields()
        self.fields["amount_etb"].label = "Donation amount (ETB)"
        self.fields["bank_or_channel"].label = "Bank or payment channel used"
