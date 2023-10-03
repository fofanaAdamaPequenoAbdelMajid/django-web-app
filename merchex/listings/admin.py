# listings/admin.py
from django.contrib import admin
from listings.models import Band
from listings.models import Listing


# Register your models here.
class BandAdmin(admin.ModelAdmin):
	list_display = ('name', 'genre', 'yearFormed' , 'active', 'officialHomepage', 'biography')
admin.site.register(Band, BandAdmin)

class BandAdmin2(admin.ModelAdmin):
	list_display = ('title', 'sold', 'year', 'type')
admin.site.register(Listing, BandAdmin2)

class ListingAdmin(admin.ModelAdmin):
	list_display = ('title', 'band')