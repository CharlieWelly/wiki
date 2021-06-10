from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util
import re

def index(request):
    try:
        query = request.GET['q']
    except KeyError:
        return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})
    else:
        matched = []
        q = query.lower()
        for entry in util.list_entries():
            if q in entry.lower() and q == entry.lower():
                return HttpResponseRedirect(reverse("encyclopedia:entry_page", args={"title": entry, "content": util.get_entry(entry)}))
            elif q in entry.lower():
                matched.append(entry)
        return render(request, "encyclopedia/search_result.html", {"matched": matched, "query": query})


def entry_page(request, title):
    return render(request, "encyclopedia/entry_page.html", {"title":title, "content": util.get_entry(title)})

