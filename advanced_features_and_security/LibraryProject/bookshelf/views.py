from django.shortcuts import render
from django.auth.decorator import permission_required
from django.shortcuts import get_object_or_404, redirect,render
from .models import Vlogs
from .forms import VlogForm
from django.views.generic.list import ListView

# Create your views here.
# List view — anyone with can_view permission can see
class VlogListView(ListView):
    model = Vlogs
    template_name = 'bookshelf/vlog_list.html'
    context_object_name = 'vlogs'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('bookshelf.can_view'):
            return render(request, 'bookshelf/permission_denied.html')
        return super().dispatch(request, *args, **kwargs)
    
#create view — only users with add_vlog permission can add
@permission_required('bookshelf.add_vlog', raise_exception=True)
def add_vlog(request):
    if request.method == 'POST':
        form = VlogForm(request.POST)
        if form .is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = VlogForm()
    return render(request, 'bookshelf/add_vlog.html', {'form': form})

#edit view — only users with edit-vlog permission can edit
@permission_required('bookshelf.edit_vlog', raise_exception=True)
def edit_vlog(request, vlog_id):
    vlog = get_object_or_404(Vlogs, id=vlog_id)
    if request.method == 'POST':
        form = VlogForm(request.POST, instance=vlog)
        if form.is_valid():
            form.save()
            return redirect('vlog-list')
    else:
        form = VlogForm(instance=vlog)
    return render(request, 'bookshelf/edit_vlog.html', {'form': form})

#delte view — only users with delete_vlog permission can delete
@permission_required('bookshelf.delete_vlog', raise_exception=True)
def delete_vlog(request, vlog_id):      
    vlog = get_object_or_404(Vlogs, id=vlog_id)
    if request.method == 'POST':
        vlog.delete()
        return redirect('vlog-list')
    return render(request, 'bookshelf/confirm_delete.html', {'vlog': vlog})