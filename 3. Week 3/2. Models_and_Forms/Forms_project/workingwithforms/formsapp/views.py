from django.shortcuts import render
from django.http import HttpResponse
from .forms import ApplicationForm


# Create your views here.
def index(request):
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "form.html", context)