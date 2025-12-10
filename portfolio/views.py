from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')


def privacy(request):
    return render(request, 'privacy.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"

        # SEND EMAIL
        send_mail(
            subject="New Contact Message",
            message=full_message,
            from_email="ihsanshanu03@gmail.com",
            recipient_list=["ihsanshanu03@gmail.com"],
            fail_silently=False,
        )

        # SUCCESS MESSAGE
        messages.success(request, "Message sent successfully!")

        return redirect("contact")  # contact is the name in urls.py

    return render(request, "contact.html")
