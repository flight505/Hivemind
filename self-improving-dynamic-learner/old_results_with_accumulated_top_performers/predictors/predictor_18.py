"""
Predictor 18
Generated on: 2025-09-09 03:04:21
Accuracy: 47.59%
"""


# PREDICTOR 18 - Accuracy: 47.59%
# Correct predictions: 4759/10000 (47.59%)

def predict_output(A, B, C, D, E):
    # Calculate key features with refined combinations
    sum_ABC = A + B + C
    sum_DE = D + E
    diff_AE = A - E
    diff_BD = B - D
    ratio_BD = B / (D + 1)
    ratio_CE = C / (E + 1)
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
    if high_C and not high_E:
        return 1
    elif B > 70 and C > 50:
        return 2
    elif high_D and E < 40:
        return 3
    elif low_C and (high_E or D > 20):
        return 4
    elif A > 40 and B > 30 and C < 25:
        return 4
    elif low_B and high_A:
        return 4
    elif C > 50 and E < 30:
        return 4
    else:
        # Secondary decision tree with refined patterns
        if sum_ABC > 130 and ratio_BD > 1.0:
            return 1
        elif sum_DE > 150 and low_C:
            return 4
        elif diff_AE < 0 and high_D:
            return 3
        elif B > 60 and C > 50:
            return 2
        elif med_C and D > 50:
            return 1
        elif E > 70 and A < 30:
            return 4
        elif D > 60 and C < 50:
            return 3
        else:
            # Tertiary conditions for edge cases
            if avg_all > 60 and diff_BD > 0:
                return 1
            elif A > 80 and B < 60:
                return 1
            elif B > 80 and D < 30:
                return 2
            elif E < 20 and high_D:
                return 3
            else:
                return 1