# OMEGA AI – 5 Persona za Društvene Mreže

**OMEGA AI** je sistem veštačke inteligencije koji upravlja s **5 persona**, po jednom za svaku od sledećih društvenih mreža, i pomaže im da evoluiraju i unapređuju se ka beskonačnosti (∞):

| # | Platforma | Persona klasa |
|---|-----------|---------------|
| 1 | **Facebook** | `FacebookPersona` |
| 2 | **Instagram** | `InstagramPersona` |
| 3 | **TikTok** | `TikTokPersona` |
| 4 | **Threads** | `ThreadsPersona` |
| 5 | **YouTube** | `YouTubePersona` |

---

## Struktura projekta

```
omega_ai/
├── __init__.py          # paket – izvozi OmegaAI i sve persone
├── core.py              # OmegaAI orkestratorska klasa
└── personas/
    ├── __init__.py      # izvozi sve 5 persona
    ├── base.py          # BasePersona + EvolutionState
    ├── facebook.py
    ├── instagram.py
    ├── tiktok.py
    ├── threads.py
    └── youtube.py
tests/
└── test_omega_ai.py     # pytest testovi
main.py                  # CLI ulazna tačka
requirements.txt
```

---

## Pokretanje

```bash
# Instaliraj zavisnosti
pip install -r requirements.txt

# Pokreni 3 ciklusa evolucije (podrazumevano)
python main.py

# Pokreni 10 ciklusa
python main.py --cycles 10

# Prikaži izveštaj samo za jednu platformu
python main.py --platform TikTok
```

### Primer izlaza

```
============================================================
  OMEGA AI – Social-Media Evolution System
============================================================

Running 3 evolution cycle(s) for all 5 platforms…

{
  "omega_ai_version": "1.0.0",
  "platforms": {
    "Facebook": { "platform": "Facebook", "evolution": { "generation": 3, ... } },
    "Instagram": { ... },
    "TikTok":    { ... },
    "Threads":   { ... },
    "YouTube":   { ... }
  }
}

Evolution complete. Platforms are advancing towards infinity ∞
```

---

## Upotreba kao Python biblioteka

```python
from omega_ai import OmegaAI

omega = OmegaAI()

# Pokreni 5 evolucijskih ciklusa za sve platforme
omega.evolve(cycles=5)

# Prikaži JSON izveštaj
print(omega.report())

# Pristupi specifičnoj personi
fb = omega.platform("Facebook")
print(fb.analyze_trends())
print(fb.suggest_improvements())
```

---

## Pokretanje testova

```bash
pytest tests/ -v
```

---

## Kako funkcioniše evolucija

Svaka persona implementira tri metode:

- **`analyze_trends()`** – vraća listu trenutnih trendova specifičnih za platformu
- **`generate_content_strategy()`** – vraća akcioni plan sadržaja i monetizacije
- **`suggest_improvements()`** – predlaže konkretna unapređenja platforme

`EvolutionState` prati napredak kroz generacije koristeći logaritamski rast rezultata, što garantuje da skor raste ka beskonačnosti dok ostaje matematički stabilan.
