"""
Predictor 76
Generated on: 2025-09-09 03:35:07
Accuracy: 53.75%
"""


# PREDICTOR 76 - Accuracy: 53.75%
# Correct predictions: 5375/10000 (53.75%)

def predict_output(A, B, C, D, E):
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
    
    # Primary decision tree with refined conditions
    if high_A and high_B and high_C:
        return 1
    elif high_A and high_B and low_C:
        if high_D:
            return 4
        else:
            return 2
    elif high_A and high_B and med_C:
        return 2
    elif high_C and not high_E:
        return 1
    elif low_C and high_E:
        return 4
    elif low_C and high_D:
        return 4
    elif low_C and low_B and high_A:
        return 3
    elif med_C and high_D:
        return 1
    elif low_B and high_A:
        return 4
    elif low_A and med_B and high_C and low_D and med_E:
        return 4
    elif low_A and high_B and med_C and low_D:
        if C < 45:
            return 4
        else:
            return 3
    elif med_A and high_B and high_C:
        return 1
    elif med_A and high_B and med_C and high_E:
        return 2
    elif med_A and high_B and low_C and high_D:
        return 4
    elif low_A and med_B and low_C and low_D and med_E:
        return 3
    elif high_A and low_B and med_C and low_D and med_E:
        return 1
    elif med_A and med_B and med_C and med_D and med_E:
        if B > 50 and D > 55:
            return 3
        else:
            return 2
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
            return 1