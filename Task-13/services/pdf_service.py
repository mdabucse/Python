from weasyprint import HTML
from config import REPORT_DIR

def generate_pdf(html_content, filename):
    output_path = REPORT_DIR / filename
    HTML(string=html_content).write_pdf(output_path)
    return output_path