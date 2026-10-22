"""Document formatting constants — canonical visual identity system.

All generated documents (resumes, cover letters, analyses, interview prep)
use this unified color and typography system. The navy color is standardized
to #17365D across all document types (per design decision 2026-10-10).
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class ColorPalette:
    NAVY: str = '#17365D'              # Deep navy — headings, name, separators, section titles
    LIGHT_BLUE: str = '#5B9BD5'        # Light blue — role line, employer/client accents
    BODY_TEXT: str = '#1F1F1F'         # Dark charcoal — body text
    SECONDARY_TEXT: str = '#4F4F4F'    # Medium gray — secondary/descriptive text
    SECTION_GREEN: str = '#008000'     # Green — subsection titles in analysis/interview docs
    ACCENT_ORANGE: str = '#C00000'     # Blood orange — bold items in analysis/interview docs
    WHITE: str = '#FFFFFF'             # Page background

@dataclass(frozen=True)
class Typography:
    # Font families
    HEADING_FONT: str = 'Cambria'
    BODY_FONT: str = 'Times New Roman'
    
    # Sizes (in points)
    NAME_SIZE: float = 20.0
    ROLE_LINE_SIZE: float = 11.0
    CONTACT_SIZE: float = 9.0
    SECTION_HEADING_SIZE: float = 12.0
    BODY_SIZE: float = 10.0
    SKILLS_SIZE: float = 9.25        # 9-9.5pt range
    ROLE_TITLE_SIZE: float = 10.75   # 10.5-11pt range
    
    # Spacing
    LINE_SPACING: float = 1.0
    SECTION_SPACE_BEFORE: float = 10.0  # ~9-11pt
    SECTION_SPACE_AFTER: float = 4.0    # ~3-5pt

@dataclass(frozen=True) 
class PageLayout:
    # Margins in inches
    TOP_MARGIN: float = 0.5
    BOTTOM_MARGIN: float = 0.5
    LEFT_MARGIN: float = 0.62
    RIGHT_MARGIN: float = 0.62
    SEPARATOR_WIDTH: float = 1.0  # pt

# Singleton instances
COLORS = ColorPalette()
FONTS = Typography()
LAYOUT = PageLayout()
