import os
import io
from datetime import datetime
from docxtpl import DocxTemplate

from django.http import HttpResponse
from django.views import View
from django.conf import settings




# Create your views here.
class GenerateDocumentView(View):
    def get(self, request):
        # Load template
        template_path = os.path.join(settings.BASE_DIR, 'static', 'template.docx')
        doc = DocxTemplate(template_path)
        
        # Prepare context with dynamic data
        context = {
            'company_name': 'Example Corp',
            'date': datetime.now().strftime("%d %B, %Y"),
            'customer': {
                'name': 'John Doe',
                'address': '123 Main Street',
                'city': 'New York',
                'email': 'john@example.com',
            },
            'items': [
                {'name': 'Product A', 'price': '$100', 'quantity': 2},
                {'name': 'Product B', 'price': '$85', 'quantity': 1},
                {'name': 'Product C', 'price': '$45', 'quantity': 3},
            ],
            'total': '$505',
        }
        
        # Render the template with context
        doc.render(context)
        
        # Save the generated document to a BytesIO buffer
        buffer = io.BytesIO()
        doc.save(buffer)
        buffer.seek(0)
        
        # Create the HTTP response with the document
        response = HttpResponse(
            buffer.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        response['Content-Disposition'] = 'attachment; filename=generated_document.docx'
        
        return response