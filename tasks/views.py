from django.shortcuts import render

# Create your views here.


def index(request):
    tasks = {"task1": "new tasks"}
    return render(request, "tasks/index.html", context=tasks)
