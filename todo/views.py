from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Todo
from .forms import ToDoForm
# Create your views here.
def todo_list(request):
	todos = Todo.objects.all()
	context = {
	'todo_list': todos
	}
	return render(request, 'todo/todo_list.html', context  )

def todo_detail(request, id):
	todo = Todo.objects.get(id=id)
	context = {
	'todo':todo
	}
	return render(request, 'todo/todo_detail.html' , context)

def todo_create(request):
	form = ToDoForm(request.POST or None)
	if form.is_valid():
		# print(form.cleaned_data)
		form.save()
		return redirect('/')
	context ={'form':form}
	return render(request, 'todo/todo_create.html' , context)

def todo_update(request , id):
	todo = Todo.objects.get(id=id)
	form = ToDoForm(request.POST or None , instance=todo)
	if form.is_valid():
		# print(form.cleaned_data)
		form.save()
		return redirect('/')
	context ={'form':form}
	return render(request, 'todo/todo_update.html' , context)

def todo_delete(request , id):
	#get the specific todo to delete
	todo = Todo.objects.get(id=id)
	todo.delete()

	return redirect('/')