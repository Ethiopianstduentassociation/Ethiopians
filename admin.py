from django.contrib import admin
from .models import StudentApplication, SupportStory, DonationRecord

@admin.register(StudentApplication)
class StudentApplicationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "current_region", "education_level", "urgency", "status", "created_at")
    list_filter = ("status", "urgency", "current_region", "created_at")
    search_fields = ("full_name", "phone", "email", "current_region", "school_or_university")
    readonly_fields = ("created_at",)
    fieldsets = (
        ("Student contact", {"fields": ("full_name", "age", "email", "phone", "safe_contact_method", "consent_to_contact")}),
        ("Education and location", {"fields": ("current_region", "current_city", "preferred_safe_region", "school_or_university", "education_level")}),
        ("Safety needs", {"fields": ("people_at_risk", "urgency", "situation", "needs")}),
        ("Review", {"fields": ("status", "staff_notes", "created_at")}),
    )

@admin.register(SupportStory)
class SupportStoryAdmin(admin.ModelAdmin):
    list_display = ("title", "region", "is_published", "consent_confirmed", "created_at")
    list_filter = ("is_published", "consent_confirmed", "region")
    search_fields = ("title", "summary", "story")
    list_editable = ("is_published", "consent_confirmed")
    readonly_fields = ("created_at",)
    fieldsets = (
        ("Public story", {"fields": ("title", "summary", "story", "region", "education_level", "support_needed", "image")}),
        ("Safe contact and consent", {"fields": ("contact_email", "consent_confirmed", "is_published")}),
        ("Metadata", {"fields": ("created_at",)}),
    )
    def save_model(self, request, obj, form, change):
        if not obj.consent_confirmed:
            obj.is_published = False
        super().save_model(request, obj, form, change)

@admin.register(DonationRecord)
class DonationRecordAdmin(admin.ModelAdmin):
    list_display = ("amount_etb", "bank_or_channel", "donor_name", "verified", "created_at")
    list_filter = ("verified", "bank_or_channel", "created_at")
    search_fields = ("donor_name", "donor_email", "reference_number")
    list_editable = ("verified",)
