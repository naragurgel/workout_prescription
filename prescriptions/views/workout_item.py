from django.shortcuts import render, redirect, get_object_or_404
from ..models import WorkoutItem, WorkoutItem
from ..forms import WorkoutItemForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages


@staff_member_required()
def list(request):
    workout_items = WorkoutItem.objects.all()
    return render(request, 'workout_item/list.html', {'workout_items': workout_items})  # noqa


@staff_member_required()
def create(request):
    form = WorkoutItemForm(request.POST or None)  # noqa
    if form.is_valid():
        form.save()
        messages.success(request, "Workout created successful!")
        return redirect('workout_item_list')
    return render(request, 'form.html', {'form': form, 'title': 'Create Workout Item'})  # noqa


@staff_member_required()
def update(request, pk):
    workout_item = get_object_or_404(WorkoutItem, pk=pk)
    form = WorkoutItemForm(request.POST or None, instance=workout_item)  # noqa
    if form.is_valid():
        form.save()
        messages.success(request, "Workout updated successful!")
        return redirect('workout_item_list')
    return render(request, 'form.html', {'form': form, 'title': 'Update Workout Item'})  # noqa


@staff_member_required()
def delete(request, pk):
    workout_item = get_object_or_404(WorkoutItem, pk=pk)