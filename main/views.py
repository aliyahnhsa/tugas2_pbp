from django.shortcuts import render, redirect 
from main.forms import GamesEntryForm
from main.models import GamesEntry
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    game_entries = GamesEntry.objects.all()

    context = {
        'appname': 'RandomGames Store App',
        'name': 'Aliyah Nahisa Sugiana',
        'class': 'PBP B',
        'game_entries': game_entries,
    }

    return render(request, "main.html", context)

def create_games_entry(request):
    form = GamesEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
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

