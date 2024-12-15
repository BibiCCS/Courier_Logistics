from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from viewer.mixins import StaffRequiredMixin
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


# ----SearchCourier----
def search_courier(request):
    query = request.GET.get("q", "").strip()
    results = []

    if query:
        try:
            # Split query into street name and number
            street_name, number = query.split(", ")

            # Filter couriers based on the related neighborhood and street
            results = Courier.objects.filter(
                neighborhood__street__name__icontains=street_name.strip(),
                neighborhood__street__number__icontains=number.strip(),
            )
        except ValueError:
            # Handle invalid format gracefully
            results = []

    return render(request, "search_courier.html", {"query": query, "results": results})


# ----County Views---- #
class CountyListView(LoginRequiredMixin, ListView):
    model = County
    template_name = 'county_list.html'
    context_object_name = 'counties'
    success_url = reverse_lazy('county-list')


class CountyDetailView(LoginRequiredMixin, DetailView):
    model = County
    template_name = 'county_detail.html'
    context_object_name = 'county'
    success_url = reverse_lazy('county-list')


class CountyCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = County
    fields = ['name']
    template_name = 'county_form.html'
    success_url = reverse_lazy('county-list')
    permission_required = 'viewer.add_county'


class CountyUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = County
    fields = ['name']
    template_name = 'county_form.html'
    success_url = reverse_lazy('county-list')
    permission_required = 'viewer.change_county'


class CountyDeleteView(LoginRequiredMixin, StaffRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = County
    template_name = 'county_confirm_delete.html'
    success_url = reverse_lazy('county-list')
    permission_required = 'viewer.delete_county'


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


class CityCreateView(LoginRequiredMixin,  PermissionRequiredMixin, CreateView):
    model = City
    fields = ['name', 'county']
    template_name = 'city_form.html'
    success_url = reverse_lazy('city-list')
    permission_required = 'viewer.add_city'


class CityUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = City
    fields = ['name', 'county']
    template_name = 'city_form.html'
    success_url = reverse_lazy('city-list')
    permission_required = 'viewer.change_city'


class CityDeleteView(LoginRequiredMixin, StaffRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = City
    template_name = 'city_confirm_delete.html'
    success_url = reverse_lazy('city-list')
    permission_required = 'viewer.delete_city'


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


class NeighborhoodCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Neighborhood
    fields = ['name', 'city']
    template_name = 'neighborhood_form.html'
    success_url = reverse_lazy('neighborhood-list')
    permission_required = 'viewer.add_neighborhood'


class NeighborhoodUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Neighborhood
    fields = ['name', 'city']
    template_name = 'neighborhood_form.html'
    success_url = reverse_lazy('neighborhood-list')
    permission_required = 'viewer.change_neighborhood'


class NeighborhoodDeleteView(LoginRequiredMixin, StaffRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Neighborhood
    template_name = 'neighborhood_confirm_delete.html'
    success_url = reverse_lazy('neighborhood-list')
    permission_required = 'viewer.delete_neighborhood'


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


class StreetCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Street
    fields = ['name', 'number', 'neighborhood']
    template_name = 'street_form.html'
    success_url = reverse_lazy('street-list')
    permission_required = 'viewer.add_street'


class StreetUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Street
    fields = ['name', 'number', 'neighborhood']
    template_name = 'street_form.html'
    success_url = reverse_lazy('street-list')
    permission_required = 'viewer.change_street'


class StreetDeleteView(LoginRequiredMixin, StaffRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Street
    template_name = 'street_confirm_delete.html'
    success_url = reverse_lazy('street-list')
    permission_required = 'viewer.delete_street'


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


class CourierCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Courier
    fields = ['name', 'neighborhood']
    template_name = 'courier_form.html'
    success_url = reverse_lazy('courier-list')
    permission_required = 'viewer.add_courier'


class CourierUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Courier
    fields = ['name', 'neighborhood']
    template_name = 'courier_form.html'
    success_url = reverse_lazy('courier-list')
    permission_required = 'viewer.change_courier'


class CourierDeleteView(LoginRequiredMixin, StaffRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Courier
    template_name = 'courier-confirm-delete.html'
    success_url = reverse_lazy('courier-list')
    permission_required = 'viewer.delete_courier'


