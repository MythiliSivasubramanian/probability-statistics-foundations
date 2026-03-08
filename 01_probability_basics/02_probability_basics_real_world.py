"""
File: 02_probability_basics_real_world.py
Topic: Probability Basics with Real-World Examples (No user-defined functions)
"""


def print_divider(char = "_"):
    print("\n" + char * 78)


print_divider("_")
print("1) Core Idea: What Is Probability?")
print("Probability tells how likely an event is.")
print("Range: 0 (impossible) to 1 (certain)")
print("Formula (equally likely outcomes): P(E) _ favorable / total")


print_divider("_")
print("2) Coin Example (Simple and Foundational)")
sample_space_coin = ["H", "T"]
event_head = ["H"]
favorable = len(event_head)
total = len(sample_space_coin)
p_head = favorable / total
print(f"Sample space: {sample_space_coin}")
print(f"Event (getting Head): {event_head}")
print(f"P(Head) _ {favorable}/{total} _ {p_head:.2f}")


print_divider("_")
print("3) Die Example + Complement Rule")
sample_space_die = [1, 2, 3, 4, 5, 6]
event_even = [2, 4, 6]
favorable = len(event_even)
total = len(sample_space_die)
p_even = favorable / total
p_not_even = 1 - p_even
print(f"Sample space: {sample_space_die}")
print(f"Event (Even): {event_even}")
print(f"P(Even) _ {favorable}/{total} _ {p_even:.2f}")
print("Complement rule: P(not Even) _ 1 - P(Even)")
print(f"P(not Even) _ {p_not_even:.2f}")


print_divider("_")
print("4) Real-World Example: Weather Forecast")
print("Suppose weather app says P(rain tomorrow) _ 0.30")
rain_probability = 0.30
print(f"P(Rain) = {rain_probability:.2f}")
print(f"P(No Rain) = {1 - rain_probability:.2f}")


print_divider("_")
print("5) Real-World Example: Quality Check in Manufacturing")
print("A factory inspects one item from a lot. If 8 out of 200 are defective:")
defective = 8
total_items = 200
p_defective = defective / total_items
print(f"P(Defective) = {defective}/{total_items} _ {p_defective:.4f}")
print(f"P(Not Defective) = {1 - p_defective:.4f}")


print_divider("_")
print("6) Addition Rule (Mutually Exclusive Events)")
print("For one die roll:")
print("A = getting 1, B = getting 6")
print("P(A or B) = P(A) + P(B)")
p_one = 1 / 6
p_six = 1 / 6
p_one_or_six = p_one + p_six
print(f"P(1 or 6) = 1/6 + 1/6 = {p_one_or_six:.2f}")


print_divider("_")
print("7) Conditional Probability (Basic Intuition)")
print("Given that a drawn card is a face card, what is P(King)?")
print("In a standard deck: face cards are J, Q, K (12 total), Kings are 4.")
kings = 4
face_cards = 12
p_king_given_face = kings / face_cards
print(f"P(King | Face Card) = 4/12 = {p_king_given_face:.2f}")


print_divider("_")
print("8) Experimental vs Theoretical Probability")
print("Theoretical probability comes from math model.")
print("Experimental probability comes from actual observed data.")
tosses = [
    "H", "T", "H", "H", "T", "H", "T", "T", "H", "T",
    "H", "H", "T", "H", "T", "H", "H", "T", "H", "T"
]
heads_count = tosses.count("H")
tails_count = tosses.count("T")
p_head_exp = heads_count / len(tosses)
p_head_theory = 0.50
print(f"Observed tosses: {len(tosses)}")
print(f"Heads count: {heads_count}, Tails count: {tails_count}")
print(f"Experimental P(Head) = {p_head_exp:.2f}")
print(f"Theoretical P(Head) = {p_head_theory:.2f}")


print_divider("_")
print("9) Medical Screening (Important Real-World Caution)")
print("If a test has 95% sensitivity, it means:")
print("P(Test Positive | Person has disease) _ 0.95")
print("This is a conditional probability statement.")


print_divider("_")
print("10) Quick Recap")
print("1. Probability _ favorable / total (if outcomes are equally likely)")
print("2. Complement: P(not A) _ 1 - P(A)")
print("3. Mutually exclusive addition: P(A or B) _ P(A) + P(B)")
print("4. Conditional: P(A|B) means probability of A when B is already known")
print("5. Experimental probabilities approach theoretical values with more trials")
