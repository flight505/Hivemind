"""
Predictor 9
Generated on: 2025-09-09 03:03:46
Accuracy: 38.83%
"""


# PREDICTOR 9 - Accuracy: 38.83%
# Correct predictions: 3883/10000 (38.83%)

def predict_output(A, B, C, D, E):
    # Calculate key features
    sum_BCE = B + C + E
    diff_AD = A - D
    ratio_BE = B / (E + 1)
    high_C = C > 80
    low_B = B < 20
    high_E = E > 70
    high_D = D > 60
    low_D = D < 20
    high_A = A > 60
    
    # Primary decision tree with refined conditions
    if high_C and (E > 70 or D < 20):
        return 2
    elif high_C and low_B:
        return 1
    elif high_E and C < 30:
        return 4
    elif B > 90 and (C < 20 or E > 60):
        return 4
    elif low_D and high_C:
        return 1
    elif high_D and E < 30:
        return 3
    else:
        # Secondary decision tree with improved patterns
        if sum_BCE > 180 and B > 70:
            return 2
        elif diff_AD < 0 and high_E:
            return 4
        elif ratio_BE > 1.5 and C < 40:
            return 1
        elif high_A and D > 50:
            return 3
        else:
            return 1