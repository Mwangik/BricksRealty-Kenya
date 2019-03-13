from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator
from listings.choices import price_choices, bedroom_choices, county_choices

# Create your views here.
def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
         'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):

     listing = get_object_or_404(Listing, pk=listing_id)
     context = {
          'listing': listing
     }
     return render(request, 'listings/listing.html', context)

def search(request):
     context = {
        'county_choices': county_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices
        }
     return render(request, 'listings/search.html', context)


