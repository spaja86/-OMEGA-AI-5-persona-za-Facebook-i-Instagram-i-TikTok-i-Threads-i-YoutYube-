"""Tests for OMEGA AI – five social-media personas and orchestrator."""

from __future__ import annotations

import math
import pytest

from omega_ai import OmegaAI
from omega_ai.personas import (
    FacebookPersona,
    InstagramPersona,
    TikTokPersona,
    ThreadsPersona,
    YouTubePersona,
)
from omega_ai.personas.base import BasePersona, EvolutionState


# ---------------------------------------------------------------------------
# EvolutionState
# ---------------------------------------------------------------------------

class TestEvolutionState:
    def test_initial_state(self):
        state = EvolutionState()
        assert state.generation == 0
        assert state.score == 1.0
        assert state.insights == []

    def test_advance_increments_generation(self):
        state = EvolutionState()
        state.advance()
        assert state.generation == 1

    def test_advance_increases_score(self):
        state = EvolutionState()
        original_score = state.score
        state.advance()
        assert state.score > original_score

    def test_score_grows_unbounded(self):
        state = EvolutionState()
        for _ in range(100):
            state.advance()
        assert state.score > 1.0
        assert math.isfinite(state.score)

    def test_to_dict_keys(self):
        state = EvolutionState()
        d = state.to_dict()
        assert set(d.keys()) == {"generation", "score", "insights", "timestamp"}


# ---------------------------------------------------------------------------
# Individual personas
# ---------------------------------------------------------------------------

PERSONA_PARAMS = [
    (FacebookPersona, "Facebook"),
    (InstagramPersona, "Instagram"),
    (TikTokPersona, "TikTok"),
    (ThreadsPersona, "Threads"),
    (YouTubePersona, "YouTube"),
]


@pytest.mark.parametrize("PersonaClass, name", PERSONA_PARAMS)
class TestPersonas:
    def test_platform_attribute(self, PersonaClass, name):
        persona = PersonaClass()
        assert persona.PLATFORM == name

    def test_is_base_persona(self, PersonaClass, name):
        persona = PersonaClass()
        assert isinstance(persona, BasePersona)

    def test_analyze_trends_returns_list(self, PersonaClass, name):
        persona = PersonaClass()
        trends = persona.analyze_trends()
        assert isinstance(trends, list)
        assert len(trends) > 0

    def test_generate_content_strategy_returns_dict(self, PersonaClass, name):
        persona = PersonaClass()
        strategy = persona.generate_content_strategy()
        assert isinstance(strategy, dict)
        assert len(strategy) > 0

    def test_suggest_improvements_returns_list(self, PersonaClass, name):
        persona = PersonaClass()
        improvements = persona.suggest_improvements()
        assert isinstance(improvements, list)
        assert len(improvements) > 0

    def test_evolve_advances_generation(self, PersonaClass, name):
        persona = PersonaClass()
        persona.evolve(cycles=2)
        assert persona.state.generation == 2

    def test_evolve_populates_insights(self, PersonaClass, name):
        persona = PersonaClass()
        persona.evolve(cycles=3)
        assert len(persona.state.insights) == 3

    def test_status_contains_platform(self, PersonaClass, name):
        persona = PersonaClass()
        status = persona.status()
        assert status["platform"] == name
        assert "evolution" in status
        assert "current_strategy" in status


# ---------------------------------------------------------------------------
# OmegaAI orchestrator
# ---------------------------------------------------------------------------

class TestOmegaAI:
    def test_has_five_personas(self):
        omega = OmegaAI()
        assert len(omega.personas) == 5

    def test_all_platforms_present(self):
        omega = OmegaAI()
        assert set(omega.personas.keys()) == {
            "Facebook", "Instagram", "TikTok", "Threads", "YouTube"
        }

    def test_evolve_advances_all(self):
        omega = OmegaAI()
        omega.evolve(cycles=4)
        for persona in omega.personas.values():
            assert persona.state.generation == 4

    def test_evolve_invalid_cycles_raises(self):
        omega = OmegaAI()
        with pytest.raises(ValueError):
            omega.evolve(cycles=0)

    def test_status_returns_all_platforms(self):
        omega = OmegaAI()
        status = omega.status()
        assert set(status.keys()) == {
            "Facebook", "Instagram", "TikTok", "Threads", "YouTube"
        }

    def test_report_is_valid_json(self):
        import json
        omega = OmegaAI()
        omega.evolve(cycles=1)
        report = omega.report()
        parsed = json.loads(report)
        assert "omega_ai_version" in parsed
        assert "platforms" in parsed

    def test_platform_returns_correct_type(self):
        omega = OmegaAI()
        assert isinstance(omega.platform("Facebook"), FacebookPersona)
        assert isinstance(omega.platform("Instagram"), InstagramPersona)
        assert isinstance(omega.platform("TikTok"), TikTokPersona)
        assert isinstance(omega.platform("Threads"), ThreadsPersona)
        assert isinstance(omega.platform("YouTube"), YouTubePersona)

    def test_platform_unknown_raises_key_error(self):
        omega = OmegaAI()
        with pytest.raises(KeyError):
            omega.platform("Twitter")
