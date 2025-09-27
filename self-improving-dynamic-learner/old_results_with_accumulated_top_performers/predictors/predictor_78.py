"""
Predictor 78
Generated on: 2025-09-09 03:35:37
Accuracy: 47.00%
"""


# PREDICTOR 78 - Accuracy: 47.00%
# Correct predictions: 4700/10000 (47.00%)

def predict_output(A, B, C, D, E):
    # Basic thresholds
    high_A = A > 70
    high_B = B > 70
    high_C = C > 60
    high_D = D > 70
    high_E = E > 80
    low_A = A < 30
    low_B = B < 25
    low_C = C < 25
    low_D = D < 20
    low_E = E < 30
    med_C = 25 <= C <= 50
    med_A = 30 <= A <= 70
    med_B = 25 <= B <= 70
    med_D = 20 <= D <= 70
    med_E = 30 <= E <= 60
    
    sum_ABC = A + B + C
    sum_DE = D + E
    diff_AE = A - E
    ratio_BD = B / (D + 1)
    
    # Primary decision tree - prioritize key patterns
    if high_C and not high_E and B < 80:
        if low_B and not high_D:
            if diff_AE < 0:
                return 3
            else:
                return 1
        elif high_B:
            return 2
        else:
            return 1
    elif low_C and (high_E or high_D):
        if low_B and high_A:
            return 3
        else:
            return 4
    elif high_D and E < 35 and C < 30:
        return 3
    elif B > 70 and high_C and D < 30:
        return 2
    elif low_B and high_A:
        return 4
    elif A > 40 and B > 30 and low_C:
        return 4
    elif med_C and D > 50 and B < 60:
        return 1
    else:
        # Secondary decision tree with numerical patterns
        if sum_ABC > 130 and ratio_BD > 1.0:
            return 1
        elif sum_DE > 150 and low_C:
            return 4
        elif diff_AE < 0 and high_D:
            return 3
        elif B > 60 and C > 50:
            return 2
        else:
            return 1