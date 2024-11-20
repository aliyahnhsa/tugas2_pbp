import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from main.forms import GameEntryForm
from main.models import GameEntry
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

@login_required(login_url='/login')
def show_main(request):

    context = {
        'appname': 'Randomgame Store App',
        'name': request.user.username,
        'class': 'PBP B',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

@csrf_exempt
@require_POST
def add_game_entry_ajax(request):
    game = strip_tags(request.POST.get("game"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    user = request.user

    new_game = GameEntry(
        game=game, price=price,
        description=description,
        user=user
    )
    new_game.save()

    return HttpResponse(b"CREATED", status=201)

def create_games_entry(request):
    form = GameEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        game_entry = form.save(commit=False)
        game_entry.user = request.user
        game_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_games_entry.html", context)

def show_xml(request):
    data = GameEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = GameEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = GameEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = GameEntry.objects.filter(pk=id)
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
      messages.error(request, "Invalid username or password. Please try again.")
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_game(request, id):
    # Get game entry berdasarkan id
    game = GameEntry.objects.get(pk = id)

    # Set game entry sebagai instance dari form
    form = GameEntryForm(request.POST or None, instance=game)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_game.html", context)

def delete_game(request, id):
    game = GameEntry.objects.get(pk = id)
    game.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
def create_mood_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_mood = GameEntry.objects.create(
            user=request.user,
            mood=data["mood"],
            mood_intensity=int(data["mood_intensity"]),
            feelings=data["feelings"]
        )

        new_mood.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)