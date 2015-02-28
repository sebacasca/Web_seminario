from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$','commerce.views.pagina', name='principal'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT}
	),

    url(r'^lista/','commerce.views.lista_producto', name='lista'),
	url(r'^nuevousuario/$', 'commerce.views.nuevousuario', name='nuevousuario'),
	url(r'^ingresar/$','commerce.views.ingresar',name='ingresar'),
	url(r'^privado/$','commerce.views.privado'),
	url(r'^cerrar/$', 'commerce.views.cerrar', name='cerrar'),
	#url(r'^descripcion_producto/(?P<slug>[-\w]+)/(?P<id>\d+)/$','commerce.views.producto_individual', name='ver_producto'),
	url(r'^producto_individual/$', 'commerce.views.producto_individual', name='ver_producto'),
	url(r'^mi_carrito/$', 'commerce.views.mi_carro', name='mi_carrito'),
	
	url(r'^mi_compra/$', 'commerce.views.mi_compra', name='mi_compra'),
	

)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
