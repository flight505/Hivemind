"""
Predictor 109
Generated on: 2025-09-09 04:03:40
Accuracy: 50.83%
"""


# PREDICTOR 109 - Accuracy: 50.83%
# Correct predictions: 5083/10000 (50.83%)

def predict_output(A, B, C, D, E):
    # Calculate key features
    sum_ABC = A + B + C
    sum_DE = D + E
    diff_AE = A - E
    ratio_BD = B / (D + 1)
    high_C = C > 60
    high_E = E > 80
    low_C = C < 25
    high_D = D > 70
    low_B = B < 25
    high_A = A > 70
    low_A = A < 30
    med_A = 30 <= A <= 70
    med_B = 25 <= B <= 70
    med_D = 20 <= D <= 70
    low_D = D < 20
    med_E = 30 <= E <= 60
    low_E = E < 30
    med_C = 25 <= C <= 50
    
    # Primary decision tree with refined conditions
    if high_C and not high_E:
        return 1
    elif low_C and high_E:
        return 4
    elif low_C and high_D and low_E:
        return 3
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
            return 1