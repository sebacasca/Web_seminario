from django.db import models
from datetime import datetime
#from django.contrib.auth.models import User
from sorl.thumbnail import ImageField #BAJAR LA VERSION pip install sorl-thumbnail==11.12.1b SINO NO ANDA!



class categoria(models.Model):
    id_cat = models.AutoField(primary_key=True)#ME PARECE QUE LOS ID ESTAN AL PEDO
    nombre_cat = models.CharField(max_length=100)
    desc_cat = models.TextField()
    slug = models.SlugField(max_length = 255, unique=True, help_text= 'Direccion unica de url.')
    def __unicode__(self):
        return self.nombre_cat
    @models.permalink
    def get_absolute_url(self):
        return ('Categoria', (), { 'categoria_slug': self.slug})


class subcategoria(models.Model):
    id_sc = models.AutoField(primary_key=True)
    nombre_sc = models.CharField(max_length=100)
    categoria =models.ForeignKey('categoria', related_name='C')
    slug = models.SlugField(max_length = 255, unique=True, help_text= 'Direccion unica de url.')
    def __unicode__(self):
        return self.nombre_sc
    @models.permalink
    def get_absolute_url(self):
        return ('Subcategoria', (), { 'subcategoria_slug': self.slug})


class producto(models.Model):
    genero_choices = (('M', 'Masculino'),
            ('F', 'Femenino'),
            ('U', 'Unisex'))
    codigo = models.AutoField(primary_key=True)#models.IntegerField()
    nombre_producto = models.CharField(max_length=100)
    subcategoria = models.ForeignKey('subcategoria' ,related_name='SC')
    marca = models.CharField(max_length=100)
    stock = models.IntegerField(blank=False)
    genero = models.CharField(max_length=10, choices=genero_choices,default='M')
    precio = models.DecimalField(max_digits=9, decimal_places = 2)
    activo = models.BooleanField(default=False)
    descripcion = models.TextField()
    #imagen = ImageWithThumbsField(upload_to='foto_producto', sizes=((200,200),(125,125)))#Carga la imagen, guarda la original mas las dos redimensionadas
    imagen = ImageField(upload_to='foto_producto')
    slug = models.SlugField(max_length = 255, unique=True, help_text= 'Direccion unica de url.')
	

    class Meta:
        ordering = ['nombre_producto']
        
    def __unicode__(self):
        return self.nombre_producto

    @models.permalink
    def get_absolute_url(self):
        return ('catalogo_producto', (), { 'producto_slug': self.slug})
