from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import Auto


class AutoModelTests(TestCase):
	def test_auto_str_returns_readable_name(self):
		auto = Auto.objects.create(
			brand="Toyota",
			model="Corolla",
			year=2022,
			price="25000.00",
			color="White",
			transmission="automatic",
			fuel_type="gasoline",
			mileage=30000,
			description="Reliable sedan",
		)

		self.assertEqual(str(auto), "2022 Toyota Corolla")

	def test_default_ordering_is_newest_first(self):
		older = Auto.objects.create(
			brand="Honda",
			model="Civic",
			year=2020,
			price="22000.00",
			color="Black",
			transmission="manual",
			fuel_type="gasoline",
			mileage=45000,
			description="Compact car",
		)
		newer = Auto.objects.create(
			brand="Tesla",
			model="Model 3",
			year=2023,
			price="39000.00",
			color="Red",
			transmission="automatic",
			fuel_type="electric",
			mileage=12000,
			description="EV",
		)

		autos = list(Auto.objects.all())
		self.assertEqual(autos[0], newer)
		self.assertEqual(autos[1], older)


class AutoViewTests(TestCase):
	def setUp(self):
		self.auto = Auto.objects.create(
			brand="Ford",
			model="Focus",
			year=2019,
			price="16000.00",
			color="Blue",
			transmission="manual",
			fuel_type="diesel",
			mileage=70000,
			description="Used hatchback",
		)

	def _valid_payload(self):
		return {
			"brand": "BMW",
			"model": "320i",
			"year": "2021",
			"price": "31000.00",
			"color": "Gray",
			"transmission": "automatic",
			"fuel_type": "gasoline",
			"mileage": "20000",
			"description": "Sport sedan",
		}

	def test_index_view(self):
		response = self.client.get(reverse("myapp:index"))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "index.html")

	def test_auto_list_view(self):
		response = self.client.get(reverse("myapp:auto-list"))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "auto_list.html")
		self.assertContains(response, "Ford")

	def test_auto_detail_view(self):
		response = self.client.get(reverse("myapp:auto-detail", args=[self.auto.pk]))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "auto_detail.html")
		self.assertEqual(response.context["auto"], self.auto)

	def test_auto_create_view_post_creates_auto(self):
		response = self.client.post(reverse("myapp:auto-create"), data=self._valid_payload())

		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, reverse("myapp:auto-list"))
		self.assertEqual(Auto.objects.count(), 2)
		created = Auto.objects.get(brand="BMW", model="320i")
		self.assertEqual(created.year, 2021)
		self.assertEqual(created.price, Decimal("31000.00"))

	def test_auto_update_view_post_updates_auto(self):
		payload = self._valid_payload()
		payload["brand"] = "Audi"
		payload["model"] = "A4"
		payload["year"] = "2020"

		response = self.client.post(
			reverse("myapp:auto-update", args=[self.auto.pk]),
			data=payload,
		)

		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, reverse("myapp:auto-detail", args=[self.auto.pk]))

		self.auto.refresh_from_db()
		self.assertEqual(self.auto.brand, "Audi")
		self.assertEqual(self.auto.model, "A4")
		self.assertEqual(self.auto.year, 2020)

	def test_auto_delete_view_post_deletes_auto(self):
		response = self.client.post(reverse("myapp:auto-delete", args=[self.auto.pk]))

		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, reverse("myapp:auto-list"))
		self.assertFalse(Auto.objects.filter(pk=self.auto.pk).exists())
