from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
# Create your views here.
def todo_list(request):
	return HttpResponse(Todo.get_all())