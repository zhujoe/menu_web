from django.shortcuts import render
from get_menu.models import cookbook
import random

# Create your views here.
def index(request):
    image_url_list = []
    name_list = []
    n = random.randint(1, 100)
    sqldata = cookbook.objects.order_by('id')[n:n+4]
    for cai in sqldata:
        name_list.append(cai.name)
        image_url_list.append('http:' + cai.img_url)
    content = {'name1': name_list[0],
               'name2': name_list[1],
               'name3': name_list[2],
               'name4': name_list[3],
               'image1': image_url_list[0],
               'image2': image_url_list[1],
               'image3': image_url_list[2],
               'image4': image_url_list[3]}
    # print(image_url_list)
    # print(name_list)
    return render(request, 'index.html', content)


def blog(request, name):
    sqldata = cookbook.objects.filter(name=name)
    content = {}
    for cai in sqldata:
        content = {'name': cai.name,
                   'image_url': 'http:' + str(cai.img_url),
                   'makings': cai.makings,
                   'work': cai.work,
                   'knack': cai.knack,
                   'family': cai.family}
    return render(request, 'blog.html', content)
