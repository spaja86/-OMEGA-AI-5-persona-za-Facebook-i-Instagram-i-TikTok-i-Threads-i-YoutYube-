"""Instagram Persona – OMEGA AI persona dedicated to Instagram."""

from __future__ import annotations

from typing import Any

from .base import BasePersona


class InstagramPersona(BasePersona):
    """OMEGA AI persona that evolves Instagram towards infinity.

    Focus areas: visual storytelling, Reels, Shopping, Collab posts,
    creator economy, and aesthetic-driven discovery.
    """

    PLATFORM = "Instagram"

    def analyze_trends(self) -> list[str]:
        return [
            "Reels dominating feed reach over static posts",
            "AI-generated filters and background effects going mainstream",
            "Instagram Shopping closing the discover-to-purchase gap",
            "Collab posts enabling dual-audience content exposure",
            "Behind-the-scenes Stories outperforming polished content",
            "Audio-first Reels leveraging trending sounds",
            "Close Friends lists expanding beyond Stories to posts",
        ]

    def generate_content_strategy(self) -> dict[str, Any]:
        return {
            "content_mix": {
                "reels": "40%",
                "carousel_posts": "25%",
                "stories": "20%",
                "static_posts": "10%",
                "live_streams": "5%",
            },
            "engagement_tactics": [
                "Use trending audio within first 48 hours of chart entry",
                "Post Collab Reels with complementary niche creators",
                "Create 'Save-worthy' carousel tutorials for evergreen reach",
                "Leverage question stickers to seed comment conversations",
            ],
            "monetisation": [
                "Product tags on Shopping-enabled posts",
                "Paid partnership labels with brand collaborations",
                "Subscriptions for exclusive Close-Friends content",
            ],
            "evolution_goal": (
                "Become the definitive visual discovery engine "
                "bridging creativity, commerce, and culture"
            ),
        }

    def suggest_improvements(self) -> list[str]:
        return [
            "Introduce a 'Creative Studio' with AI-assisted storyboarding",
            "Add multi-language auto-captions to Reels",
            "Enable direct affiliate linking on organic posts",
            "Build community 'Mood Boards' shared across accounts",
            "Launch a 'Collab Series' feature for episodic co-created content",
            "Surface detailed reach analytics for every Story frame",
            "Allow polls and quizzes inside Reels",
        ]
