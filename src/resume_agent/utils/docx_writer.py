"""Native OpenXML DOCX generator using Python standard library (zipfile + xml.etree).

Creates Microsoft Word (.docx) files with:
- Navy #17365D title and section headings
- Light blue #5B9BD5 accents and role bar shading #EBF1F5
- Real hyperlinked text for LinkedIn and AI Guardians portal
- Clean single-column ATS typography
"""
import html
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Dict, Tuple

CONTENT_TYPES_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>"""

RELS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

STYLES_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault>
      <w:rPr>
        <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
        <w:sz w:val="20"/>
        <w:color w:val="1F1F1F"/>
      </w:rPr>
    </w:rPrDefault>
  </w:docDefaults>
</w:styles>"""

def create_docx(
    filename: Path,
    paragraphs: List[Dict]
) -> Path:
    """Create a native .docx file from structured paragraph data.

    Paragraph dict format:
    {
        "text_runs": [
            {"text": "...", "bold": True, "color": "17365D", "size": 36, "url": "https://..."},
            ...
        ],
        "align": "left" | "center",
        "bg_color": "EBF1F5",  # optional shading for role bars
        "bottom_border": True, # optional bottom border rule
        "space_before": 120,   # twips (1/20 of a pt)
        "space_after": 60
    }
    """
    filename = Path(filename)
    filename.parent.mkdir(parents=True, exist_ok=True)

    # Collect all hyperlinks for document.xml.rels
    hyperlinks: List[Tuple[str, str]] = []  # (rId, url)
    link_counter = 1

    # Build word/document.xml
    doc_xml_lines = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">',
        '  <w:body>'
    ]

    for p in paragraphs:
        align = p.get("align", "left")
        bg_color = p.get("bg_color")
        bottom_border = p.get("bottom_border", False)
        space_before = p.get("space_before", 0)
        space_after = p.get("space_after", 60)

        p_pr = ['<w:pPr>']
        if align == "center":
            p_pr.append('<w:jc w:val="center"/>')
        p_pr.append(f'<w:spacing w:before="{space_before}" w:after="{space_after}" w:line="240" w:lineRule="auto"/>')

        left_indent = p.get("left_indent")
        hanging_indent = p.get("hanging_indent")
        if left_indent is not None or hanging_indent is not None:
            ind_attrs = []
            if left_indent is not None:
                ind_attrs.append(f'w:left="{left_indent}"')
            if hanging_indent is not None:
                ind_attrs.append(f'w:hanging="{hanging_indent}"')
            p_pr.append(f'<w:ind {" ".join(ind_attrs)}/>')

        if bg_color:
            p_pr.append(f'<w:shd w:val="clear" w:color="auto" w:fill="{bg_color}"/>')

        if bottom_border:
            p_pr.append('<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="4" w:color="17365D"/></w:pBdr>')

        p_pr.append('</w:pPr>')

        doc_xml_lines.append(f'    <w:p>{"".join(p_pr)}')

        for run in p.get("text_runs", []):
            text = run.get("text", "")
            bold = run.get("bold", False)
            italic = run.get("italic", False)
            color = run.get("color", "1F1F1F")
            size = run.get("size", 20)  # half-points (20 = 10pt)
            font = run.get("font")
            url = run.get("url")

            r_pr = ['<w:rPr>']
            if font:
                r_pr.append(f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}"/>')
            if bold:
                r_pr.append('<w:b/>')
            if italic:
                r_pr.append('<w:i/>')
            if color:
                r_pr.append(f'<w:color w:val="{color}"/>')
            r_pr.append(f'<w:sz w:val="{size}"/>')
            if url:
                r_pr.append('<w:u w:val="single"/>')
            r_pr.append('</w:rPr>')
            escaped_text = html.escape(text)
            r_html = f'<w:r>{"".join(r_pr)}<w:t xml:space="preserve">{escaped_text}</w:t></w:r>'

            if url:
                r_id = f"rIdHyperlink{link_counter}"
                link_counter += 1
                hyperlinks.append((r_id, url))
                doc_xml_lines.append(f'<w:hyperlink r:id="{r_id}">{r_html}</w:hyperlink>')
            else:
                doc_xml_lines.append(r_html)

        doc_xml_lines.append('    </w:p>')

    top_margin = 720  # 0.50 inch
    bottom_margin = 720
    left_margin = 893  # 0.62 inch
    right_margin = 893
    doc_xml_lines.append('    <w:sectPr>')
    doc_xml_lines.append('      <w:pgSz w:w="12240" w:h="15840"/>')
    doc_xml_lines.append(f'      <w:pgMar w:top="{top_margin}" w:right="{right_margin}" w:bottom="{bottom_margin}" w:left="{left_margin}" w:header="720" w:footer="720" w:gutter="0"/>')
    doc_xml_lines.append('    </w:sectPr>')
    doc_xml_lines.append('  </w:body>')
    doc_xml_lines.append('</w:document>')
    document_xml = "\n".join(doc_xml_lines)

    # Build word/_rels/document.xml.rels
    doc_rels_lines = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    ]
    for r_id, url in hyperlinks:
        doc_rels_lines.append(
            f'  <Relationship Id="{r_id}" '
            f'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink" '
            f'Target="{url}" TargetMode="External"/>'
        )
    doc_rels_lines.append('</Relationships>')
    doc_rels_xml = "\n".join(doc_rels_lines)

    # Write Zip Archive
    with zipfile.ZipFile(filename, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", CONTENT_TYPES_XML)
        zf.writestr("_rels/.rels", RELS_XML)
        zf.writestr("word/document.xml", document_xml)
        zf.writestr("word/_rels/document.xml.rels", doc_rels_xml)
        zf.writestr("word/styles.xml", STYLES_XML)

    return filename
