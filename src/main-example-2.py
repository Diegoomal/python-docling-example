from docling.document_converter import DocumentConverter
from pathlib import Path

def main():
    source = Path(__file__).resolve().parents[1] / "dataset" / "2408.09869v5.pdf"
    output_path = Path(__file__).resolve().parents[1] / "output" / f"{source.stem}.md"

    converter = DocumentConverter()
    doc = converter.convert(source).document
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(doc.export_to_markdown(), encoding="utf-8")

    print(f"Markdown salvo em: {output_path}")

if __name__ == "__main__":
    main()
