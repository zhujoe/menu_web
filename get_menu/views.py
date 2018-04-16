from django.shortcuts import render
import requests
from get_menu.models import cookbook
from bs4 import BeautifulSoup as bs
from django.utils import timezone
import time
from django.http import HttpResponse

# Create your views here.
def updatamenu_all():
    urllist = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    for num in range(15755, 200000):
        url = 'https://www.xinshipu.com/zuofa/'+str(num)
        urllist.append(url)

    num = 0
    for url in urllist:
        num+=1
        print(num)
        print(url)
        try:
            html = requests.get(url, timeout=120, headers=headers).content
        except:
            print('访问超时')
            continue
        data = bs(html, 'html5lib')
        try:
            name = data.find('h1', {'class': 'font18 no-overflow'}).text
            print(name)
            img_url = data.find('div', {'class': 'gallery'}).find('img')['src']
            # print(img_url)
            text_data = data.find('div', {'class': 'bpannel mt20 p15 re-steps'})#.find_all('p')
            makeings = ' '
            work = ' '
            knack = ' '
            family = ' '
            for i in text_data:
                try:
                    tit = i.find('div', {'class': 'dt cg2'}).text
                except:
                    # print('无标签')
                    continue
                if tit == '材料':
                    makeings = i.find('p').text
                    # print(makeings)
                elif tit == '做法':
                    work = ''
                    for x in i.find_all('p'):
                        work = work + str(x.text)
                    # print(work)
                elif tit == '小诀窍':
                    knack = ''
                    for x in i.find_all('p'):
                        knack = knack + str(x.text)
                    # print(knack)
                elif tit == '相关':
                    family = ''
                    for x in i.find_all('span', {'class': 'name'}):
                        family += x.text + ' '
                    # print(family)
                else:
                    continue
                # print('--------------------')
        except:
            print('网址无效！跳过！')
            continue
        sql = cookbook(name=name, img_url=img_url, makings=makeings, work=work, knack=knack, family=family,
                       pub_date=timezone.now())

        sql.save()
        time.sleep(1)
        print('#')


def index(request):
    updatamenu_all()
    return HttpResponse("完成！")


if __name__ == '__main__':
    updatamenu_all()
