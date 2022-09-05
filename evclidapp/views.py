from django.shortcuts import render

from evclidapp.forms import AppealForm
from evclidapp.models import Appeal, IndexPage


def get_index_content():
    content_page = IndexPage.objects.all()

    if content_page:
        content = {
            'title': content_page[0].title,
            'subtitle': content_page[0].subtitle,
            'about': content_page[0].about,
            'first_advantage_title': content_page[0].first_advantage_title,
            'first_advantage_text': content_page[0].first_advantage_text,
            'second_advantage_title': content_page[0].second_advantage_title,
            'second_advantage_text': content_page[0].second_advantage_text
        }
    else:
        content = {
            'title': 'Заголовок сайта',
            'subtitle': 'Подзаголовок сайта',
            'about': 'Раздел описания компании',
            'first_advantage_title': 'Заголовок первого приемущества',
            'first_advantage_text': 'Описание первого приемущества',
            'second_advantage_title': 'Заголовок второго приемущества',
            'second_advantage_text': 'Описание второго приемущества'
        }
    
    return content


def index(request):
    if request.method == 'POST':
        form = AppealForm(request.POST)
        if form.is_valid():
            print('Ok!')
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])
            try:
                Appeal.objects.create(
                    name=form.cleaned_data['name'],
                    e_mail=form.cleaned_data['email'],
                    text=form.cleaned_data['text']
                )
            except Exception:
                print('Ошибка в создании модели обращения')

            return render(request, 'thanks.html')
    else:
        form = AppealForm()
    
    content = get_index_content()

    context = {
        'form': form,
        'content': content
    }

    return render(request, 'index.html', context)


def thanks(request):
    return render(request, 'thanks.html')
