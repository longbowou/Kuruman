from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic import TemplateView

from kuruman.orders import views

urlpatterns = [
    path('', views.KTDatatableIndexView.as_view(), name="ktdatatable"),
    path('json', views.KTDatatableView.as_view(), name="ktdatatable-dt"),

    path('datatables', TemplateView.as_view(template_name="orders/datatables.html"), name="datatables"),
    path('datatables.json', views.DatatablesView.as_view(), name="datatables-dt")
]

urlpatterns += staticfiles_urlpatterns()

