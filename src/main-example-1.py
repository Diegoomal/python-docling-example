from docling.document_converter import DocumentConverter

def main():
    source = "https://arxiv.org/pdf/2408.09869"
    converter = DocumentConverter()
    doc = converter.convert(source).document
    print(doc.export_to_markdown())

if __name__ == "__main__":
    main()
