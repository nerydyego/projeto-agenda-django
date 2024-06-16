from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.http import Http404

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[0:10]
    
    context = {
        'contacts': contacts,
        'site_title': 'Contatos - ',
    }
    return render(
        request,
        'contact/index.html',
        context
        )

def search(request):
    search_value = request.GET.get('q', '').strip()
    
    if search_value == '':
        return redirect('contact:index')
    # https://docs.djangoproject.com/en/5.0/ref/models/lookups/
    contacts = Contact.objects\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value)
            )\
        .order_by('-id')
    
    context = {
        'contacts': contacts,
        'site_title': 'Search - ',
    }
    return render(
        request,
        'contact/index.html',
        context
        )

def contact(request, contact_id):
    
    single_contact = get_object_or_404(
        Contact.objects.filter(pk=contact_id, show=True)
    )

    site_title = f'{single_contact.first_name} {single_contact.last_name}'
    # sigle_contact = Contact.objects.filter(pk=contact_id).first()
    
    # if sigle_contact is None:
    #     raise Http404()
    context = {
        'contact': single_contact,
        'site_title': site_title,
    }
    return render(
        request,
        'contact/contact.html',
        context
        )
