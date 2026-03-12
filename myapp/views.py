from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from .models import Auto

# Home page
def index(request):
    return render(request, 'index.html', {'title': 'Home'})

# List all Autos
def auto_list(request):
    autos = Auto.objects.all()
    return render(request, 'auto_list.html', {'autos': autos})

# Create Auto
def auto_create(request):
    if request.method == 'POST':
        auto = Auto.objects.create(
            brand=request.POST.get('brand'),
            model=request.POST.get('model'),
            year=int(request.POST.get('year')),
            price=request.POST.get('price'),
            color=request.POST.get('color'),
            transmission=request.POST.get('transmission'),
            fuel_type=request.POST.get('fuel_type'),
            mileage=int(request.POST.get('mileage')),
            description=request.POST.get('description'),
        )
        messages.success(request, f"Auto {auto.brand} {auto.model} added successfully!")
        return redirect('myapp:auto-list')
    
    return render(request, 'auto_form.html', {'title': 'Add Auto'})

# Detail Auto
def auto_detail(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    return render(request, 'auto_detail.html', {'auto': auto})

# Update Auto
def auto_update(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    
    if request.method == 'POST':
        auto.brand = request.POST.get('brand')
        auto.model = request.POST.get('model')
        auto.year = int(request.POST.get('year'))
        auto.price = request.POST.get('price')
        auto.color = request.POST.get('color')
        auto.transmission = request.POST.get('transmission')
        auto.fuel_type = request.POST.get('fuel_type')
        auto.mileage = int(request.POST.get('mileage'))
        auto.description = request.POST.get('description')
        auto.save()
        messages.success(request, f"Auto updated successfully!")
        return redirect('myapp:auto-detail', pk=auto.pk)
    
    return render(request, 'auto_form.html', {'auto': auto, 'title': 'Edit Auto'})

# Delete Auto
def auto_delete(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    
    if request.method == 'POST':
        auto_name = f"{auto.brand} {auto.model}"
        auto.delete()
        messages.success(request, f"Auto {auto_name} deleted successfully!")
        return redirect('myapp:auto-list')
    
    return render(request, 'auto_confirm_delete.html', {'auto': auto})
