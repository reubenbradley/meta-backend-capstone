from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from django.contrib.auth.models import User


class MenuViewTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="mytestuser",
            password="mytestpassword"
        )

        token = Token.objects.create(user=user)

        self.client = APIClient()
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {token.key}"
        )

        MenuItem.objects.create(
            Title="Ice Cream",
            Price=5,
            Inventory=100
        )

        MenuItem.objects.create(
            Title="Pizza",
            Price=15,
            Inventory=50
        )

    def test_getall(self):
        response = self.client.get("/restaurant/menu/")

        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)

        self.assertEqual(response.data, serializer.data)