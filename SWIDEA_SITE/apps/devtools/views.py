from django.shortcuts import render, redirect, get_object_or_404
from .models import Devtool
from .forms import DevtoolForm


def devtool_list(request):
    devtools = Devtool.objects.all()
    return render(request, 'devtools/devtool_list.html', {'devtools': devtools})


def devtool_detail(request, pk):
    devtool = get_object_or_404(Devtool, pk=pk)
    return render(request, 'devtools/devtool_detail.html', {'devtool': devtool})


def devtool_create(request):
    if request.method == 'POST':
        form = DevtoolForm(request.POST)
        if form.is_valid():
            devtool = form.save()
            return redirect('devtools:detail', pk=devtool.pk)
    else:
        form = DevtoolForm()
    return render(request, 'devtools/devtool_form.html', {'form': form})


def devtool_update(request, pk):
    devtool = get_object_or_404(Devtool, pk=pk)
    if request.method == 'POST':
        form = DevtoolForm(request.POST, instance=devtool)
        if form.is_valid():
            form.save()
            return redirect('devtools:detail', pk=devtool.pk)
    else:
        form = DevtoolForm(instance=devtool)
    return render(request, 'devtools/devtool_form.html', {'form': form})


def devtool_delete(request, pk):
    devtool = get_object_or_404(Devtool, pk=pk)
    devtool.delete()
    return redirect('devtools:list')
