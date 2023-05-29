from django.shortcuts import render, redirect, get_object_or_404
from ..models import Workout
from ..forms import WorkoutForm
from django.contrib.admin.views.decorators import staff_member_required
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def list(request):
    if not request.user.is_authenticated:
        workouts = []
    elif request.user.is_staff:
        workouts = Workout.objects.all()
    else:
        workouts = Workout.objects.filter(owner=request.user)
    return render(request, 'workout/list.html', {'workouts': workouts})  # noqa


@staff_member_required()
def delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        workout.delete()
        messages.success(request, "Workout delete successful!")
        return redirect('workout_list')
    return render(request, 'workout/confirm_delete.html', {'workout': workout})   # noqa


@staff_member_required()
def update(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    form = WorkoutForm(request.POST or None, instance=workout)  # noqa
    if form.is_valid():
        form.save()
        messages.success(request, "Workout updated successful!")
        return redirect('workout_list')
    return render(request, 'form.html', {'form': form, 'title': 'Update Workout'})  # noqa


@login_required()
def detail(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    return render(request, 'workout/detail.html', {'workout': workout})   # noqa
