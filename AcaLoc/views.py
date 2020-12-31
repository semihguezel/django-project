from django.shortcuts import render

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
