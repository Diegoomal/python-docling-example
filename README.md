# Docling PDF to Markdown Example | [this-repo](https://github.com/Diegoomal/python-docling-example)

Small Python project demonstrating how to use [Docling](https://www.docling.ai/) to convert PDF documents into Markdown.

The repository includes two examples:

- [src/main-example-1.py](./src/main-example-1.py): converts the Docling arXiv paper directly from its online PDF URL.
- [src/main-example-2.py](./src/main-example-2.py): reads a local PDF from [dataset/2408.09869v5.pdf](./dataset/2408.09869v5.pdf) and writes the extracted Markdown to `output/2408.09869v5.md`.

## Project Structure

```text
dataset/
  2408.09869v5.pdf
output/
  .gitkeep
src/
  main-example-1.py
  main-example-2.py
requirements.txt
env.yml
conda.md
```

## Setup

Create and activate the Conda environment:

```bash
conda env create -n docling-env -f ./env.yml
conda activate docling-env
```

If the environment already exists, update it with:

```bash
conda env update -n docling-env -f ./env.yml
```

More Conda snippets are available in [conda.md](./conda.md).

## Usage

Run the online PDF example:

```bash
python src/main-example-1.py
```

Run the local PDF to Markdown example:

```bash
python src/main-example-2.py
```

The local example writes the exported Markdown file to:

```text
output/2408.09869v5.md
```

## References

- [Docling website](https://www.docling.ai/)
- [Docling documentation](https://docling-project.github.io/docling/)
- [Docling arXiv paper](https://arxiv.org/pdf/2408.09869)
