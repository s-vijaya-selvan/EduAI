import pandas as pd


df = pd.read_csv(
    "data/sequential_mastery.csv"
)


results = []


for student_type in df["student_type"].unique():

    student_df = df[
        df["student_type"] == student_type
    ]


    for lr in sorted(
        student_df["learning_rate"].unique()
    ):

        lr_df = student_df[
            student_df["learning_rate"] == lr
        ].copy()


        # Performance on NEXT assessment
        lr_df["next_performance"] = (
            lr_df["performance"].shift(-1)
        )


        # Last row has no future assessment
        lr_df = lr_df.dropna(
            subset=["next_performance"]
        )


        # Prediction error
        lr_df["error"] = (
            lr_df["next_performance"]
            - lr_df["new_mastery"]
        )


        lr_df["squared_error"] = (
            lr_df["error"] ** 2
        )


        mse = lr_df[
            "squared_error"
        ].mean()


        mae = (
            lr_df["error"]
            .abs()
            .mean()
        )


        results.append({

            "student_type":
                student_type,

            "learning_rate":
                lr,

            "MSE":
                mse,

            "MAE":
                mae
        })


optimization_df = pd.DataFrame(
    results
)


print("\nLEARNING RATE PERFORMANCE\n")

print(
    optimization_df.to_string(
        index=False
    )
)


print("\nLOWEST MSE FOR EACH SIMULATED PATTERN\n")


best = (

    optimization_df
    .sort_values("MSE")
    .groupby("student_type")
    .first()
    .reset_index()

)


print(
    best.to_string(
        index=False
    )
)


optimization_df.to_csv(
    "data/learning_rate_optimization.csv",
    index=False
)