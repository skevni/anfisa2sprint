from django.contrib import admin

# Register your models here.
from .models import Category, IceCream, Topping, Wrapper


class IceCreamInLine(admin.TabularInline):
    model = IceCream
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = (IceCreamInLine,)
    list_display = (
        'title',
    )


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category',
    )
    search_fields = (
        'title',
    )
    list_filter = ('category',)
    list_display_links = ('title',)
    empty_value_display = 'Не задано'
    filter_horizontal = ('toppings',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Topping)
admin.site.register(Wrapper)
admin.site.register(IceCream, IceCreamAdmin)
