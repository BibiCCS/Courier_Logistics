from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from viewer.models import County, City, Neighborhood, Street, Courier, Microzones




# ----Home Views----
def home(request):
    return render(request, 'home.html')


# ----Dashboard Views----
class DashBoardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    login_url = '/admin/login/'


# ----Microzones----
class MicrozonesTemplateView(LoginRequiredMixin, TemplateView):
    model = Microzones
    template_name = 'microzones.html'


# ----County Views---- #
class CountyListView(LoginRequiredMixin, ListView):
    model = County
    template_name = 'county_list.html'
    context_object_name = 'counties'
    success_url = reverse_lazy('county-list')

class CountyDetailView(LoginRequiredMixin, DetailView):
    model = County
    template_name = 'county-detail.html'
    context_object_name = 'county'
    success_url = reverse_lazy('county-list')

class CountyCreateView(LoginRequiredMixin, CreateView):
    model = County
    fields = ['name']
    template_name = 'county_form.html'
    success_url = reverse_lazy('county-list')

class CountyUpdateView(LoginRequiredMixin, UpdateView):
    model = County
    fields = ['name']
    template_name = 'county_form.html'
    success_url = reverse_lazy('county-list')

class CountyDeleteView(LoginRequiredMixin, DeleteView):
    model = County
    template_name = 'county_confirm_delete.html'
    success_url = reverse_lazy('county-list')


# ----City Views---- #
class CityListView(LoginRequiredMixin, ListView):
    model = City
    template_name = 'city_list.html'
    context_object_name = 'cities'
    success_url = reverse_lazy('city-list')


class CityDetailView(LoginRequiredMixin, DetailView):
    model = City
    template_name = 'city_detail.html'
    context_object_name = 'city'
    success_url = reverse_lazy('city-list')

class CityCreateView(LoginRequiredMixin, CreateView):
    model = City
    fields = ['name', 'county']
    template_name = 'city_form.html'
    success_url = reverse_lazy('city-list')


class CityUpdateView(LoginRequiredMixin, UpdateView):
    model = City
    fields = ['name', 'county']
    template_name = 'city_form.html'
    success_url = reverse_lazy('city-list')


class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    template_name = 'city_confirm_delete.html'
    success_url = reverse_lazy('city-list')


# ----Neighborhood Views---- #
class NeighborhoodListView(LoginRequiredMixin, ListView):
    model = Neighborhood
    template_name = 'neighborhood_list.html'
    context_object_name = 'neighborhoods'
    success_url = reverse_lazy('neighborhood-list')


class NeighborhoodDetailView(LoginRequiredMixin, DetailView):
    model = Neighborhood
    template_name = 'neighborhood_detail.html'
    context_object_name = 'neighborhood'
    success_url = reverse_lazy('neighborhood-list')


class NeighborhoodCreateView(LoginRequiredMixin, CreateView):
    model = Neighborhood
    fields = ['name', 'city']
    template_name = 'neighborhood_form.html'
    success_url = reverse_lazy('neighborhood-list')


class NeighborhoodUpdateView(LoginRequiredMixin, UpdateView):
    model = Neighborhood
    fields = ['name', 'city']
    template_name = 'neighborhood_form.html'
    success_url = reverse_lazy('neighborhood-list')


class NeighborhoodDeleteView(LoginRequiredMixin, DeleteView):
    model = Neighborhood
    template_name = 'neighborhood_confirm_delete.html'
    success_url = reverse_lazy('neighborhood-list')


# ----Street Views---- #
class StreetListView(LoginRequiredMixin, ListView):
    model = Street
    template_name = 'street_list.html'
    context_object_name = 'streets'
    success_url = reverse_lazy('street-list')

class StreetDetailView(LoginRequiredMixin, DetailView):
    model = Street
    template_name = 'street_detail.html'
    context_object_name = 'street'
    success_url = reverse_lazy('street-list')

class StreetCreateView(LoginRequiredMixin, CreateView):
    model = Street
    fields = ['name', 'number', 'neighborhood']
    template_name = 'street_form.html'
    success_url = reverse_lazy('street-list')

class StreetUpdateView(LoginRequiredMixin, UpdateView):
    model = Street
    fields = ['name', 'number', 'neighborhood']
    template_name = 'street_form.html'
    success_url = reverse_lazy('street-list')

class StreetDeleteView(LoginRequiredMixin, DeleteView):
    model = Street
    template_name = 'street_confirm_delete.html'
    success_url = reverse_lazy('street-list')


# ----Courier Views---- #
class CourierListView(LoginRequiredMixin, ListView):
    model = Courier
    template_name = 'courier_list.html'
    context_object_name = 'couriers'
    success_url = reverse_lazy('courier-list')

class CourierDetailView(LoginRequiredMixin, DetailView):
    model = Courier
    template_name = 'courier_detail.html'
    context_object_name = 'courier'
    success_url = reverse_lazy('courier-list')

class CourierCreateView(LoginRequiredMixin, CreateView):
    model = Courier
    fields = ['name', 'neighborhood']
    template_name = 'courier_form.html'
    success_url = reverse_lazy('courier-list')

class CourierUpdateView(LoginRequiredMixin, UpdateView):
    model = Courier
    fields = ['name', 'neighborhood']
    template_name = 'courier_form.html'
    success_url = reverse_lazy('courier-list')

class CourierDeleteView(LoginRequiredMixin, DetailView):
    model = Courier
    template_name = 'courier-confirm-delete.html'
    success_url = reverse_lazy('courier-list')

