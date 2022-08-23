from io import BytesIO

from django.http import FileResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View

from .colors import colors
from .schematic import Schematic


class IndexView(TemplateView):
    template_name = "index.html"
    
@method_decorator(csrf_exempt, name='dispatch')
class ConvertView(View):
    
    def get(self, request):
        return render(request, "convert.html", {"colors": colors})
    
    def post(self, request):
        new_colors = {}
        for color in colors:
            try:
                if request.POST[f"color_{color.id}"] == "on":
                    new_colors[color.base_color] = request.POST[f"color_{color.id}_block"]
            except:
                pass
        
        img = request.FILES["img"]
        palette = Schematic.get_palette(new_colors)
        edited_image = Schematic.edit_image(img, palette)
        schem = Schematic.generate(edited_image, new_colors)
        
        buffer = BytesIO()
        schem.save(buffer)
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename="mcmapmatic.litematic")

