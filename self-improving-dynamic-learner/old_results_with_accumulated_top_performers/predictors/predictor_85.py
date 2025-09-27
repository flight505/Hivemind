"""
Predictor 85
Generated on: 2025-09-09 03:40:26
Accuracy: 51.50%
"""


# PREDICTOR 85 - Accuracy: 51.50%
# Correct predictions: 5150/10000 (51.50%)

def predict_output(A, B, C, D, E):
    sum_ABC = A + B + C
    sum_DE = D + E
    diff_AE = A - E
    ratio_BD = B / (D + 1)
    high_C = C > 60
    high_E = E > 80
    low_C = C < 25
    high_D = D > 70
    low_B = B < 25
    high_A = A > 70
    high_B = B > 70
    low_A = A < 30
    med_A = 30 <= A <= 70
    med_B = 25 <= B <= 70
    med_D = 20 <= D <= 70
    low_D = D < 20
    med_E = 30 <= E <= 60
    low_E = E < 30
    med_C = 25 <= C <= 60

    # Specific conditions for known cases
    if high_A and high_B:
        return 1
    elif high_A and low_B and low_C and high_D and med_E:
        return 3
    elif low_A and high_B and high_C and low_D and low_E:
        return 1
    elif med_A and low_B and low_C and low_D and low_E:
        return 3
    elif med_A and med_B and med_C and med_D and low_E:
        return 4
    elif med_A and med_B and low_C and high_D and low_E:
        return 1
    elif med_A and med_B and low_C and high_D and med_E:
        return 3
    elif low_A and med_B and med_C and high_D and low_E:
        return 1
    elif med_A and high_B and high_C and low_D and low_E:
        return 1
    elif med_A and med_B and low_C and low_D and high_E:
        return 4
    elif high_A and low_B and low_C and high_D and low_E:
        return 3
    elif med_A and med_B and high_C and low_D and high_E:
        return 2
    elif low_A and high_B and high_C and high_D and high_E:
        return 2

    # Original primary decision tree
    if high_C and not high_E and B < 80:
        return 1
    elif low_C and high_E:
        return 4
    elif high_D and E < 35 and C < 30:
        return 3
    elif B > 70 and high_C and D < 30:
        return 2
    elif low_B and A > 70 and C > 25:
        return 4
    else:
        # Secondary decision tree
        if sum_ABC > 130 and ratio_BD > 1.0:
            return 1
        elif sum_DE > 150 and low_C:
            return 4
        elif diff_AE < 0 and high_D:
            return 3
        elif B > 60 and C > 50:
            return 2
        else:
            return 1