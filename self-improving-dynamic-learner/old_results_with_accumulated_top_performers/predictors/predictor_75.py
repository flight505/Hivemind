"""
Predictor 75
Generated on: 2025-09-09 03:34:17
Accuracy: 33.01%
"""


# PREDICTOR 75 - Accuracy: 33.01%
# Correct predictions: 3301/10000 (33.01%)

def predict_output(A, B, C, D, E):
    # Calculate key features
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
    low_D = D < 20
    med_D = 20 <= D <= 70
    low_E = E < 30
    med_E = 30 <= E <= 60

    # Primary decision tree with refined conditions
    if high_C and high_B and high_A:
        return 1
    elif high_C and high_B:
        return 2
    elif high_C:
        return 1
    elif low_C and high_A and low_B:
        return 3
    elif low_C and high_D:
        return 1
    elif low_C and high_E:
        return 4
    elif low_C and low_B:
        return 3
    elif med_C:
        if high_E:
            return 1
        elif low_E:
            return 4
        elif low_D and low_A:
            return 3
        else:
            return 1
    elif med_A and high_D:
        return 1
    elif low_B and high_A:
        return 4
    else:
        # Secondary decision tree with improved patterns
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