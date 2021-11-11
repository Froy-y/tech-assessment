from django.db.models import query
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Reservation, Listing
from .filters import ReservationFilter

# Create your views here.
#home
def home(request):
    return render(request, 'home.html')

# Reservations
# index
def reservations(request):
    # Capability to list all reservations
    reservation = Reservation.objects.all()
    # filter
    myFilter = ReservationFilter(request.GET, queryset=reservation)
    reservation = myFilter.qs
    
    return render(request, 'reservations/index.html', {
        'reservations': reservation,
        'myFilter': myFilter
    })

# show
def reservation_details(request, reservations_id):
    reservation = Reservation.objects.get(id=reservations_id)
    listings_avaliable = Listing.objects.exclude(id__in = reservation.listing.all().values_list('id'))
    
    return render(request, 'reservations/detail.html', {
        'reservations': reservation,
        'listings': listings_avaliable
    })

# post
# Create a new reservation
class ReservationCreate(CreateView):
    model = Reservation
    fields = ['name', 'check_in', 'check_out']
    
    def form_valid(self, form):
        return super().form_valid(form)

# put
# Modify one reservation / Modify multiple reservations
class ReservationUpdate(UpdateView):
    model = Reservation
    fields = ['name', 'check_in', 'check_out']

# delete
class ReservationDelete(DeleteView):
    model = Reservation
    success_url = '/reservations/'
    
# Listings M:M
# index
class ListingsList(ListView):
    model = Listing
    
# show
class ListingDetail(DetailView):
    model = Listing
    
# post
class ListingCreate(CreateView):
    model = Listing
    fields = '__all__'

# put
class ListingUpdate(UpdateView):
    model = Listing
    fields = '__all__'

# delete
class ListingDelete(DeleteView):
    model = Listing
    success_url = '/listings'
    
# associations between listing and reservations
# assoc
def assoc_listing(request, reservations_id, listing_id): 
    Reservation.objects.get(id=reservations_id).listing.add(listing_id)
    return redirect('reservation_details', reservations_id=reservations_id)

def unassoc_listing(request, reservations_id, listing_id):
    Reservation.objects.get(id=reservations_id).listing.remove(listing_id)
    return redirect('reservation_details', reservations_id=reservations_id)