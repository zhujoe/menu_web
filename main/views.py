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


def recommend(request):
    data_lists = []
    for i in range(6):
        image_url_list = []
        name_list = []
        n = random.randint(1, 13375)
        sqldata = cookbook.objects.order_by('id')[n:n+4]
        for cai in sqldata:
            name_list.append(cai.name)
            image_url_list.append('http:' + cai.img_url)
        data_lists.append({'name1': name_list[0],
                           'name2': name_list[1],
                           'name3': name_list[2],
                           'name4': name_list[3],
                           'image1': image_url_list[0],
                           'image2': image_url_list[1],
                           'image3': image_url_list[2],
                           'image4': image_url_list[3],
                           'myid': 'demo' + str(n)})
    content = {'data_lists': data_lists}
    return render(request, 'recommend.html', content)


def search(request):
    content = {}
    if request.method == 'GET':
        content = {'holder': '输入关键字'}
        return render(request, 'search.html', content)
    elif request.method == 'POST':
        name = request.POST.get('name', None)
        if name == '':
            content = {'holder': '不能为空'}
            return render(request, 'search.html', content)
        # print('开始查询')
        sqldata = cookbook.objects.filter(name__contains=name)
        # print('查询结束')
        # print(sqldata)
        if len(sqldata) == 1:
            for cai in sqldata:
                content = {'name': cai.name,
                        'image_url': 'http:' + str(cai.img_url),
                        'makings': cai.makings,
                        'work': cai.work,
                        'knack': cai.knack,
                        'family': cai.family}
            return render(request, 'blog.html', content)

        elif len(sqldata) > 1:
            if len(sqldata) > 10:
                while 1:
                    a = random.randint(0, len(sqldata))
                    if a + 10 < len(sqldata):
                        break
                content = {'holder': '包含搜索词的内容如下',
                           'name_list': sqldata[a:a+10]}
            else:
                content = {'holder': '包含搜索词的内容如下',
                           'name_list': sqldata}
            return render(request, 'search.html', content)

        elif len(sqldata) == 0:
            content = {'holder': '未找到' + str(name)}
        return render(request, 'search.html', content)


def mail(request):
    return render(request, 'mail.html')
