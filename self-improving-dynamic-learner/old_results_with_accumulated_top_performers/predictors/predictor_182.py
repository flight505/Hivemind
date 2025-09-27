"""
Predictor 182
Generated on: 2025-09-09 05:04:02
Accuracy: 48.88%
"""


# PREDICTOR 182 - Accuracy: 48.88%
# Correct predictions: 4888/10000 (48.88%)

def predict_output(A, B, C, D, E):
    # Calculate key features using basic arithmetic operations
    sum_ABC = A + B + C
    sum_DE = D + E
    diff_AE = A - E
    ratio_BD = B / (D + 1)
    
    # Define threshold categories for pattern recognition
    high_C = C > 60
    low_C = C < 25
    med_C = 25 <= C <= 50
    high_D = D > 70
    high_E = E > 80
    low_B = B < 25
    high_A = A > 70
    high_B = B > 70
    low_A = A < 30
    med_A = 30 <= A <= 70
    med_B = 25 <= B <= 70
    low_D = D < 20
    med_E = 30 <= E <= 60
    low_E = E < 30
    
    # Primary decision tree with refined conditions based on sample data patterns
    if low_B and C < 15:
        return 3
    elif low_B and low_C:
        return 1
    elif high_E and low_C:
        return 4
    if high_C:
        if high_B and low_D:
            return 1
        elif high_B and high_C and high_D and B > 85:
            return 2
        elif high_B and high_C and high_D:
            return 3
        elif low_D and high_E:
            return 2
        elif high_D and med_E:
            return 1
        elif low_E:
            if B + C > 120:
                return 2
            else:
                return 4
        else:
            return 1
    elif low_C and high_D:
        return 1
    elif low_C and low_B:
        return 3
    elif med_C and (low_B or low_A or low_E):
        return 3
    # Secondary decision tree with improved mathematical patterns
    if sum_ABC > 130 and ratio_BD > 1.0 and not high_D:
        return 1
    elif sum_DE > 150 and low_C and A < 30:
        return 4
    elif diff_AE < 0 and high_D and E < 40:
        return 3
    elif B > 60 and C > 50 and E < 60 and not high_D:
        return 2
    else:
        return 1