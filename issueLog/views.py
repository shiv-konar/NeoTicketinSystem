from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from .forms import IssueLogForm
# Create your views here.


def issuelog(request, ):
    form = IssueLogForm(request.POST or None)
    context = {
        "form":form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.issued_by = request.user
        instance.save()
    return render(request, "issuelog.html", context)