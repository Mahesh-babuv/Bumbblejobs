from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages


def homepage(request):
    return render (request,"home.html")

def alljobs(request):
    return render (request,"jobs.html")

def thankyou(request):
    return render(request, 'thankyou.html')

def about(request):
    return render(request, 'about.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')

def applynow(request):
    if request.method == 'POST':
        # Process form data (this can be extended for a real form)
        messages.success(request, "Application submitted successfully.")
        return redirect('thankyou')  # Redirect to a thank-you page
    return render(request, 'applynow.html')