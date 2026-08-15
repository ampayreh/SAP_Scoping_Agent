# Tools

Post-processing utilities for the SAP S/4HANA Scoping Agent.

## proposal-to-pdf.py

Converts Skill 04 (Executive Proposal Drafter) markdown output into a professionally styled PDF with McKinsey-grade formatting: cover page, table of contents, page numbers, consulting-firm typography, and styled tables.

### Setup

```bash
cd sap-s4hana-scoping-agent

# Create virtual environment
python3 -m venv tools/.venv
source tools/.venv/bin/activate

# Install dependencies
pip install weasyprint markdown

# macOS system dependencies (if not already installed)
brew install pango cairo glib
```

### Usage

```bash
# Activate the virtual environment
source tools/.venv/bin/activate

# Basic usage — generates PDF in the same directory as the input
python3 tools/proposal-to-pdf.py benchmarks/scenario-a-agribusiness/skill-04-output.md

# Custom output path
python3 tools/proposal-to-pdf.py skill-04-output.md -o ~/Desktop/HHE-Proposal.pdf

# Override metadata
python3 tools/proposal-to-pdf.py skill-04-output.md --client "Acme Corp" --date "March 2026"

# Skip cover page and/or table of contents
python3 tools/proposal-to-pdf.py skill-04-output.md --no-cover --no-toc

# Custom CSS stylesheet
python3 tools/proposal-to-pdf.py skill-04-output.md -s path/to/custom.css
```

### CLI Reference

| Argument | Description |
|---|---|
| `input` | Path to Skill 04 markdown output file (required) |
| `--output`, `-o` | Output PDF path (default: input filename with .pdf extension) |
| `--style`, `-s` | Path to CSS stylesheet (default: `tools/proposal-style.css`) |
| `--no-cover` | Skip cover page generation |
| `--no-toc` | Skip table of contents generation |
| `--client` | Override client name for cover page |
| `--date` | Override date for cover page |
| `--title` | Override document title |

### What the PDF Includes

- Professional cover page with accent bar, title, client name, and confidentiality notice
- Auto-generated table of contents with page numbers
- Page numbers in footer, "Confidential" marker, running header
- Dark blue (#003366) section headers with underlines
- Styled tables with dark blue header rows and alternating row shading
- Blockquote callout boxes with blue accent border
- Page breaks between major sections
- Georgia serif body text / Helvetica Neue sans-serif headers

### Customization

Edit `proposal-style.css` to adjust colors, fonts, spacing, or page layout. Key variables to change:

- `#003366` — primary brand color (headers, accent bar, table headers)
- `Georgia` — body font family
- `Helvetica Neue` — header font family
- `10.5pt` — base body font size
- `letter` — page size (change to `A4` for international format)
