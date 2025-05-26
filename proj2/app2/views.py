from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
# Create your views here.
def display_datetime(request, hours):
    curr = datetime.now()
    plus = curr + timedelta(hours = hours)
    minus = curr - timedelta(hours = -hours)
    return HttpResponse(f"<h1> Current Date & Time: {curr} </h1> <h2> Date & Time Ahead of {hours} hours: {plus}</h2> <h2> Date & Time Behind of {hours} hours: {minus}</h2>")