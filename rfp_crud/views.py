from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML

from rfp_crud.models.rfp_model import Rfp
from rfp_crud.forms.rfp_model_form import RfpModelForm

def index(request):
  return render(request, 'rfp_crud/index.html')

def rfp_show(request, id, template_name='rfp_crud/show.html'):
    rpf = get_object_or_404(Rfp, id=id)
    return render(request, template_name, {'object': rpf})

def rfp_list(request, template_name='rfp_crud/list.html'):
    posts = Rfp.objects.all()
    data = {}
    data['object_list'] = posts
    return render(request, template_name, data)

def rfp_list_pdf(request):
    object_list = Rfp.objects.all()
    html_string = render_to_string('rfp_crud/pdf_template.html', {'object_list': object_list})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/opportunities.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('opportunities.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="opportunities.pdf"'
        return response

    return response

def rfp_create(request, template_name='rfp_crud/form.html'):
    verify = verify_user(request)
    if  verify != 'pass':
        return verify

    form = RfpModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('rfp_crud:list')
    return render(request, template_name, {'form': form})

def rfp_update(request, id, template_name='rfp_crud/form.html'):
    verify = verify_user(request)
    if  verify != 'pass':
        return verify

    rpf = get_object_or_404(Rfp, id=id)
    form = RfpModelForm(request.POST or None, instance=rpf)
    if form.is_valid():
        form.save()
        return redirect('rfp_crud:list')
    return render(request, template_name, {'form': form})

def rfp_delete(request, id, template_name='rfp_crud/delete.html'):
    verify = verify_user(request)
    if  verify != 'pass':
        return verify

    rpf = get_object_or_404(Rfp, id=id)
    
    if request.method=='POST':
        rpf.delete()
        messages.success(request, 'Record deleted successfully.')
        return redirect('rfp_crud:list')
    return render(request, template_name)

def verify_user(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.WARNING, 'You need to login first')
        return redirect('/')
    return 'pass'