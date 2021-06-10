from django.shortcuts import render

from . import util


def index(request):
    print(f'this is the type of request: {type(request)}')
    print(f'this is the method of request: {dir(request)}')
    print(f'this is the full request: {request.read()}')
    print(f'this is the querydict of the request get: {print(request.META)}')
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_page(request, title):
    return render(request, "encyclopedia/entry_page.html", {"title":title, "content": util.get_entry(title)})