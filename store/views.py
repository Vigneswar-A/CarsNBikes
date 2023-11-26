from django.shortcuts import render
from store.forms import Sell, Buy, PRICE_DIFF, KM_DIFF
from django.http import *
from store.models import Vehicle
from django.utils.html import escape

def home(request):
    if request.GET.get("action") == "sell":
        form = Sell()
        return render(request, "sell.html", {"form": form})
    elif request.GET.get("action") == "buy":
        form = Buy()
        return render(request, "buy.html", {"form": form})
    else:
        return render(request, "index.html")
    
def sell(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    data = Sell(request.POST)
    if not data.is_valid():
        return HttpResponseBadRequest("<h1>Invalid Format!</h1>")
    sanitized_data = {}
    for field, value in data.cleaned_data.items():
        sanitized_value = escape(value)
        sanitized_data[field] = sanitized_value
    Vehicle(**sanitized_data).save()
    return HttpResponseRedirect("/store")
    

def buy(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    data = Buy(request.POST)
    if not data.is_valid():
        return HttpResponseBadRequest("<h1>Invalid Format!</h1>")
    params = data.cleaned_data
    filters = {
        "VehicleType" : params.get("vehicle_type"),
        "Kilometers__range" : [int(params.get("kilometers"))*KM_DIFF, (int(params.get("kilometers"))+1)*(KM_DIFF)],
        "Price__range" : [int(params.get("price"))*PRICE_DIFF, (int(params.get("price"))+1)*(PRICE_DIFF)],
    }

    if (brand := params.get("brand")):
        filters["Brand__icontains"] = brand

    results = Vehicle.objects.filter(**filters)
    return JsonResponse(list(results.values()), safe=False, content_type='application/json')