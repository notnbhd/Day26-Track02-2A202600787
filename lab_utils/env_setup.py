"""Load .env từ project root — dùng cho mọi agent (orchestrator + A2A specialists)."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = PROJECT_ROOT / ".env"


def load_lab_env() -> None:
    """Nạp DEEPSEEK_API_KEY và biến lab từ .env (idempotent)."""
    load_dotenv(ENV_FILE)
    # Tắt Vertex AI — dùng DeepSeek qua LiteLLM thay Gemini
    os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "FALSE")


def require_api_key() -> None:
    """Raise sớm nếu thiếu API key (tránh lỗi khó hiểu lúc gọi model)."""
    load_lab_env()
    if not os.getenv("DEEPSEEK_API_KEY"):
        raise RuntimeError(
            f"Thiếu DEEPSEEK_API_KEY. Đặt trong {ENV_FILE} — "
            "lấy key tại https://platform.deepseek.com/api_keys"
        )
