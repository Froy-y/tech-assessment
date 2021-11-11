from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservations/<int:reservations_id>/', views.reservation_details, name='reservation_details'),
    path('reservations/create/', views.ReservationCreate.as_view(), name='reservation_create'),
    path('reservations/<int:pk>/update/', views.ReservationUpdate.as_view(), name='reservation_update'),
    path('reservations/<int:pk>/delete/', views.ReservationDelete.as_view(), name='reservation_delete'),
    path('listings/', views.ListingsList.as_view(), name='listing_list'),
    path('listings/<int:pk>/', views.ListingDetail.as_view(), name='listing_details'),
    path('listings/create/', views.ListingCreate.as_view(), name='listing_create'),
    path('listings/<int:pk>/update/', views.ListingUpdate.as_view(), name='listing_update'),
    path('listings/<int:pk>/delete/', views.ListingDelete.as_view(), name='listing_delete'),
    path('reservations/<int:reservations_id>/assoc_listing/<int:listing_id>/', views.assoc_listing, name='assoc_listing'),
    path('reservations/<int:reservations_id>/unassoc_listing/<int:listing_id>/', views.unassoc_listing, name='unassoc_listing'),
]