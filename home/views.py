import json

from django.shortcuts import render


def home(request):
    labels = ['Label 1', 'Label 2', 'Label 3']
    data = [30, 50, 20]

    context = {
        'labels': json.dumps(labels),
        'data': json.dumps(data),
    }

    return render(request, 'home/home.html', context)
