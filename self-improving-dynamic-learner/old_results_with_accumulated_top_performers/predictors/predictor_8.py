"""
Predictor 8
Generated on: 2025-09-09 03:03:43
Accuracy: 36.87%
"""


# PREDICTOR 8 - Accuracy: 36.87%
# Correct predictions: 3687/10000 (36.87%)

def predict_output(A, B, C, D, E):
    # Calculate key features
    sum_ABC = A + B + C
    sum_DE = D + E
    diff_AB = A - B
    ratio_CD = C / (D + 1)
    high_A = A > 70
    low_B = B < 30
    high_C = C > 50
    high_D = D > 60
    high_E = E > 70
    
    # Primary decision tree with refined conditions
    if low_B and high_A:
        return 4
    elif high_C and B < 40 and D < 20:
        return 3
    elif B > 80 and C < 40:
        return 1
    elif high_E and D > 70:
        return 4
    elif high_D and E < 30:
        return 3
    elif C > 80 and B < 20:
        return 2
    else:
        # Secondary decision tree with improved patterns
        if sum_ABC > 150 and diff_AB > 0:
            return 1
        elif sum_DE > 140 and high_E:
            return 4
        elif ratio_CD > 1.0 and A > 50:
            return 3
        elif B > 60 and C > 60:
            return 2
        else:
            return 1