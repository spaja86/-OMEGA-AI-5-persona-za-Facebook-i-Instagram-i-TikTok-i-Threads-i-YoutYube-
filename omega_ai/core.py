"""OMEGA AI core orchestrator – manages all five social-media personas."""

from __future__ import annotations

import json
from typing import Any

from .personas import (
    FacebookPersona,
    InstagramPersona,
    TikTokPersona,
    ThreadsPersona,
    YouTubePersona,
)


class OmegaAI:
    """Orchestrates five OMEGA AI personas, one per social-media platform.

    Each persona independently analyses its platform, generates a strategy,
    and suggests improvements.  Calling :meth:`evolve` advances every persona
    by the requested number of evolution cycles, driving all platforms towards
    infinite improvement.

    Example::

        from omega_ai import OmegaAI

        omega = OmegaAI()
        omega.evolve(cycles=3)
        print(omega.report())
    """

    VERSION = "1.0.0"

    def __init__(self) -> None:
        self.personas = {
            "Facebook": FacebookPersona(),
            "Instagram": InstagramPersona(),
            "TikTok": TikTokPersona(),
            "Threads": ThreadsPersona(),
            "YouTube": YouTubePersona(),
        }

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def evolve(self, cycles: int = 1) -> None:
        """Advance all five personas by *cycles* evolution steps."""
        if cycles < 1:
            raise ValueError("cycles must be >= 1")
        for persona in self.personas.values():
            persona.evolve(cycles=cycles)

    def status(self) -> dict[str, Any]:
        """Return the current evolution state for every persona."""
        return {
            name: persona.status()
            for name, persona in self.personas.items()
        }

    def report(self, indent: int = 2) -> str:
        """Return a pretty-printed JSON report of all personas."""
        return json.dumps(
            {
                "omega_ai_version": self.VERSION,
                "platforms": self.status(),
            },
            indent=indent,
            ensure_ascii=False,
        )

    def platform(self, name: str):
        """Return the persona for the given platform name.

        :param name: One of ``"Facebook"``, ``"Instagram"``, ``"TikTok"``,
            ``"Threads"``, or ``"YouTube"`` (case-sensitive).
        :raises KeyError: If *name* is not a recognised platform.
        """
        if name not in self.personas:
            raise KeyError(
                f"{name!r} is not a recognised platform. "
                f"Choose from: {list(self.personas)}"
            )
        return self.personas[name]

    def __repr__(self) -> str:  # pragma: no cover
        gens = {
            name: p.state.generation for name, p in self.personas.items()
        }
        return f"<OmegaAI v{self.VERSION} generations={gens}>"
