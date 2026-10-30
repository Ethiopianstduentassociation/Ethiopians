from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .forms import StudentApplicationForm, DonationForm
from .models import SupportStory

def home(request):
    stories = SupportStory.objects.filter(is_published=True, consent_confirmed=True)[:3]
    return render(request, "association/home.html", {"stories": stories})

@require_http_methods(["GET", "POST"])
def apply(request):
    if request.method == "POST":
        form = StudentApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            # Optional notification; configure email settings before enabling in production.
            if getattr(settings, "EMAIL_HOST", ""):
                try:
                    send_mail(
                        "New student support application",
                        f"Application {application.pk} received. Please review it securely in the admin.",
                        getattr(settings, "DEFAULT_FROM_EMAIL", "noreply@example.org"),
                        [getattr(settings, "ASSOCIATION_ALERT_EMAIL", "admin@example.org")],
                        fail_silently=True,
                    )
                except Exception:
                    pass
            return redirect("application_received")
    else:
        form = StudentApplicationForm()
    return render(request, "association/apply.html", {"form": form})

def application_received(request):
    return render(request, "association/application_received.html")

def stories(request):
    entries = SupportStory.objects.filter(is_published=True, consent_confirmed=True)
    return render(request, "association/stories.html", {"stories": entries})

def story_detail(request, pk):
    story = get_object_or_404(SupportStory, pk=pk, is_published=True, consent_confirmed=True)
    return render(request, "association/story_detail.html", {"story": story})

@require_http_methods(["GET", "POST"])
def donate(request):
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for recording your donation. The association will verify the transfer before marking it as confirmed.")
            return redirect("donate")
    else:
        form = DonationForm()
    return render(request, "association/donate.html", {"form": form})
