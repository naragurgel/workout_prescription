from django.shortcuts import render, redirect, get_object_or_404
from ..models import WorkoutPrescription, WorkoutSheet
from ..forms import WorkoutPrescriptionForm


def create(request, workout_sheet_id, day_of_week):
    workout_sheet = get_object_or_404(WorkoutSheet, pk=workout_sheet_id)
    workout_prescription = WorkoutPrescription(day_of_week=day_of_week, workout_sheet=workout_sheet)  # noqa
    form = WorkoutPrescriptionForm(request.POST or None, instance=workout_prescription)  # noqa
    if form.is_valid():
        form.save()
        return redirect('workout_sheet_details', pk=workout_sheet_id)
    return render(request, 'form.html', {'form': form, 'title': 'Create Workout Sheet'})  # noqa


def update(request, pk):
    workout_prescription = get_object_or_404(WorkoutPrescription, pk=pk)
    form = WorkoutPrescriptionForm(request.POST or None, instance=workout_prescription)  # noqa
    if form.is_valid():
        form.save()
        return redirect('workout_prescription_list')
    return render(request, 'form.html', {'form': form, 'title': 'Update Workout Sheet'})  # noqa


def delete(request, pk):
    workout_prescription = get_object_or_404(WorkoutPrescription, pk=pk)
    if request.method == 'POST':
        workout_prescription.delete()
        return redirect('workout_prescription_list')
    return render(request, 'workout_prescription/confirm_delete.html', {'workout_prescription': workout_prescription})   # noqa
