from django.shortcuts import render, redirect, get_object_or_404
from ..models import Equipment
from ..forms import EquipmentForm
from django.views.generic import CreateView

def list(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment/list.html', {'equipments': equipments})


def create(request):
    form = EquipmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('equipment_list')
    return render(request, 'form.html', {'form': form, 'title': 'Create Equipment'})  # noqa


def update(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    form = EquipmentForm(request.POST or None, instance=equipment_group)
    if form.is_valid():
        form.save()
        return redirect('equipment_list')
    return render(request, 'form.html', {'form': form, 'title': 'Update Equipment'})  # noqa


def delete(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        equipment.delete()
        return redirect('equipment_list')
    return render(request, 'equipment/confirm_delete.html', {'equipment': equipment})  # noqa