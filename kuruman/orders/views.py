import json

from django.template.defaultfilters import date as date_filter
from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView
from django_ktdatatable_view.base_ktdatatable_view import BaseKTDatatableView

from kuruman.orders.models import Order


class KTDatatableIndexView(TemplateView):
    template_name = "orders/ktdatatable.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['columns'] = json.dumps(KTDatatableView.columns)
        return data


class KTDatatableView(BaseKTDatatableView):
    columns = [
        {"field": 'order_id', 'title': f'{_("# Order ID")}', "textAlign": "center"},
        {"field": 'country', 'title': f'{_("Country")}', "textAlign": "center"},
        {"field": 'created_at', 'title': f'{_("Ship Date")}', "sortable": "desc", "textAlign": "center"},
        {"field": 'company', 'title': f'{_("Company Name")}', "textAlign": "center"},
        {"field": 'status', 'title': f'{_("Status")}', "textAlign": "center"},
        {"field": 'type', 'title': f'{_("Type")}', "textAlign": "center"},
        {"field": 'actions', 'title': f'{_("Actions")}', 'sortable': False, "textAlign": "center"}
    ]
    model = Order

    def render_column(self, row, column):
        row: Order

        if column == "order_id":
            return f"#{row.order_id.upper()}"
        elif column == "created_at":
            return f"{date_filter(row.created_at)}"
        elif column == "status":
            class_name = 'info'
            if row.status == Order.STATUS_PENDING:
                class_name = 'success'
            if row.status == Order.STATUS_DELIVERED or row.status == Order.STATUS_DANGER:
                class_name = 'danger'
            if row.status == Order.STATUS_CANCELED:
                class_name = 'primary'
            return f'<span><span class="label label-lg font-weight-bold label-inline label-square label-light-{class_name}">{row.get_status_display()}</span></span>'
        elif column == "type":
            class_name = 'primary'
            if row.type == Order.TYPE_ONLINE:
                class_name = 'danger'
            if row.type == Order.TYPE_DIRECT:
                class_name = 'success'
            return f'<span>' \
                   f'<span class="label label-{class_name} label-dot mr-2"></span>' \
                   f'<span class="font-weight-bold text-{class_name}">{row.get_type_display()}</span>' \
                   f'</span>'
        elif column == "actions":
            show_btn = render_to_string(
                "buttons/show.html",
                {
                    "url": "#"
                }
            )
            return "".join([show_btn])
        else:
            return super(KTDatatableView, self).render_column(row, column)


class DatatablesView(BaseDatatableView):
    columns = [
        'order_id',
        'country',
        'created_at',
        'company',
        'status',
        'type',
        'actions'
    ]
    model = Order

    def render_column(self, row, column):
        row: Order

        if column == "order_id":
            return f"#{row.order_id.upper()}"
        elif column == "created_at":
            return f"{date_filter(row.created_at)}"
        elif column == "status":
            class_name = 'info'
            if row.status == Order.STATUS_PENDING:
                class_name = 'success'
            if row.status == Order.STATUS_DELIVERED or row.status == Order.STATUS_DANGER:
                class_name = 'danger'
            if row.status == Order.STATUS_CANCELED:
                class_name = 'primary'
            return f'<span><span class="label label-lg font-weight-bold label-inline label-square label-light-{class_name}">{row.get_status_display()}</span></span>'
        elif column == "type":
            class_name = 'primary'
            if row.type == Order.TYPE_ONLINE:
                class_name = 'danger'
            if row.type == Order.TYPE_DIRECT:
                class_name = 'success'
            return f'<span class="label label-{class_name} label-dot mr-2"></span>' \
                   f'<span class="font-weight-bold text-{class_name}">{row.get_type_display()}</span>'
        elif column == "actions":
            show_btn = render_to_string(
                "buttons/show.html",
                {
                    "url": "#"
                }
            )
            return "".join([show_btn])
        else:
            return super(DatatablesView, self).render_column(row, column)
