"""
Predictor 168
Generated on: 2025-09-09 04:52:00
Accuracy: 41.75%
"""


# PREDICTOR 168 - Accuracy: 41.75%
# Correct predictions: 4175/10000 (41.75%)

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
    low_A = A < 30
    # Primary decision tree with refined conditions
    if high_C and not high_E:
        if diff_AE > 25 and low_B and D < 30:
            return 1
        elif low_A and C > 80:
            return 4
        else:
            return 1
    elif low_C:
        if high_E:
            return 4
        elif high_D:
            if E < 30:
                return 1
            else:
                return 3
        else:
            return 3
    elif high_D and E < 35:
        return 3
    elif B > 70 and high_C:
        return 2
    elif low_B and A > 70:
        return 4
    elif low_B and high_E:
        return 2
    elif high_A and high_B:
        return 2
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