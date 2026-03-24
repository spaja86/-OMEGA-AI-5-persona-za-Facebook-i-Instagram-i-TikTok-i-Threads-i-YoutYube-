"""TikTok Persona – OMEGA AI persona dedicated to TikTok."""

from __future__ import annotations

from typing import Any

from .base import BasePersona


class TikTokPersona(BasePersona):
    """OMEGA AI persona that evolves TikTok towards infinity.

    Focus areas: algorithm-driven discovery, viral short-form video,
    TikTok Shop, duets/stitches, sound trends, and LIVE commerce.
    """

    PLATFORM = "TikTok"

    def analyze_trends(self) -> list[str]:
        return [
            "For You Page (FYP) algorithm rewarding watch-time over followers",
            "LIVE shopping events driving record GMV for creators",
            "Duet / Stitch culture fuelling viral challenge loops",
            "Original audio becoming brand identity for creators",
            "Educational 'LearnTok' content competing with long-form media",
            "Series feature enabling episodic premium content",
            "Green-screen effect powering reaction and commentary genres",
        ]

    def generate_content_strategy(self) -> dict[str, Any]:
        return {
            "content_mix": {
                "short_form_video_under_60s": "50%",
                "medium_form_video_1_3min": "20%",
                "live_streams": "15%",
                "series_episodes": "10%",
                "photo_mode_carousels": "5%",
            },
            "engagement_tactics": [
                "Hook viewers in the first 1–2 seconds to maximise completion rate",
                "Participate in trending sounds within 24 hours of peak",
                "Respond to top comments with video replies",
                "Use Stitch to add value on viral topics in your niche",
            ],
            "monetisation": [
                "TikTok LIVE gifts and diamonds",
                "TikTok Shop affiliate commissions",
                "Creator Fund and Creativity Program Beta payouts",
                "Brand deals using TikTok Creator Marketplace",
            ],
            "evolution_goal": (
                "Become the fastest-evolving entertainment and commerce "
                "platform by closing the gap between discovery and purchase"
            ),
        }

    def suggest_improvements(self) -> list[str]:
        return [
            "Introduce AI co-pilot for real-time script suggestions while filming",
            "Build 'Trend Forecast' dashboard showing 72-hour emerging sounds",
            "Enable collaborative LIVE sessions with up to 6 creators",
            "Allow pre-scheduled TikTok Shop drops with countdown timers",
            "Expand Series monetisation to mid-tier creators",
            "Add granular audience demographic insights per video",
            "Launch a 'TikTok Academy' with platform-native creator education",
        ]
