import random
import re
from enum import auto

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from . import forms, util


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def entry_page(request, title):
    return render(
        request,
        "encyclopedia/entry_page.html",
        {"title": title, "content": util.to_html(util.get_entry(title))},
    )


def search(request):
    query = request.GET["q"]
    matched = []
    for entry in util.list_entries():
        if query.lower() == entry.lower():
            return HttpResponseRedirect(reverse("entry_page", args=(query,)))
        elif query.lower() in entry.lower():
            matched.append(entry)
    return render(
        request, "encyclopedia/search_result.html", {"matched": matched, "query": query}
    )


class NewPage(View):
    form_class = forms.NewPage
    template_name = "encyclopedia/new_page.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            content = "# " + title + "\n\n" + content
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry_page", args=(title,)))
        else:
            return render(request, self.template_name, {"form": form})


class EditPage(NewPage):
    form_class = forms.EditPage
    template_name = "encyclopedia/edit_page.html"

    def get(self, request, *args, **kwargs):
        title = request.GET.get("q")
        entry = util.get_entry(title)
        split_entry = re.split(r"[\r\n]+", entry, maxsplit=1)
        initial = {"title": title, "content": split_entry[-1]}
        form = self.form_class(initial=initial, auto_id=False)
        return render(request, self.template_name, {"form": form})


def random_page(request):
    title = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse("entry_page", args=(title,)))
