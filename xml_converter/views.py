
from django.http import JsonResponse
from django.shortcuts import render

from .forms import UploadFileForm
from .utils import convert_xml_to_json, ParseException


def upload_page(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                data = convert_xml_to_json(request.FILES['file'])
                return JsonResponse(data)
            except ParseException as e:
                form.add_error('file', e)
    else:
        form = UploadFileForm()
    return render(request, 'upload_page.html', {'form': form})
