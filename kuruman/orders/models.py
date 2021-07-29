import uuid

from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext as _


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.CharField(max_length=8)
    country = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    STATUS_INFO = 'INFO'
    STATUS_DELIVERED = 'DELIVERED'
    STATUS_DANGER = 'DANGER'
    STATUS_PENDING = 'PENDING'
    STATUS_CANCELED = 'CANCELED'
    STATUS_SUCCESS = 'SUCCESS'
    STATUS_CHOICES = [
        (STATUS_INFO, _("Info")),
        (STATUS_DELIVERED, _("Delivered")),
        (STATUS_DANGER, _("Danger")),
        (STATUS_PENDING, _("Pending")),
        (STATUS_CANCELED, _("Canceled")),
        (STATUS_SUCCESS, _("Success")),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_PENDING)
    TYPE_ONLINE = 'ONLINE'
    TYPE_RETAIL = 'RETAIL'
    TYPE_DIRECT = 'DIRECT'
    TYPE_CHOICES = [
        (TYPE_ONLINE, _("Online")),
        (TYPE_RETAIL, _("Retail")),
        (TYPE_DIRECT, _("Direct")),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=TYPE_ONLINE)
    created_at = models.DateField(default=now)

    def __str__(self):
        return f'#{str(self.id)[-8:]} {self.country} {self.company} {self.status} {self.type} {self.created_at}'

