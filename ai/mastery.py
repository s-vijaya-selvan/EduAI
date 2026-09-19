def calculate_accuracy(correct:
                       int, attempted: int) -> float:
    if attempted <= 0:
        return 0.0

    return correct / attempted

def update_mastery(
        old_mastery: float,
        performance: float,
        learning_rate: float = 0.30) -> float:
        new_mastery = old_mastery + learning_rate * (performance - old_mastery)
        return  max(0.0, min(1.0,new_mastery))


if __name__ == "__main__":
     old_mastery = 0.40
     accuracy = calculate_accuracy(correct=8, attempted=10)

     new_mastery= update_mastery(old_mastery,accuracy)

     print("Previous mastery:",old_mastery)
     print("Current performance:",accuracy)
     print("Updated mastery:",round(new_mastery,2))
