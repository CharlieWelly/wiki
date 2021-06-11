from enum import auto
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util
from . import forms


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def entry_page(request, title):
    return render(
        request,
        "encyclopedia/entry_page.html",
        {"title": title, "content": util.get_entry(title)},
    )


def search(request):
    query = request.GET["q"]
    q = query.lower()
    matched = []
    for entry in util.list_entries():
        if q in entry.lower() and q == entry.lower():
            return HttpResponseRedirect(
                reverse(
                    "entry_page",
                    args=(query,),
                )
            )
        elif q in entry.lower():
            matched.append(entry)
    return render(
        request, "encyclopedia/search_result.html", {"matched": matched, "query": query}
    )


def new_page(request):
    if request.method == "POST":
        form = forms.NewPage(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry_page", args=(title,)))
        else:
            return render(request, "encyclopedia/new_page.html", {"form": form})
    else:
        return render(request, "encyclopedia/new_page.html", {"form": forms.NewPage()})
