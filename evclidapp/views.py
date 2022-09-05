from django.shortcuts import render

from evclidapp.forms import AppealForm
from evclidapp.models import Appeal


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

    context = {
        'form': form
    }

    return render(request, 'index.html', context)


def thanks(request):
    return render(request, 'thanks.html')
