from django.contrib import admin
from commerce.models import *
from sorl.thumbnail.admin import AdminImageMixin


class ProductoAdmin(AdminImageMixin, admin.ModelAdmin):

    list_display = ('codigo','nombre_producto','precio','marca','genero','stock','activo')
    list_display_links = ('nombre_producto',)
    list_per_page = 50
    ordering = ['precio']
    search_fields = ['nombre_producto', 'descripcion']

    prepopulated_fields = {'slug' : ('nombre_producto',)}

admin.site.register(producto,ProductoAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_cat','nombre_cat')
    list_display_links = ('nombre_cat',)
    list_per_page = 20
    ordering = ['nombre_cat']
    search_fields = ['nombre_cat','desc_cat']
    

    prepopulated_fields = {'slug': ('nombre_cat',)}

admin.site.register(categoria, CategoriaAdmin)

class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_sc','nombre_sc',)
    list_display_links = ('nombre_sc',)
    ordering = ['nombre_sc']
    search_fields = ['nombre_sc']
    prepopulated_fields = {'slug': ('nombre_sc',)}

admin.site.register(subcategoria,SubcategoriaAdmin)

'''class Mode(AdminImageMixin, ModelAdmin):
    pass

class TabularInline(AdminImageMixin, TabularInline):
    pass

class StackedInline(AdminImageMixin, StackedInline):
    pass'''

    
    

    
