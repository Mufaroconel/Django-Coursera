# from django.shortcuts import render
# from django.http import HttpResponse

# from datetime import datetime
# Create your views here.

# def home(request):
#     return HttpResponse('Welcome to little lemon restaurant')
# def userlogin(request):
#     return HttpResponse("Welcome Login to continue.")
# def display_date(request):
#     date_joined = datetime.today().year
#     return HttpResponse(date_joined)
# def menu(request):
#     text = """<nav style='background-color: #f2f2f2; padding: 10px;'><ul style='list-style-type: none; margin: 0; padding: 0;'><li style='display: inline; margin-right: 20px;'><a href='#' style='text-decoration: none; color: #333;'>Home</a></li><li style='display: inline; margin-right: 20px;'><a href='#' style='text-decoration: none; color: #333;'>About</a></li><li style='display: inline; margin-right: 20px;'><a href='#' style='text-decoration: none; color: #333;'>Services</a></li><li style='display: inline;'><a href='#' style='text-decoration: none; color: #333;'>Contact</a></li></ul></nav>"""
#     return HttpResponse(text)

# 8. Creating_request_and_responses

# def home(request):
    
#     path = request.path
#     scheme = request.scheme
#     method = request.method
#     address = request.META['REMOTE_ADDR']
#     user_agent = request.META['HTTP_USER_AGENT']
#     path_info = request.path_info
#     # response.headers['Age'] = 20

#     msg = f"""<br>
#     <br>Path: {path}
#     <br>Address: {address}
#     <br>Scheme: {scheme}
#     <br>Method: {method}
#     <br>User_Agent: {user_agent}
#     <br>Path_Info: {path_info}

#     """

#     response = HttpResponse("This works")
    # return response
    # return HttpResponse(msg, content_type = 'text/html', charset='utf-8')
    # return HttpResponse(path, content_type = 'text/html', charset = 'utf-8')

# Mapping urls with params

# from django.shortcuts import render
# from django.http import HttpResponse

# # Your views here
# def menu_items(request, dish):
#     items = {'pasta': 'Delicious pasta dish', 
#              'falafel': 'Crispy falafel', 
#              'cheesecake': 'Creamy cheesecake'
#              }
#     description = items[dish]
#     return HttpResponse(f"<h1>{dish}</h1><p>{description}</p>")

# Regular Expressions


