from django.shortcuts import render
from .models import Treasure
# Create your views here.


def index(request):
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures': treasures})


# class Treasure:
#     def __init__(self, name, value, material, location):
#         self.name = name
#         self.value = value
#         self.material = material
#         self.location = location
#
#
# treasures = [
#     Treasure('Gold Nugget', 500.0, 'gold', "Curly's Creek, NM"),
#     Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO"),
#     Treasure('Coffee Can', 20.0, 'tin', 'Acme, CA'),
# ]
