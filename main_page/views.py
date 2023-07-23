from django.shortcuts import render
from . import models

def main_page(request):
    logo = models.Logo.objects.all()
    about_me = models.AboutME.objects.all()
    about_me_photo = models.AboutMEPhoto.objects.all()
    sliders = models.Slider.objects.all()
    target = models.Target.objects.all()
    contact = models.Contact.objects.all()
    context = {
        'logo': logo,
        'slider': sliders,
        'about': about_me,
        'about_photo': about_me_photo,
        'target': target,
        'contact': contact,
    }
    return render(request, 'index.html', context)
