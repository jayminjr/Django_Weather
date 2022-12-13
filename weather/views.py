from django.utils.timezone import now, timedelta
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from weather.forms import CityForm
from django.urls import reverse
from django.contrib import messages
import requests

from weather.models import City

# Create your views here.
def get_city_data(city):
    """
    API call for get city weather details.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=1be6324f259e2d5ad5e3f216c7627890"
    data = requests.get(url).json()
    if data["cod"] != 200:
        return None
    new_city_ojb = City(
        name=data["name"],
        temperature=data.get("main", {}).get("temp"),
        min_temp=data.get("main", {}).get("temp_min"),
        max_temp=data.get("main", {}).get("temp_max"),
        wind_speed=data.get("wind", {}).get("speed"),
        humidity=data.get("main", {}).get("humidity"),
    )
    new_city_ojb.save()
    return new_city_ojb


class HomeView(View):
    """
    A View to display recent cities.
    """

    template_name = "city_list.html"

    def get(self, request, *args, **kwargs):
        context = {
            "form": CityForm(),
            "cities": City.objects.all().order_by("-created_at")[:5]
            or City.objects.all().order_by("-created_at"),
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data.get("name")
            city_name = city_name.capitalize()
            if (
                city := City.objects.filter(name=city_name)
                .order_by("-created_at")
                .first()
            ):
                session_time = now() - timedelta(minutes=60)
                if city.created_at >= session_time:
                    return redirect(reverse("city_detail", kwargs={"pk": city.pk}))
                city.delete()
                data = get_city_data(city_name)
                return redirect(reverse("city_detail", kwargs={"pk": data.pk}))
            else:
                if data := get_city_data(city_name):
                    return redirect(reverse("city_detail", kwargs={"pk": data.pk}))
                messages.error(request, "Please enter valid city name.")
                return redirect(reverse("home"))
        else:
            context = {
                "form": form,
            }
            return render(request, self.template_name, context=context)


class CityDetailView(DetailView):
    """
    A DetailView to display city weather detail
    """

    model = City
    template_name = "city_detail.html"
