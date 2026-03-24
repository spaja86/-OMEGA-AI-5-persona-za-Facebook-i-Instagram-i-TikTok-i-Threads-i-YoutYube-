"""omega_ai package – OMEGA AI social-media evolution system."""

from .core import OmegaAI
from .personas import (
    BasePersona,
    EvolutionState,
    FacebookPersona,
    InstagramPersona,
    TikTokPersona,
    ThreadsPersona,
    YouTubePersona,
)

__all__ = [
    "OmegaAI",
    "BasePersona",
    "EvolutionState",
    "FacebookPersona",
    "InstagramPersona",
    "TikTokPersona",
    "ThreadsPersona",
    "YouTubePersona",
]
