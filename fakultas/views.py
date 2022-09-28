from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def faperta(request):
    template = loader.get_template('faperta.html')
    return HttpResponse(template.render())
def feb(request):
    template = loader.get_template('feb.html')
    return HttpResponse(template.render())
def fh(request):
    template = loader.get_template('fh.html')
    return HttpResponse(template.render())
def fisip(request):
    template = loader.get_template('fisip.html')
    return HttpResponse(template.render())
def fk(request):
    template = loader.get_template('fk.html')
    return HttpResponse(template.render())
def fkip(request):
    template = loader.get_template('fkip.html')
    return HttpResponse(template.render())
def pascasarjana(request):
    template = loader.get_template('pascasarjana.html')
    return HttpResponse(template.render())
def visidanmisi(request):
    template = loader.get_template('visidanmisi.html')
    return HttpResponse(template.render())
    
