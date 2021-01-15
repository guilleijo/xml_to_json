from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import FileSerializer
from .utils import convert_xml_to_json, ParseException
from rest_framework.exceptions import ValidationError


class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        serializer = FileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file_obj = request.FILES['file']
        try:
            data = convert_xml_to_json(file_obj)
        except ParseException as e:
            raise ValidationError(e)
        return Response(data)
