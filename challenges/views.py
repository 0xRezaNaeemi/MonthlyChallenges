from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

MONTHLY_CHALLENGES = {
    "january": "start HTML course!",
    "february": "start CSS course!",
    "march": "start JAVASCRIPT course!",
    "april": "start PYTHON course!",
    "may": "start DJANGO course!",
    "june": "start REST course!",
    "july": "start GIT course!",
    "august": "start API course!",
    "september": "start REACT course!",
    "october": "start VIUE course!",
    "november": "start ANGULAR course!",
    "december": "start FULLSTACK course!",
}


def index (request):
    list_items = ""
    months = list(MONTHLY_CHALLENGES.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data =f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(MONTHLY_CHALLENGES.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month!</h1>")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("monthly-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = MONTHLY_CHALLENGES[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound(f"<h1>On '{month}', there is not any challenges!</h1>")



    
