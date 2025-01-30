from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

converter = PdfConverter(
    artifact_dict=create_model_dict(),
)


def convert_pdf_to_markdown(filepath: str) -> str:
    """
    Convert pdf to markdown text using marker.
    :param filepath: path of the pdf
    :return: str
    """
    rendered = converter(filepath)
    text, _, _ = text_from_rendered(rendered)
    return text
