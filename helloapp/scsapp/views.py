from django.shortcuts import render


def index(request):
	return render(request,"scsapp/index.html")
def about(request):
	return render(request,"scsapp/a.html")

