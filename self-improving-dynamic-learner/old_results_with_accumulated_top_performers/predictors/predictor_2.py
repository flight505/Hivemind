"""
Predictor 2
Generated on: 2025-09-09 03:03:24
Accuracy: 41.25%
"""


# PREDICTOR 2 - Accuracy: 41.25%
# Correct predictions: 4125/10000 (41.25%)

def predict_output(A, B, C, D, E):
    # Calculate key features
    sum_ABC = A + B + C
    sum_all = A + B + C + D + E
    diff_AE = A - E
    ratio_BD = B / (D + 1)  # Avoid division by zero
    high_B = B > 70
    
    if high_B and C > 50:
        return 1
    elif diff_AE < 0 and D > 50:
        return 3
    elif sum_ABC < 120 and E > 60:
        return 2
    elif A > 40 and B > 30 and C < 25:
        return 4
    else:
        # Secondary decision tree
        if sum_all > 200:
            return 1
        elif E < 30 and A > 50:
            return 3
        elif B > 50 and D < 20:
            return 2
        else:
            return 1