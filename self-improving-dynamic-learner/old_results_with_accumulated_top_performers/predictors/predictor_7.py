"""
Predictor 7
Generated on: 2025-09-09 03:03:39
Accuracy: 38.32%
"""


# PREDICTOR 7 - Accuracy: 38.32%
# Correct predictions: 3832/10000 (38.32%)

def predict_output(A, B, C, D, E):
    # Calculate key features
    sum_ABC = A + B + C
    sum_DE = D + E
    diff_BE = B - E
    ratio_AD = A / (D + 1)
    high_B = B > 90
    high_E = E > 80
    low_C = C < 20
    high_D = D > 60
    mid_C = C > 60
    
    # Primary decision tree with refined conditions
    if high_E and (D > 40 or low_C):
        return 4
    elif mid_C and B < 70:
        return 1
    elif high_B and not high_E:
        return 2
    elif high_D and E < 50:
        return 3
    elif sum_DE > 160:
        return 4
    else:
        # Secondary decision tree with improved patterns
        if sum_ABC > 140 and C > 40:
            return 1
        elif B > 80 and low_C:
            return 4
        elif A > 60 and D > 50:
            return 3
        elif diff_BE < 0 and high_D:
            return 1
        else:
            return 2