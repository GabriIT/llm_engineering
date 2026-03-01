from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

DEFAULT_SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".xlsx"}


@dataclass(slots=True)
class ParseConfig:
    knowledge_root: Path
    recursive: bool = True
    supported_extensions: set[str] = field(
        default_factory=lambda: set(DEFAULT_SUPPORTED_EXTENSIONS)
    )
    min_chars_pdf: int = 120
    min_chars_docx: int = 80
    min_chars_xlsx: int = 40
    strict_mode: bool = False

    def __post_init__(self) -> None:
        self.knowledge_root = Path(self.knowledge_root).expanduser().resolve()
        self.supported_extensions = {
            ext.lower() if ext.startswith(".") else f".{ext.lower()}"
            for ext in self.supported_extensions
        }

