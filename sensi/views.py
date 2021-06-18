from django.shortcuts import render
from django import forms

class SensiForm(forms.Form):
    sensi1 = forms.IntegerField(label="Valorant Sensitivity")


def index(request):
    if request.method == "POST":
        s1 = request.POST.get("sensi1")
        s2 = int(s1)* 3.1818
        sform = SensiForm(request.POST)
        return render(request,"sensi/index.html",{
            "form": sform,
            "s2" : s2
        })
    return render(request, "sensi/index.html",{
        "form": SensiForm()
    })