"""
Predictor 136
Generated on: 2025-09-09 04:18:09
Accuracy: 38.68%
"""


# PREDICTOR 136 - Accuracy: 38.68%
# Correct predictions: 3868/10000 (38.68%)

def predict_output(A, B, C, D, E):
    # Calculate key features using basic arithmetic operations
    sum_ABC = A + B + C
    sum_DE = D + E
    diff_AE = A - E
    diff_BD = B - D
    ratio_BD = B / (D + 1)
    ratio_AD = A / (D + 1)
    avg_all = (A + B + C + D + E) / 5
    sum_AB = A + B
    sum_CD = C + D
    sum_BE = B + E
    diff_CB = C - B
    sum_ADE = A + D + E
    ratio_CE = C / (E + 1)
    
    # Define simple threshold categories for comparisons
    high_C = C > 60
    low_C = C < 25
    med_C = 25 <= C <= 50
    high_D = D > 70
    high_E = E > 80
    low_B = B < 25
    med_B = 25 <= B <= 70
    high_A = A > 70
    high_B = B > 70
    low_A = A < 30
    med_A = 30 <= A <= 70
    low_D = D < 20
    med_D = 20 <= D <= 70
    low_E = E < 30
    med_E = 30 <= E <= 60
    
    # Primary decision tree with refined conditions based on successful patterns
    if high_C and not high_E and B < 80:
        if diff_CB > 30 and low_B and not high_D:
            return 1
        elif high_B and D < 40:
            return 2
        elif low_B and E < 50 and (D < 20 or E < 40):
            return 3
        else:
            return 1
    elif low_C and (high_E or high_D):
        if sum_ADE > 150 or (B > 60 and D < 40):
            return 4
        else:
            return 4
    elif high_D and E < 35 and C < 30:
        return 3
    elif B > 70 and high_C and D < 30:
        return 2
    elif low_B and high_A:
        if C > 40 or sum_AB > 80:
            return 1
        else:
            return 4
    elif A > 40 and B > 30 and low_C:
        if ratio_CE < 0.3 or sum_DE > 120:
            return 4
        else:
            return 4
    elif med_C and D > 50 and B < 60:
        if E < 40 or ratio_AD > 1.2:
            return 1
        else:
            return 3
    else:
        # Secondary decision tree with improved mathematical patterns
        if sum_ABC > 130 and ratio_BD > 1.0 and not high_D:
            return 1
        elif sum_DE > 150 and low_C and A < 30:
            return 4
        elif diff_AE < 0 and high_D and E < 40:
            return 3
        elif B > 60 and C > 50 and E < 60 and not high_D:
            return 2
        elif high_A and low_B and C > 40:
            return 1
        elif B > 80 and low_C and D > 50:
            return 4
        elif B > 70 and high_E and C > 50:
            return