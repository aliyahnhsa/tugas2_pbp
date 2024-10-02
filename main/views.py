import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from main.forms import GamesEntryForm
from main.models import GamesEntry
from django.http import HttpResponse
from django.core import serializers

@login_required(login_url='/login')
def show_main(request):
    game_entries = GamesEntry.objects.filter(user=request.user)

    context = {
        'appname': 'RandomGames Store App',
        'name': request.user.username,
        'class': 'PBP B',
        'game_entries': game_entries,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_games_entry(request):
    form = GamesEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        game_entry = form.save(commit=False)
        game_entry.user = request.user
        game_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_games_entry.html", context)

def show_xml(request):
    data = GamesEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = GamesEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = GamesEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = GamesEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
      
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_game(request, id):
    # Get mood entry berdasarkan id
    game = GamesEntry.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = GamesEntryForm(request.POST or None, instance=game)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_game.html", context)

def delete_game(request, id):
    game = GamesEntry.objects.get(pk = id)
    game.delete()
    return HttpResponseRedirect(reverse('main:show_main'))