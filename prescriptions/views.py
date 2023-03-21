from django.shortcuts import render, redirect, get_object_or_404
from .models import MuscleGroup
from .forms import MuscleGroupForm


def muscle_group_list(request):
    muscle_groups = MuscleGroup.objects.all()
    return render(request, 'muscle_group/list.html', {'muscle_groups': muscle_groups})


def muscle_group_create(request):
    form = MuscleGroupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('muscle_group_list')
    return render(request, 'muscle_group/form.html', {'form': form})


def muscle_group_update(request, pk):
    muscle_group = get_object_or_404(MuscleGroup, pk=pk)
    form = MuscleGroupForm(request.POST or None, instance=muscle_group)
    if form.is_valid():
        form.save()
        return redirect('muscle_group_list')
    return render(request, 'muscle_group/form.html', {'form': form})


def muscle_group_delete(request, pk):
    muscle_group = get_object_or_404(MuscleGroup, pk=pk)
    if request.method == 'POST':
        muscle_group.delete()
        return redirect('muscle_group_list')
    return render(request, 'muscle_group/confirm_delete.html', {'muscle_group': muscle_group})
