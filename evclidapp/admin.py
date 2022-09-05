import site
from django.contrib import admin

from evclidapp.models import Appeal, IndexPage


admin.site.register(Appeal)
admin.site.register(IndexPage)
