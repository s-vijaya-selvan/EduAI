from ai.mastery import calculate_accuracy, update_mastery

def test_accuracy():
    assert calculate_accuracy(8,10) == 0.8

def test_zero_attempts():
    assert calculate_accuracy(0,0) ==0.0

def test_mastery_increases():
    new_mastery = update_mastery(old_mastery=0.4,performance=0.8
    )

    assert new_mastery > 0.4
    
