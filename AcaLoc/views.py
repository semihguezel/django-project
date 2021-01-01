from django.shortcuts import render
from AcaLoc.models import Academican, Department

Aca = [
    {
        'academician': 'Berk Anbaroğlu',
        'department': 'Geomatic',
        'location': 'Latitude: 39.865756847488434  Longitude: 32.733861598331'
    },
    {
        'academician': 'Berk Hacıyatmazoğlu',
        'department': 'Computer Science',
        'location': 'Latitude: 39.865756847488120  Longitude: 32.733861598111'

    }
]


def home(request):
    context = {
        'Acas': Aca
    }
    return render(request, 'AcaLoc/home.html', context)


def about(request):
    return render(request, 'AcaLoc/about.html', {'title': 'Malumço'})

def deneme(request,*args,**kwargs):
    obj = Academican.objects.all()
    context = {
        "object": obj,
    }
    return render(request,'AcaLoc/deneme.html',context)
