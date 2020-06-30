from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm
import requests
from bs4 import BeautifulSoup
import json

# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    for album in albums:
        if not album.colors:
            requestURL = 'https://api.blitline.com/job'
            imageURL = album.artworkURL
            result = requests.post(requestURL, json={
                "json":[
                    {
                        "application_id":"5-VpdA-OQSzTPND7mczLOAg",
                        "v": 1.23,
                        "src": imageURL,
                        "extract_colors": {
                            "max_colors": 6
                        },
                        "functions":[
                            {
                                "name": "no_op",
                                "params": {
                                }
                            }
                        ]
                    }
                ]
            })
            results = result.json()
            response = requests.get(f'https://cache.blitline.com/listen/{ results["results"][0]["job_id"]}')
            results = response.json()
            colors = results["results"]["original_meta"]["extracted_colors"]["data"]
            hexcolors = []
            for color in colors:
                hexcolors.append(color["color"]["hex_color"])
            album.colors = json.dumps(hexcolors)
            album.save()
    return render(request, "albums/list_albums.html", {"albums": albums})


def show_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "albums/show_album.html", {"album": album})


def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')
    return render(request, "albums/add_album.html", {"form": form})


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')
    return render(request, "albums/edit_album.html", {"form": form, "album": album})


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')
    return render(request, "albums/delete_album.html", {"album": album})