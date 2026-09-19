from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------------
# Configuration
# -----------------------------------

INITIAL_MASTERY = 0.50

LEARNING_RATES = [
    0.1, 0.2, 0.3,
    0.4, 0.5, 0.6,
    0.7, 0.8, 0.9
]


# 20 assessment performances
student_patterns = {

    "improving": [
        0.30, 0.35, 0.40, 0.38, 0.45,
        0.50, 0.48, 0.55, 0.60, 0.58,
        0.65, 0.68, 0.70, 0.72, 0.75,
        0.78, 0.80, 0.82, 0.85, 0.88
    ],

    "strong": [
        0.85, 0.90, 0.88, 0.92, 0.87,
        0.91, 0.89, 0.93, 0.86, 0.90,
        0.88, 0.92, 0.89, 0.94, 0.90,
        0.91, 0.87, 0.93, 0.90, 0.92
    ],

    "struggling": [
        0.35, 0.40, 0.30, 0.38, 0.32,
        0.42, 0.35, 0.30, 0.40, 0.33,
        0.36, 0.41, 0.34, 0.38, 0.31,
        0.37, 0.35, 0.40, 0.32, 0.36
    ],

    "inconsistent": [
        0.80, 0.30, 0.90, 0.40, 0.75,
        0.25, 0.85, 0.35, 0.95, 0.45,
        0.70, 0.30, 0.88, 0.42, 0.78,
        0.28, 0.92, 0.38, 0.82, 0.33
    ]
}


# -----------------------------------
# Mastery function
# -----------------------------------

def update_mastery(old_mastery, performance, learning_rate):

    new_mastery = (
        old_mastery
        + learning_rate
        * (performance - old_mastery)
    )

    return max(0.0, min(1.0, new_mastery))


# -----------------------------------
# Run simulation
# -----------------------------------

results = []


for student_type, performances in student_patterns.items():

    for learning_rate in LEARNING_RATES:

        mastery = INITIAL_MASTERY

        for assessment_number, performance in enumerate(
            performances,
            start=1
        ):

            old_mastery = mastery

            mastery = update_mastery(
                old_mastery,
                performance,
                learning_rate
            )

            results.append({

                "student_type": student_type,

                "assessment":
                    assessment_number,

                "performance":
                    performance,

                "learning_rate":
                    learning_rate,

                "old_mastery":
                    old_mastery,

                "new_mastery":
                    mastery
            })


# -----------------------------------
# DataFrame
# -----------------------------------

df = pd.DataFrame(results)

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data directory
DATA_DIR = PROJECT_ROOT / "data"

# Create it if it does not exist
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Output file
output_file = DATA_DIR / "sequential_mastery.csv"

df.to_csv(
    output_file,
    index=False
)
print(f"\nSimulation saved to:")
print(output_file)

print("\nTotal simulation rows:")
print(len(df))


print("\nSample:")
print(df.head(20).to_string(index=False))


# -----------------------------------
# Final mastery comparison
# -----------------------------------

final_mastery = (

    df
    .groupby([
        "student_type",
        "learning_rate"
    ])
    .tail(1)

)


print("\nFINAL MASTERY\n")

print(
    final_mastery[
        [
            "student_type",
            "learning_rate",
            "new_mastery"
        ]
    ].to_string(index=False)
)


# -----------------------------------
# Plot improving student
# -----------------------------------

student_to_plot = "improving"

subset = df[
    df["student_type"] == student_to_plot
]


plt.figure(figsize=(10, 6))


for lr in LEARNING_RATES:

    lr_data = subset[
        subset["learning_rate"] == lr
    ]

    plt.plot(
        lr_data["assessment"],
        lr_data["new_mastery"],
        label=f"LR={lr}"
    )


# Actual performance
performances = student_patterns[
    student_to_plot
]


plt.plot(
    range(1, 21),
    performances,
    linestyle="--",
    linewidth=3,
    label="Performance"
)


plt.xlabel("Assessment")
plt.ylabel("Mastery")
plt.title(
    "Learning Rate Comparison - Improving Student"
)

plt.legend()
plt.grid(True)

plt.show()