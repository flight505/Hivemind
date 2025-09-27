"""
Predictor 16
Generated on: 2025-09-09 03:04:11
Accuracy: 52.58%
"""


# PREDICTOR 16 - Accuracy: 52.58%
# Correct predictions: 5258/10000 (52.58%)

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
    med_C = 25 <= C <= 40
    high_D = D > 70
    high_E = E > 80
    low_B = B < 25
    high_A = A > 70
    high_B = B > 70
    
    # Primary decision tree with improved conditions
    if high_C or (B > 50 and sum_ABC > 120):
        return 1
    elif low_C and (high_E or D > 20):
        return 4
    elif high_D and E < 40:
        return 3
    elif B > 60 and C > 70:
        return 2
    elif low_B and high_A:
        return 4
    elif A > 40 and B > 30 and C < 25:
        return 4
    elif med_C and D > 50:
        return 1
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
        elif high_B and C > 40:
            return 2
        elif E > 70 and A < 30:
            return 4
        elif D > 60 and C < 50:
            return 3
        else:
            # Tertiary conditions for edge cases
            if A > 80 and B < 60:
                return 1
            elif B > 80 and D < 30:
                return 2
            elif E < 20 and high_D:
                return 3
            else:
                return 1