from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Song
from .forms import SongForm

#create
def song_create(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'song_form.html', {'form':form})

#read
def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song_list.html', {'songs':songs})

#update game details
def song_update(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST,instance=song)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm(instance=song)
    return render(request, 'song_form.html', {'form':form})

#delete game
def song_delete(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        song.delete()
        return redirect('song_list')
    return render(request, 'song_delete.html', {'song': song})
