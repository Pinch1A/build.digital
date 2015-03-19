from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from digital.models import Field

class FieldForm(ModelForm):
    class Meta:
        model = Field
	fields = ('id', 'desc_text', 'price', 'stock_number', 'available_text')

def field_list(request, template_name='field/field_list.html'):
    fields = Field.objects.all()
    data = {}
    data['object_list'] = fields
    return render(request, template_name, data)

def field_create(request, template_name='field/field_new.html'):
    form = FieldForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('field_list')
    return render(request, template_name, {'form':form})

def field_edit(request, pk, template_name='field/field_edit.html'):
    field = get_object_or_404(Field, pk=pk)
    form = FieldForm(request.POST or None, instance=field)
    if form.is_valid():
        form.save()
        return redirect('field_list')
    return render(request, template_name, {'object':field, 'form':form})

def field_delete(request, pk, template_name='field/field_confirm_delete.html'):
    field = get_object_or_404(Field, pk=pk)    
    if request.method=='POST':
        field.delete()
        return redirect('field_list')
    return render(request, template_name, {'object':field})
