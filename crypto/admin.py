from django.contrib import admin
from .models import Crypto, Network


@admin.register(Crypto)
class CryptoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'full_name', 'time_create', 'is_published')
    prepopulated_fields = {'slug': ('full_name', )}
    filter_horizontal = ['networks']
    list_display_links = ('id', 'title')
    ordering = ['-time_create', 'title']
    list_editable = ('is_published', )
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ['titile', 'full_name']
    list_filter = ['is_published']

    @admin.display(description='Publish selected entries')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Crypto.Status.PUBLISHED)
        self.message_user(request, f'{count} records have been changed')

    @admin.display(description='Remove selected entries from publication')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Crypto.Status.DRAFT)
        self.message_user(request, f'{count} entries have been removed from publication')


class CryptoInlaine(admin.TabularInline):
    model = Crypto.networks.through
    extra = 1


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'full_name')
    prepopulated_fields = {'slug': ('full_name',)}
    list_display_links = ('id', 'title')
    ordering = ['title', 'full_name']
    list_per_page = 5
    search_fields = ['titile', 'full_name']
    inlines = [CryptoInlaine]
