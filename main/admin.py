from django.contrib import admin
from .models import Registration
from .models import Branch
from .models import News
from .models import Gallery

admin.site.register(Registration)

admin.site.register(Branch)

admin.site.register(News)

admin.site.register(Gallery)