import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from plano.forms import TopicoForm
from plano.models import Topico

@pytest.mark.django_db
class TestTopicoForm:
    def test_topico_form_valid(self):
        form_data = {
            'subtitulo': 'Subtítulo do Tópico',
            'texto': 'Texto do tópico',
        }
        file_data = {
            'arquivo_pdf': SimpleUploadedFile('file.pdf', b'file_content', content_type='application/pdf'),
        }
        form = TopicoForm(data=form_data, files=file_data)
        assert form.is_valid()

    def test_topico_form_invalid(self):
        form_data = {
            'subtitulo': 'Subtítulo do Tópico',
            'texto': '', 
        }
        form = TopicoForm(data=form_data)
        assert not form.is_valid()
