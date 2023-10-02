from django.shortcuts import render,redirect
from .models import Tabela, motivosArabia
# Create your views here.
def home(request):
  tabela= Tabela.objects.all()
  motivo = motivosArabia.objects.all()
  return render(request,"home.html", context={
    "tabela": tabela,
    "motivo": motivo,
  })

def create_motivo(request):
  if request.method=="POST":
    Tabela.objects.create(
      title=request.POST["title"],
      cor=request.POST["cor"],
      formacao=request.POST["formacao"],
      capitao=request.POST["capitao"]
    )
    return redirect("home")
  return render(request,"forms.html",context={"action":"Adicionar"})

def update_motivo(request,id):
  tabela = Tabela.objects.get(id=id)
  if request.method=="POST":
    tabela.title=request.POST["title"]
    tabela.cor=request.POST["cor"]
    tabela.formacao=request.POST["formacao"]
    tabela.capitao=request.POST["capitao"]
    tabela.save()
    return redirect("home")
  return render(request,"forms.html",context={"action":"Atualizar","tabela":tabela})

def delete_motivo(request,id):
  tabela = Tabela.objects.get(id=id)
  if request.method=="POST":
    if "confirm" in request.POST:
      tabela.delete()
    
    return redirect("home")
  return render(request,"areyousure.html",context={"tabela":tabela})
  