from django.contrib import admin

# Register your models here.
from .models import Hopital
from .models import Scolaire
from .models import Agriculture

admin.site.register(Hopital)
admin.site.register(Scolaire)
admin.site.register(Agriculture)