from django.shortcuts import render, redirect, get_object_or_404
from ..models import WorkoutSheet
from ..forms import WorkoutSheetForm
from django.contrib.admin.views.decorators import staff_member_required


def list(request):
    workout_sheets = WorkoutSheet.objects.all()
    return render(request, 'workout_sheet/list.html', {'workout_sheets': workout_sheets})  # noqa


@staff_member_required()
def create(request):
    form = WorkoutSheetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('workout_sheet_list')
    return render(request, 'form.html', {'form': form, 'title': 'Create Workout Sheet'})  # noqa


@staff_member_required()
def update(request, pk):
    workout_sheet = get_object_or_404(WorkoutSheet, pk=pk)
    form = WorkoutSheetForm(request.POST or None, instance=workout_sheet)
    if form.is_valid():
        form.save()
        return redirect('workout_sheet_list')
    return render(request, 'form.html', {'form': form, 'title': 'Update Workout Sheet'})  # noqa


@staff_member_required()
def delete(request, pk):
    workout_sheet = get_object_or_404(WorkoutSheet, pk=pk)
    if request.method == 'POST':
        workout_sheet.delete()
        return redirect('workout_sheet_list')
    return render(request, 'workout_sheet/confirm_delete.html', {'workout_sheet': workout_sheet})   # noqa


def details(request, pk):
    workout_sheet = get_object_or_404(WorkoutSheet, pk=pk)
    mo = workout_sheet.workoutprescription_set.filter(day_of_week='MO')
    tu = workout_sheet.workoutprescription_set.filter(day_of_week='TU')
    we = workout_sheet.workoutprescription_set.filter(day_of_week='WE')
    th = workout_sheet.workoutprescription_set.filter(day_of_week='TH')
    fr = workout_sheet.workoutprescription_set.filter(day_of_week='FR')
    sa = workout_sheet.workoutprescription_set.filter(day_of_week='SA')
    su = workout_sheet.workoutprescription_set.filter(day_of_week='SU')
    return render(request, 'workout_sheet/details.html', {
        'workout_sheet': workout_sheet,
        'mo': mo,
        'tu': tu,
        'we': we,
        'th': th,
        'fr': fr,
        'sa': sa,
        'su': su
        })   # noqa

