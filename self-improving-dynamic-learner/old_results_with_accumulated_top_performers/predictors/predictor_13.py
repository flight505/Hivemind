"""
Predictor 13
Generated on: 2025-09-09 03:03:58
Accuracy: 51.83%
"""


# PREDICTOR 13 - Accuracy: 51.83%
# Correct predictions: 5183/10000 (51.83%)

def predict_output(A, B, C, D, E):
    # Calculate key features with improved combinations
    sum_ABC = A + B + C
    sum_DE = D + E
    diff_AE = A - E
    diff_BD = B - D
    ratio_BD = B / (D + 1)
    avg_all = (A + B + C + D + E) / 5
    low_B = B < 25
    high_C = C > 60
    low_C = C < 25
    high_D = D > 70
    high_E = E > 80
    
    # Primary decision tree with refined conditions
    if high_C and not high_E:
        return 1
    elif low_C and (high_E or D > 60):
        return 4
    elif high_D and E < 35:
        return 3
    elif B > 70 and high_C:
        return 2
    elif low_B and A > 70:
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
            # Additional conditions for specific cases
            if B > 80 and C < 20:
                return 4
            elif B > 75 and E > 90:
                return 2
            elif A > 90 and B > 50 and C > 50:
                return 2
            elif A > 85 and B < 30 and C < 5:
                return 1
            else:
                return 1