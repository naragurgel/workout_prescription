from django.shortcuts import render, redirect, get_object_or_404
from ..models import Workout
from ..forms import WorkoutForm
from django.contrib.admin.views.decorators import staff_member_required


def list(request):
    workouts = Workout.objects.all()
    return render(request, 'workout/list.html', {'workouts': workouts})  # noqa


@staff_member_required()
def create(request):
    form = WorkoutForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('workout_list')
    return render(request, 'form.html', {'form': form, 'title': 'Create Workout'})  # noqa


@staff_member_required()
def update(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    form = WorkoutForm(request.POST or None, instance=workout)
    if form.is_valid():
        form.save()
        return redirect('workout_list')
    return render(request, 'form.html', {'form': form, 'title': 'Update Workout'})  # noqa


@staff_member_required()
def delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        workout.delete()
        return redirect('workout_list')
    return render(request, 'workout/confirm_delete.html', {'workout': workout})   # noqa