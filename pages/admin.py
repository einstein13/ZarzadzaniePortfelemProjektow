from django.contrib import admin

from .forms import HtmlContentForm
from .models import HtmlContent

class HtmlContentAdmin(admin.ModelAdmin):
    # this is class replacing the form to WYSIWYG one
    form = HtmlContentForm

admin.site.register(HtmlContent, HtmlContentAdmin)
