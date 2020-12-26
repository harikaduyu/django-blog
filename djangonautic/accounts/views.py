from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

import logging

logger = logging.getLogger(__name__)


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
