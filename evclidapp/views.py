from django.shortcuts import render

from evclidapp.forms import AppealForm


def index(request):
    if request.method == 'POST':
        form = AppealForm(request.POST)
        if form.is_valid():
            print('Ok!')
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])
    else:
        form = AppealForm()

    context = {
        'form': form
    }

    return render(request, 'index.html', context)
