"""
Predictor 1
Generated on: 2025-09-09 03:03:21
Accuracy: 36.83%
"""


# PREDICTOR 1 - Accuracy: 36.83%
# Correct predictions: 3683/10000 (36.83%)

def predict_output(A, B, C, D, E):
    # Calculate key features
    sum_ABC = A + B + C
    sum_DE = D + E
    diff_BD = B - D
    ratio_BE = B / (E + 1)  # Avoid division by zero
    
    if sum_ABC > 100 and diff_BD < 0:
        return 1
    elif sum_DE > 140 and C > 70:
        return 2
    elif A > 40 and E < 40 and D > 20:
        return 3
    elif B > 30 and D < 30:
        return 4
    else:
        # Default case - prioritize most common pattern
        if ratio_BE > 2.0:
            return 1
        elif sum_ABC < 80:
            return 3
        else:
            return 2