from django.shortcuts import render
from django.http import HttpResponse
from formsapp.forms import ApplicationForm


# Create your views here.
def form_view(request):
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "form.html", context)