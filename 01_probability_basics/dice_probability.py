"""
File name : dice_probability.
Topic: Dice Probability
Problem:  Roll a fair die 12 times.
Outcomes recorded as:
rolls = [1, 3, 5, 2, 6, 4, 3, 2, 5, 1, 6, 3]

Task 1 — Count Each Outcome
- Find how many times each number appeared.

Task 2 — Experimental Probability of Rolling a 3
Formula : P(3) = Count of 3 / Total rolls
Expected: 3 appears → 3 times. Total → 12
P(3) = 3 / 12 = 0.25
Round to 2 decimals.

Task 3 — Experimental Probability of Even Numbers
Even outcomes: 2, 4, 6
Count total even occurrences.
Then: P(Even) = Even count / Total rolls

Task 4 — Compare With Theoretical Probability
For a fair die:
Event	Theoretical Probability
Rolling 3	1/6 ≈ 0.17
Even number	3/6 = 0.50

Print comparison:
Experimental P(3) : 0.25
Theoretical P(3)  : 0.17


"""

from collections import Counter

# List of outcomes of a Dice roll of 12 times.
rolls = [1, 3, 5, 2, 6, 4, 3, 2, 5, 1, 6, 3]

# Count how many times each number appeared
numbers_count = dict(Counter(rolls))

print("\n\nDice Rolled 12 times:\nOutcomes and no of times:\n")
for k,v in numbers_count.items():
    print(k, "appears", v, "times")
    
# Experimental Probability of Rolling a 3
print("\n\nExperimental Probability of Rolling a 3")
print("-" * 50)
p_3 = numbers_count[3] / len(rolls) 
print("Number 3 occured", numbers_count[3], "times out of", len(rolls), "dice rolls")
print(f"Probability of Number 3 is : {p_3:.2f}") # Round to 2 decimals
print("-" * 50)

# Experimental Probability of Even Numbers

# Count total number of even_outcomes
even_outcomes_count = 0
for k,v in numbers_count.items():
    if k % 2 == 0:
        even_outcomes_count += v
print("\nTotal no of times of even occurances(2,4,6) :", even_outcomes_count)
#  P(Even) = Even count / Total rolls
p_even = even_outcomes_count / len(rolls)
print(f"Experimental Probability of Even Numbers : {p_even:.2f}")
print("-" * 50)

# Compare With Theoretical Probability
"""
For a fair die:
Event	Theoretical Probability
Rolling 3	(1/6 ) ≈ 0.17 (Theoritical Probability of rolling 1 times vs 12 times same)
Even number	(3/6)  = 0.50 
"""
print("\nComparision between Theoretical and Experimental Probability")
print("-" * 60)
print(f"Probability of Number 3 :\nTheoretical : 0.17\nExperimental {p_3}\n\nProbability of Even Numbers : \nTheoretical : 0.50\nExperimental : {p_even:.2f}\n\n")