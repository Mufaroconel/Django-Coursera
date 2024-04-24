from django.shortcuts import render

# Create your views here.
def about(request):
    about_content = {'about': "Little Lemon location 123 Main St, New York, NY 10001 phone 123-456-7890 email"}
    return render(request, 'about.html', about_content)