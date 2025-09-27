"""
Predictor 203
Generated on: 2025-09-09 05:19:34
Accuracy: 30.31%
"""


# PREDICTOR 203 - Accuracy: 30.31%
# Correct predictions: 3031/10000 (30.31%)

def predict_output(A, B, C, D, E):
    # Calculate key features using basic arithmetic
    sum_ABC = A + B + C
    sum_DE = D + E
    diff_AE = A - E
    diff_BD = B - D
    ratio_BD = B / (D + 1)
    avg_all = (A + B + C + D + E) / 5
    high_C = C > 60
    high_E = E > 80
    low_C = C < 25
    high_D = D > 70
    low_B = B < 25
    high_A = A > 70
    low_A = A < 30
    med_A = 30 <= A <= 70
    med_B = 25 <= B <= 70
    low_D = D < 20
    low_E = E < 30
    med_C = 25 <= C <= 50
    
    # Primary decision tree with refined conditions
    if high_C and not high_E:
        if low_B and avg_all < 70:
            if low_A:
                return 1
            else:
                return 2
        elif high_B:
            if low_D:
                return 1
            else:
                return 2
        else:
            return 1
    elif low_C and (high_E or high_D):
        if high_A and avg_all < 80:
            return 1
        else:
            return 4
    elif high_D and E < 35:
        if low_B:
            return 3
        else:
            return 1
    elif B > 70 and high_C:
        return 2
    elif low_B and high_A:
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