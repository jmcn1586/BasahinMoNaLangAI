import fitz

def read_pdf(file):
    text = ''
    with fitz.open(stream=file.read(), filetype='pdf') as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()