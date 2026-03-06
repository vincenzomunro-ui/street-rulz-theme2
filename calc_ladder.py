#!/usr/bin/env python3
"""Calculate ladder standings after Round 5 and generate fair Round 6 schedule."""

# All match results Rounds 1-5
results = [
    # Round 1 - 5 Feb
    ("Headstart", 6, "Big Sexy FC", 12),
    ("School Run United", 5, "Spirit of Mawen", 14),  # R1 G2 was "Goal Truma Unit" but that's Spirit of Mawen (renamed)
    ("Spirit of Mawen", 9, "Third Leg Strikers", 7),
    # Round 2 - 12 Feb
    ("Headstart", 8, "School Run United", 5),
    ("Screaming Schooners", 5, "Third Leg Strikers", 9),
    ("Spirit of Mawen", 9, "Big Sexy FC", 7),
    # Round 3 - 19 Feb
    ("Headstart", 3, "Third Leg Strikers", 5),
    ("Big Sexy FC", 12, "School Run United", 6),
    ("Spirit of Mawen", 12, "Screaming Schooners", 5),
    # Round 4 - 26 Feb
    ("Big Sexy FC", 12, "Screaming Schooners", 8),
    ("School Run United", 4, "Headstart", 7),
    ("Spirit of Mawen", 7, "Third Leg Strikers", 10),
    # Round 5 - 5 Mar (from the screenshot)
    ("Headstart", 10, "Screaming Schooners", 9),
    ("Big Sexy FC", 8, "Third Leg Strikers", 7),
    ("Spirit of Mawen", 9, "School Run United", 13),
]

# Note: Round 1 Game 2 had "Goal Truma Unit" scoring 14 vs School Run United 5
# But Goal Truma Unit is not in the current 6-team roster. Looking at the data,
# it seems Spirit of Mawen played twice in R1 (G2 as "Goal Truma Unit" and G3).
# Let's recalculate using only the 6 known teams and the actual results.
# R1 G2: School Run United 5 vs Goal Truma Unit 14 - this team doesn't exist in ladder
# So Spirit of Mawen's R1 stats come from G3 only.
# Let's be precise and use what's in the fixture data.

teams = {
    "Big Sexy FC": {"p": 0, "w": 0, "d": 0, "l": 0, "gf": 0, "ga": 0},
    "Third Leg Strikers": {"p": 0, "w": 0, "d": 0, "l": 0, "gf": 0, "ga": 0},
    "Spirit of Mawen": {"p": 0, "w": 0, "d": 0, "l": 0, "gf": 0, "ga": 0},
    "Headstart": {"p": 0, "w": 0, "d": 0, "l": 0, "gf": 0, "ga": 0},
    "Screaming Schooners": {"p": 0, "w": 0, "d": 0, "l": 0, "gf": 0, "ga": 0},
    "School Run United": {"p": 0, "w": 0, "d": 0, "l": 0, "gf": 0, "ga": 0},
}

# Recalculate from actual fixture data (what's in the JSON)
actual_results = [
    # Round 1
    ("Headstart", 6, "Big Sexy FC", 12),
    ("School Run United", 5, "Screaming Schooners", 14),  # Wait, R1G2 was "Goal Truma Unit"
    ("Spirit of Mawen", 9, "Third Leg Strikers", 7),
    # Round 2
    ("Headstart", 8, "School Run United", 5),
    ("Screaming Schooners", 5, "Third Leg Strikers", 9),
    ("Spirit of Mawen", 9, "Big Sexy FC", 7),
    # Round 3
    ("Headstart", 3, "Third Leg Strikers", 5),
    ("Big Sexy FC", 12, "School Run United", 6),
    ("Spirit of Mawen", 12, "Screaming Schooners", 5),
    # Round 4
    ("Big Sexy FC", 12, "Screaming Schooners", 8),
    ("School Run United", 4, "Headstart", 7),
    ("Spirit of Mawen", 7, "Third Leg Strikers", 10),
    # Round 5
    ("Headstart", 10, "Screaming Schooners", 9),
    ("Big Sexy FC", 8, "Third Leg Strikers", 7),
    ("Spirit of Mawen", 9, "School Run United", 13),
]

# R1G2 was "Goal Truma Unit" not Screaming Schooners. Let me use the EXISTING ladder
# data (after R4) and just add R5 results on top.

# After Round 4 (from the current JSON):
teams = {
    "Big Sexy FC":        {"p": 4, "w": 3, "d": 0, "l": 1, "gf": 43, "ga": 29},
    "Third Leg Strikers": {"p": 4, "w": 3, "d": 0, "l": 1, "gf": 31, "ga": 24},
    "Spirit of Mawen":    {"p": 4, "w": 3, "d": 0, "l": 1, "gf": 37, "ga": 31},
    "Headstart":          {"p": 4, "w": 2, "d": 0, "l": 2, "gf": 24, "ga": 26},
    "Screaming Schooners":{"p": 4, "w": 0, "d": 0, "l": 4, "gf": 27, "ga": 38},
    "School Run United":  {"p": 4, "w": 0, "d": 0, "l": 4, "gf": 20, "ga": 34},
}

# Round 5 results:
r5 = [
    ("Headstart", 10, "Screaming Schooners", 9),
    ("Big Sexy FC", 8, "Third Leg Strikers", 7),
    ("Spirit of Mawen", 9, "School Run United", 13),
]

for home, hs, away, aws in r5:
    teams[home]["p"] += 1
    teams[away]["p"] += 1
    teams[home]["gf"] += hs
    teams[home]["ga"] += aws
    teams[away]["gf"] += aws
    teams[away]["ga"] += hs
    if hs > aws:
        teams[home]["w"] += 1
        teams[away]["l"] += 1
    elif aws > hs:
        teams[away]["w"] += 1
        teams[home]["l"] += 1
    else:
        teams[home]["d"] += 1
        teams[away]["d"] += 1

# Calculate points and goal diff
for name, t in teams.items():
    t["pts"] = t["w"] * 3 + t["d"] * 1
    t["gd"] = t["gf"] - t["ga"]

# Sort by points, then goal diff, then goals for
sorted_teams = sorted(teams.items(), key=lambda x: (-x[1]["pts"], -x[1]["gd"], -x[1]["gf"]))

print("=== LADDER AFTER ROUND 5 ===")
print(f"{'Pos':<4} {'Team':<22} {'P':<3} {'W':<3} {'D':<3} {'L':<3} {'GF':<4} {'GA':<4} {'GD':<5} {'PTS':<4}")
for i, (name, t) in enumerate(sorted_teams, 1):
    gd_str = f"+{t['gd']}" if t['gd'] > 0 else str(t['gd'])
    print(f"{i:<4} {name:<22} {t['p']:<3} {t['w']:<3} {t['d']:<3} {t['l']:<3} {t['gf']:<4} {t['ga']:<4} {gd_str:<5} {t['pts']:<4}")

# Generate Round 6 schedule
# Previous matchups:
# R1: Headstart vs Big Sexy, School Run vs ?, Spirit vs Third Leg
# R2: Headstart vs School Run, Screamers vs Third Leg, Spirit vs Big Sexy
# R3: Headstart vs Third Leg, Big Sexy vs School Run, Spirit vs Screamers
# R4: Big Sexy vs Screamers, School Run vs Headstart, Spirit vs Third Leg
# R5: Headstart vs Screamers, Big Sexy vs Third Leg, Spirit vs School Run

# Matchups so far (each pair):
# Headstart vs Big Sexy (R1), Headstart vs School Run (R2), Headstart vs Third Leg (R3)
# Headstart vs Headstart/School Run (R4 reverse), Headstart vs Screamers (R5)
# Big Sexy vs Spirit (R2), Big Sexy vs School Run (R3), Big Sexy vs Screamers (R4)
# Big Sexy vs Third Leg (R5)
# Spirit vs Third Leg (R1, R4), Spirit vs Screamers (R3), Spirit vs School Run (R5)
# Screamers vs Third Leg (R2)

# For Round 6, fair matchups (reverse of R1 essentially, or new combos):
# Teams that haven't played each other much:
# Headstart vs Spirit (not yet!)
# Big Sexy vs School Run (R3 only)
# Third Leg vs Screamers (R2 only)

print("\n=== ROUND 6 SCHEDULE (12 March) ===")
print("Game 1: Headstart vs Spirit of Mawen (Court 1, 6:30pm) - haven't played yet!")
print("Game 2: School Run United vs Big Sexy FC (Court 2, 6:30pm)")
print("Game 3: Third Leg Strikers vs Screaming Schooners (Court 3, 7:15pm)")
