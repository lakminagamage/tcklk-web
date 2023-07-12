from .forms import ContactForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PortfolioItems,TestimonialItems,ClientlogoItems
from django.shortcuts import get_object_or_404


def indexView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'The message has been sent successfully.')
            form = ContactForm()
    else:
        form = ContactForm()

    obj = PortfolioItems.objects.all()
    testimonial = TestimonialItems.objects.all()
    clientlogo = ClientlogoItems.objects.all()


    context = {
        'form': form,
        'obj': obj,
        'clientlogo': clientlogo,
        'testimonial': testimonial
    }
    return render(request, 'index.html', context)

def legalView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'The message has been sent successfully.')
            form = ContactForm()
    else:
        form = ContactForm()

    context = {
        'form': form}

    return render(request , 'website/legal.html', context)

def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'The message has been sent successfully.')
            form = ContactForm()
    else:
        form = ContactForm()

    context = {
        'form': form }

    return render(request, 'website/contacts.html', context)

def creativesView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'The message has been sent successfully.')
            form = ContactForm()
    else:
        form = ContactForm()

    obj = PortfolioItems.objects.all()
    testimonial = TestimonialItems.objects.all()
    clientlogo = ClientlogoItems.objects.all()

    context = {
        'form': form,
        'obj': obj,
        'clientlogo': clientlogo,
        'testimonial': testimonial
    }

    return render(request, 'website/creatives.html', context)

def solutionsView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'The message has been sent successfully.')
            form = ContactForm()
    else:
        form = ContactForm()

    obj = PortfolioItems.objects.all()
    testimonial = TestimonialItems.objects.all()
    clientlogo = ClientlogoItems.objects.all()

    context = {
        'form': form,
        'obj': obj,
        'clientlogo': clientlogo,
        'testimonial': testimonial
    }
    return render(request, 'website/solutions.html', context)

def estoreView(request):

    return render(request, 'website/estore.html', {})

def eventsView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'The message has been sent successfully.')
            form = ContactForm()
    else:
        form = ContactForm()

    context = {
        'form': form}

    return render(request, 'website/events.html', context)

def portfoliodetailsView(request):
    context ={}

    return render(request, 'website/portfolio-details.html', context)






