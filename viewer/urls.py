from django.urls import path, reverse
from . import views
from viewer.views import (
    CityListView, CityDetailView, CityCreateView, CityUpdateView, CityDeleteView,NeighborhoodListView,
    NeighborhoodDetailView, NeighborhoodCreateView, NeighborhoodUpdateView, NeighborhoodDeleteView,
    StreetListView, StreetDetailView, StreetCreateView, StreetUpdateView, StreetDeleteView,
    CourierListView, CourierDetailView, CourierCreateView, CourierUpdateView, CourierDeleteView,
    DashBoardView,
    CountyListView, CountyDetailView, CountyCreateView, CountyUpdateView, CountyDeleteView,
)


urlpatterns = [
    # ----HomePage----
    path('', views.home, name='home'),

    # ----Dashboard Page----
    path('dashboard/', DashBoardView.as_view(), name='dashboard'),

    # ----County----
    path('county/', CountyListView.as_view(), name='county-list'),
    path('county/<int:pk>/', CountyDetailView.as_view(), name='county-detail'),
    path('county/add/', CountyCreateView.as_view(), name='county-add'),
    path('county/<int:pk>/edit/', CountyUpdateView.as_view(), name='county-edit'),
    path('county/<int:pk>/delete/', CountyDeleteView.as_view(), name='county-delete'),

    # ----City----
    path('cities/', CityListView.as_view(), name='city-list'),
    path('cities/<int:pk>/', CityDetailView.as_view(), name='city-detail'),
    path('cities/add/', CityCreateView.as_view(), name='city-add'),
    path('cities/<int:pk>/edit/', CityUpdateView.as_view(), name='city-edit'),
    path('cities/<int:pk>/delete/', CityDeleteView.as_view(), name='city-delete'),

    # ----Neighborhood----
    path('neighborhoods/', NeighborhoodListView.as_view(), name='neighborhood-list'),
    path('neighborhoods/<int:pk>/', NeighborhoodDetailView.as_view(), name='neighborhood-detail'),
    path('neighborhoods/add/', NeighborhoodCreateView.as_view(), name='neighborhood-add'),
    path('neighborhoods/<int:pk>/edit/', NeighborhoodUpdateView.as_view(), name='neighborhood-edit'),
    path('neighborhoods/<int:pk>/delete/', NeighborhoodDeleteView.as_view(), name='neighborhood-delete'),

    # ----Street----
    path('streets/', StreetListView.as_view(), name='street-list'),
    path('streets/<int:pk>/',StreetDetailView.as_view(), name='street-detail'),
    path('streets/add/', StreetCreateView.as_view(), name='street-add'),
    path('streets/<int:pk>/edit/', StreetUpdateView.as_view(), name='street-edit'),
    path('streets/<int:pk>/delete/', StreetDeleteView.as_view(), name='street-delete'),

    # ----Courier----
    path('couriers/', CourierListView.as_view(), name='courier-list'),
    path('couriers/<int:pk>/', CourierDetailView.as_view(), name='courier-detail'),
    path('couriers/add/', CourierCreateView.as_view(), name='courier-add'),
    path('couriers/<int:pk>/edit/', CourierUpdateView.as_view(), name='courier-edit'),
    path('couriers/<int:pk>/delete/', CourierDeleteView.as_view(), name='courier-delete'),

]