import numpy as np
import pandas as pd


ATTEMPTED = 15

CORRECT_VALUES = range(0, ATTEMPTED + 1)

LEARNING_RATES = np.arange(0.1, 1.0, 0.1)

OLD_MASTERY_VALUES = np.arange(0.0, 1.01, 0.1)


def calculate_accuracy(correct, attempted):
    if attempted <= 0:
        return 0.0

    return correct / attempted


def update_mastery(old_mastery, performance, learning_rate):

    new_mastery = old_mastery + learning_rate * (
        performance - old_mastery
    )

    return max(0.0, min(1.0, new_mastery))


results = []


for correct in CORRECT_VALUES:

    performance = calculate_accuracy(
        correct,
        ATTEMPTED
    )

    for learning_rate in LEARNING_RATES:

        for old_mastery in OLD_MASTERY_VALUES:

            new_mastery = update_mastery(
                old_mastery,
                performance,
                learning_rate
            )

            mastery_change = new_mastery - old_mastery

            results.append({
                "attempted": ATTEMPTED,
                "correct": correct,
                "performance": round(performance, 4),
                "learning_rate": round(learning_rate, 1),
                "old_mastery": round(old_mastery, 1),
                "new_mastery": round(new_mastery, 4),
                "mastery_change": round(mastery_change, 4)
            })


df = pd.DataFrame(results)


print("\nTOTAL SIMULATIONS")
print(len(df))


print("\nFIRST 20 RESULTS")
print(df.head(20).to_string(index=False))


print("\nSUMMARY")
print(
    df[
        [
            "performance",
            "learning_rate",
            "old_mastery",
            "new_mastery",
            "mastery_change"
        ]
    ].describe()
)


output_file = "data/mastery_simulation.csv"

df.to_csv(
    output_file,
    index=False
)

print(
    f"\nSimulation saved to: {output_file}"
)


