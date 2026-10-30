from django.db import models
from django.utils import timezone

class StudentApplication(models.Model):
    STATUS_CHOICES = [
        ("received", "Received"),
        ("reviewing", "Under review"),
        ("contacted", "Contacted"),
        ("supported", "Support arranged"),
        ("closed", "Closed"),
    ]
    full_name = models.CharField(max_length=160)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=40)
    current_region = models.CharField(max_length=120)
    current_city = models.CharField(max_length=120, blank=True)
    preferred_safe_region = models.CharField(max_length=120, blank=True)
    school_or_university = models.CharField(max_length=180, blank=True)
    education_level = models.CharField(max_length=100)
    people_at_risk = models.PositiveSmallIntegerField(default=1)
    urgency = models.CharField(max_length=20, choices=[
        ("urgent", "Immediate danger"),
        ("high", "Urgent"),
        ("moderate", "Needs support soon"),
    ])
    situation = models.TextField()
    needs = models.TextField(blank=True, help_text="For example: safe accommodation, transport, school continuity.")
    safe_contact_method = models.CharField(max_length=100, blank=True)
    consent_to_contact = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="received")
    created_at = models.DateTimeField(default=timezone.now)
    staff_notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} | {self.get_status_display()}"

class SupportStory(models.Model):
    title = models.CharField(max_length=180)
    summary = models.CharField(max_length=280)
    story = models.TextField()
    region = models.CharField(max_length=100, blank=True)
    education_level = models.CharField(max_length=100, blank=True)
    support_needed = models.CharField(max_length=180, blank=True)
    contact_email = models.EmailField(blank=True, help_text="Organization-controlled contact only. Never publish a student's private email.")
    image = models.ImageField(upload_to="stories/", blank=True, null=True)
    is_published = models.BooleanField(default=False)
    consent_confirmed = models.BooleanField(default=False, help_text="Confirm the person gave informed consent to publish this story.")
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

class DonationRecord(models.Model):
    donor_name = models.CharField(max_length=120, blank=True)
    donor_email = models.EmailField(blank=True)
    amount_etb = models.DecimalField(max_digits=12, decimal_places=2)
    bank_or_channel = models.CharField(max_length=100)
    reference_number = models.CharField(max_length=120, blank=True)
    message = models.TextField(blank=True)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.amount_etb} ETB via {self.bank_or_channel}"
