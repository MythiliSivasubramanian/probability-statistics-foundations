"""
File        : coin_toss_probability_analysis.py

Scenario:
A fair coin is tossed 10 times. Outcomes are recorded as Heads (H) and Tails (T).

Objectives:
1. Count number of Heads and Tails from outcomes list
2. Calculate Experimental Probability
      P(Event) = Event Count / Total Trials
3. Compare Experimental Probability with
   Theoretical Probability of a fair coin

Concepts Covered:
- Outcome counting
- Frequency calculation
- Experimental probability
- Theoretical probability comparison

Note:
Experimental probability may differ from theoretical probability
due to small sample size randomness.
"""

"""
Scenario: Toss a fair coin 10 times.
outcomes recorded:  outcomes = ["H", "T", "H", "H", "T", "H", "T", "H", "H", "T"]
(H = Heads, T = Tails)
"""

"""
Task 1 — Count Outcomes. Find: Number of Heads and Number of Tails
"""

from collections import Counter

# outcomes prerecorded
outcomes = ["H", "T", "H", "H", "T", "H", "T", "H", "H", "T"]

# Count outcomes
outcomes_count = dict(Counter(outcomes))
print("\nHeads :", outcomes_count["H"])
print("\nTails :", outcomes_count["T"])

"""
Task 2 — Experimental Probability
Formula: P(Event) = Event Count / Total Trial 
So calculate: P(Heads) and P(Tails). Round to 2 decimals.
"""

# Experimental Probability. P(Event) = Event Count / Total Trial 
p_heads = outcomes_count["H"] / len(outcomes)
p_tails = outcomes_count["T"] / len(outcomes)

print(f"\nExperimental Probability :\nP_Heads : {p_heads:.2f}\nP_Tails : {p_tails:.2f}") # Round to 2 decimals

"""
Task 3 — Compare With Theoretical Probability
For a fair coin: P(Heads) = 0.50. P(Tails) = 0.50
Print comparison like:

Experimental P(Heads) : 0.60
Theoretical P(Heads)  : 0.50

"""
theo_p_heads = 0.50
theo_p_tails = 0.50

print("\nComparision between  Theoretical Probability and Experimental Probability :")
print(f"Theoretical Probability P_Heads : {theo_p_heads:.2f}\nExperimental Probability P_Heads {p_heads:.2f}")
print(f"\nTheoretical Probability P_Tails {theo_p_tails:.2f}\nExperimental Probability P_Tails {p_tails:.2f}")