from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from france_idee.models import Hopital,Scolaire, Agriculture
from.forms import hopitalForm, scolaireForm, agricultureForm
from django.http import HttpResponseRedirect

import pymongo
# Create your views here.



def home(request):
    return render(request , 'home.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        ConfirmPassword = request.POST.get('ConfirmPassword')

        user = User(email=email,username=username)
        user.set_password(password)
        user.save()
        return redirect('/')
    return render(request,'register.html')


def hopital_view(request):
    context = {'posts' : Hopital.objects.annotate(like_count=Count('likes')).order_by('-like_count')}
    return render(request , 'hopital.html' , context)


def scolaire_view(request):
    context = {'posts' : Scolaire.objects.annotate(like_count=Count('likes')).order_by('-like_count')}
    return render(request , 'scolaire.html' , context)


def agriculture_view(request):
    context = {'posts' : Agriculture.objects.annotate(like_count=Count('likes')).order_by('-like_count')}
    return render(request , 'agriculture.html' , context)

def ajouter_view(request):
    return render(request , 'ajouter.html')




def ajouter_scolaire_view(request, id=0):
    if request.user.is_authenticated:
        if request.method == "GET":
            if id == 0:
                form = scolaireForm()
            else:
                scolaire = Scolaire.objects.get(pk=id)
                form = scolaireForm(instance=scolaire)
            return render(request,"ajouter_scolaire_view.html",{'form':form})
        else:
            if id == 0:
                form= scolaireForm(request.POST)
            else:
                scolaire = Scolaire.objects.get(pk=id)
                form = scolaireForm(request.POST,instance=scolaire)
            if form.is_valid():
                toto = form.save(commit=False)
                toto.auteur = request.user
                toto.save()
            return redirect('/scolaire')
    else:
        return redirect('/')

def ajouter_agriculture_view(request, id=0):
    if request.user.is_authenticated:
        if request.method == "GET":
            if id == 0:
                form = agricultureForm()
            else:
                agriculture = Agriculture.objects.get(pk=id)
                form = agricultureForm(instance=agriculture)
            return render(request,"ajouter_agriculture_view.html",{'form':form})
        else:
            if id == 0:
                form= agricultureForm(request.POST)
            else:
                agriculture = Agriculture.objects.get(pk=id)
                form = agricultureForm(request.POST,instance=agriculture)
            if form.is_valid():
                toto = form.save(commit=False)
                toto.auteur = request.user
                toto.save()
            return redirect('/agriculture')
    else:
        return redirect('/')

def ajouter_hopital_view(request, id=0):
    if request.user.is_authenticated:
        if request.method == "GET":
            if id == 0:
                form = hopitalForm()
            else:
                hopital = Hopital.objects.get(pk=id)
                form = hopitalForm(instance=hopital)
            return render(request,"ajouter_hopital_view.html",{'form':form})
        else:
            if id == 0:
                form= hopitalForm(request.POST)
            else:
                hopital = Hopital.objects.get(pk=id)
                form = hopitalForm(request.POST,instance=hopital)
            if form.is_valid():
                toto = form.save(commit=False)
                toto.auteur = request.user
                toto.save()
            return redirect('/hopital')
    else:
        return redirect('/')


def hopital_delete(request,id):
    if request.user.is_authenticated:
        hopital = Hopital.objects.get(pk=id)
        hopital.delete()
        return redirect('/hopital')
    else:
        return redirect('/')

def scolaire_delete(request,id):
    if request.user.is_authenticated:
        scolaire = Scolaire.objects.get(pk=id)
        scolaire.delete()
        return redirect('/scolaire')
    else:
        return redirect('/')

def agriculture_delete(request,id):
    if request.user.is_authenticated:
        agriculture = Agriculture.objects.get(pk=id)
        agriculture.delete()
        return redirect('/agriculture')
    else:
        return redirect('/agriculture')

def like_viewH(request, pk):
    user = request.user
    post = get_object_or_404(Hopital, id=request.POST.get('post_id'))

    if user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('/hopital')

def like_viewS(request, pk):
    user = request.user
    post = get_object_or_404(Scolaire, id=request.POST.get('post_id'))

    if user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('/scolaire')

def like_viewA(request, pk):
    user = request.user
    post = get_object_or_404(Agriculture, id=request.POST.get('post_id'))

    if user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('/agriculture')