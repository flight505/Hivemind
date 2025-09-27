"""
Predictor 6
Generated on: 2025-09-09 03:03:36
Accuracy: 41.15%
"""


# PREDICTOR 6 - Accuracy: 41.15%
# Correct predictions: 4115/10000 (41.15%)

def predict_output(A, B, C, D, E):
    # Calculate key features
    sum_ABC = A + B + C
    sum_DE = D + E
    diff_AE = A - E
    ratio_BE = B / (E + 1)
    high_B = B > 90
    high_C = C > 70
    high_D = D > 70
    high_E = E > 70
    low_B = B < 20
    
    # Primary decision tree - refined conditions
    if high_B and not high_E:
        return 2
    elif high_C and E < 30:
        return 4
    elif C > 50 and B < 40:
        return 1
    elif high_D and E < 40:
        return 3
    elif high_E and D < 30:
        return 4
    elif sum_ABC > 150 and B > 40:
        return 1
    else:
        # Secondary decision tree with improved logic
        if B > 60 and C > 60:
            return 2
        elif A > 70 and D > 50:
            return 3
        elif high_B and C < 30:
            return 1
        elif E > 60 and C > 40:
            return 1
        else:
            return 2