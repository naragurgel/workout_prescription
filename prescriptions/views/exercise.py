from django.shortcuts import render, redirect, get_object_or_404
from ..models import Exercise
from ..forms import ExerciseForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages


@staff_member_required()
def list(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercise/list.html', {'exercises': exercises})


@staff_member_required()
def create(request):
    form = ExerciseForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Workout created successful!")
        return redirect('exercise_list')
    return render(request, 'form.html', {'form': form, 'title': 'Create Exercise'})  # noqa


@staff_member_required()
def update(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    form = ExerciseForm(request.POST or None, instance=exercise)
    if form.is_valid():
        form.save()
        messages.success(request, "Workout updated successful!")
        return redirect('exercise_list')
    return render(request, 'form.html', {'form': form, 'title': 'Update Exercise'})  # noqa


@staff_member_required()
def delete(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        exercise.delete()
        messages.success(request, "Workout delete successful!")
        return redirect('exercise_list')
    return render(request, 'exercise/confirm_delete.html', {'exercise': exercise})  # noqa
