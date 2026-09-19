import pandas as pd


df = pd.read_csv(
    "data/mastery_simulation.csv"
)


summary = (
    df
    .groupby("learning_rate")
    .agg(
        average_change=("mastery_change", "mean"),
        average_absolute_change=(
            "mastery_change",
            lambda x: x.abs().mean()
        ),
        maximum_change=("mastery_change", "max"),
        minimum_change=("mastery_change", "min")
    )
)

df = pd.DataFrame(summary)


print("\nTOTAL SIMULATIONS")
print(len(df))


print("\nFIRST 20 RESULTS")
print(df.head(20).to_string(index=False))


print("\nSUMMARY")
print(
    df[
        [
            "average_change",
            "average_absolute_change",
            "maximum_change",
            "minimum_change"
        ]
    ].describe()
)


output_file = "data/mastery_simulation_analysis1.csv"

df.to_csv(
    output_file,
    index=False
)

print(
    f"\nSimulation saved to: {output_file}"
)