"""
Predictor 87
Generated on: 2025-09-09 03:43:31
Accuracy: 48.47%
"""


# PREDICTOR 87 - Accuracy: 48.47%
# Correct predictions: 4847/10000 (48.47%)

def predict_output(A, B, C, D, E):
    high_A = A > 70
    high_B = B > 70
    high_C = C > 60
    high_D = D > 70
    high_E = E > 80
    low_A = A < 30
    low_B = B < 25
    low_C = C < 25
    low_D = D < 20
    low_E = E < 30
    med_A = 30 <= A <= 70
    med_B = 25 <= B <= 70
    med_C = 25 <= C <= 50
    med_D = 20 <= D <= 70
    med_E = 30 <= E <= 60

    # Specific conditions for known cases
    if high_A and high_D and low_E:
        return 3
    if high_A and low_B:
        return 1
    if med_A and high_C and low_D and low_E:
        return 4
    if med_A and low_D:
        return 4
    if med_A and high_B and low_C:
        return 4
    if med_A and high_D and med_E:
        return 4
    if low_A and low_B and med_C and high_D and med_E:
        return 1
    if med_A and low_B and low_C and med_D and high_E:
        return 4
    if low_A and high_B and med_C and low_D and high_E:
        return 2
    if low_A and high_B and high_C:
        return 2
    if low_A and high_B and low_C and high_D and med_E:
        return 1

    # General decision tree
    if high_C and not high_E:
        return 1
    elif low_C and (high_E or high_D):
        return 4
    elif high_D and E < 35 and C < 30:
        return 3
    elif B > 70 and high_C:
        return 2
    elif low_B and high_A:
        return 4
    else:
        sum_ABC = A + B + C
        if sum_ABC > 130 and B / (D + 1) > 1.0:
            return 1
        elif D + E > 150 and low_C:
            return 4
        elif A - E < 0 and high_D:
            return 3
        elif B > 60 and C > 50:
            return 2
        else:
            return 1