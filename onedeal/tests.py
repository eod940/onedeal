from django.test import TestCase, Client
from django.conf import settings
from iamport import Iamport

# Create your tests here.
from onedeal.models import Item


class TestView(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_item_manager(self):
        iamport = Iamport(
            imp_key= settings.IAMPORT_KEY,
            imp_secret = settings.IAMPORT_SECRET
        )
        response = iamport.find(merchant_uid='ORD20180131-0000011')
        iamport.is_paid('ORD20180131-0000011', response=response)
        Item.item_managers.all()

