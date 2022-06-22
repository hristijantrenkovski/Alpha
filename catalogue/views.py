from typing import List
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from .forms import CreateUserForm, RateForm
from .models import Album, Artist, Language, Genre, Band, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .decorators import unauthenticated_user

# Create your views here.
@unauthenticated_user
def homePage(request):
    return render(request, 'home.html')

def index(request):
    num_of_albums = Album.objects.all().count()
    num_of_artists = Artist.objects.all().count()

    context = {
        'num_of_albums':num_of_albums,
        'num_of_artists':num_of_artists,
    }

    return render(request,'catalogue/index.html',context=context)


class ArtistCreate(CreateView):
    model = Artist
    fields = '__all__'

class BandCreate(LoginRequiredMixin,CreateView):
    model = Band
    fields = '__all__'

class GenreCreate(LoginRequiredMixin,CreateView):
    model = Genre
    fields = '__all__'

class AlbumCreateArtist(LoginRequiredMixin,CreateView):
    model = Album
    template_name = 'catalogue/album_form_artist.html'
    fields = ['name','author','genre','release_date','language','num_of_songs','price','image']

class AlbumCreateBand(LoginRequiredMixin,CreateView):
    model = Album
    template_name = 'catalogue/album_form_band.html'
    fields = ['name','band','genre','release_date','language','num_of_songs','price','image']

class AlbumListView(ListView):
    model = Album
    queryset = Album.objects.order_by('name')
    context_object_name = 'album_list'

class BandListView(ListView):
    model = Band
    queryset = Band.objects.order_by('name')
    context_object_name = 'band_list'

class ArtistListView(ListView):
    model = Artist
    queryset = Artist.objects.order_by('first_name')
    context_object_name = 'artist_list'

class AlbumDetail(DetailView):
    model = Album

class BandDetail(DetailView):
    model = Band

class ArtistDetail(DetailView):
    model = Artist


@login_required(login_url='login')
def my_view(request):
    return render(request, 'catalogue/my_view.html')

@unauthenticated_user
def registerPage(request):
   
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request,'registration/register.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('catalogue:index')
        else:
            messages.info(request, 'Username or Password incorrect!')
    context = {}
    return render(request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    return render(request, 'profile.html')

def Rate(request, name):
    album = Album.objects.get(name=Album.name)
    user = request.user

    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.album = album
            rate.save()