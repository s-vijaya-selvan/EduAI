students = [
    {"name": "student A",
     "attempted": 10, "correct":9},
     {"name": "student B",
      "attempted": 10, "correct":4},
      {"name":"student C",
       "attempted": 20, "correct": 15},
         
     ]

for student in students:
    accuracy = student["correct"] / student["attempted"]

    print(
        student["name"],
        "Accuracy:",
        round(accuracy,2)
    )
