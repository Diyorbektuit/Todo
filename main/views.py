from django.shortcuts import render, redirect
from django.views import View
from .models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        todos = Todo.objects.filter(user=request.user).order_by("-datetime")
        return render(request, "index.html", {"todos":todos})
    
    def post(self, request):
        body = request.POST.get("body")
        if body:
            Todo.objects.create(user=request.user, body=body)
        
        return redirect("index")
    

class TodoActionView(LoginRequiredMixin, View):
    def post(self, request, todo_id, action):
        todo = Todo.objects.filter(id=todo_id, user=request.user).first()
        if todo:
            if action == "done":
                todo.done = True
                todo.save()
            elif action == "delete":
                todo.delete()
                
        return redirect("index")