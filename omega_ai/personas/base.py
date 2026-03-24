"""Base Persona – foundation for every OMEGA AI platform persona."""

from __future__ import annotations

import json
import math
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class EvolutionState:
    """Tracks how far a persona has evolved."""

    generation: int = 0
    score: float = 1.0          # starts at 1, grows without bound
    insights: list[str] = field(default_factory=list)
    timestamp: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def advance(self, delta: float = 1.0) -> None:
        """Move one evolution step forward."""
        self.generation += 1
        # Logarithmic growth ensures score always increases towards ∞
        self.score += math.log1p(delta * self.generation)
        self.timestamp = datetime.now(timezone.utc).isoformat()

    def to_dict(self) -> dict[str, Any]:
        return {
            "generation": self.generation,
            "score": round(self.score, 4),
            "insights": self.insights,
            "timestamp": self.timestamp,
        }


class BasePersona(ABC):
    """Abstract base class shared by all five OMEGA AI personas."""

    #: Override in subclasses – the social-media platform this persona serves.
    PLATFORM: str = "Unknown"

    def __init__(self) -> None:
        self.state = EvolutionState()
        self._strategy: dict[str, Any] = {}

    # ------------------------------------------------------------------
    # Abstract interface every persona must implement
    # ------------------------------------------------------------------

    @abstractmethod
    def analyze_trends(self) -> list[str]:
        """Return a list of current platform-specific trends."""

    @abstractmethod
    def generate_content_strategy(self) -> dict[str, Any]:
        """Return an actionable content/feature strategy for the platform."""

    @abstractmethod
    def suggest_improvements(self) -> list[str]:
        """Return platform evolution suggestions."""

    # ------------------------------------------------------------------
    # Shared behaviour
    # ------------------------------------------------------------------

    def evolve(self, cycles: int = 1) -> None:
        """Run *cycles* evolution steps, collecting insights each time."""
        for _ in range(cycles):
            trends = self.analyze_trends()
            strategy = self.generate_content_strategy()
            improvements = self.suggest_improvements()

            insight = (
                f"[Gen {self.state.generation + 1}] "
                f"Trends: {len(trends)} | "
                f"Strategy keys: {list(strategy.keys())} | "
                f"Improvements: {len(improvements)}"
            )
            self.state.insights.append(insight)
            self.state.advance()
            self._strategy = strategy

    def status(self) -> dict[str, Any]:
        """Return a JSON-serialisable snapshot of the persona's current state."""
        return {
            "platform": self.PLATFORM,
            "evolution": self.state.to_dict(),
            "current_strategy": self._strategy,
        }

    def __repr__(self) -> str:  # pragma: no cover
        return (
            f"<{self.__class__.__name__} platform={self.PLATFORM!r} "
            f"generation={self.state.generation}>"
        )
