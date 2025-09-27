"""
Predictor 15
Generated on: 2025-09-09 03:04:06
Accuracy: 50.66%
"""


# PREDICTOR 15 - Accuracy: 50.66%
# Correct predictions: 5066/10000 (50.66%)

def predict_output(A, B, C, D, E):
    # Calculate key features with refined combinations
    sum_ABC = A + B + C
    sum_DE = D + E
    diff_AE = A - E
    diff_BD = B - D
    ratio_BD = B / (D + 1)
    avg_all = (A + B + C + D + E) / 5
    high_C = C > 60
    low_C = C < 25
    high_D = D > 70
    high_E = E > 80
    low_B = B < 25
    high_A = A > 70
    med_C = C > 40 and C < 60
    
    # Primary decision tree with improved conditions
    if high_C or (B > 50 and sum_ABC > 120):
        return 1
    elif low_C and (high_E or D > 20):
        return 4
    elif high_D and E < 40:
        return 3
    elif B > 60 and high_C:
        return 2
    elif low_B and high_A:
        return 4
    elif A > 40 and B > 30 and C < 25:
        return 4
    else:
        # Secondary decision tree with refined patterns
        if avg_all > 60 and diff_BD > 0:
            return 1
        elif sum_DE > 150 and B < 40:
            return 4
        elif diff_AE < 0 and D > 50:
            return 3
        elif sum_ABC < 100:
            return 2
        elif med_C and B > 40:
            return 1
        elif E > 70 and D < 50:
            return 4
        elif B > 70 and E > 30:
            return 2
        else:
            # Tertiary conditions for edge cases
            if A > 80 and C < 20:
                return 1
            elif D > 60 and E < 20:
                return 3
            elif B > 45 and C > 30:
                return 2
            else:
                return 1