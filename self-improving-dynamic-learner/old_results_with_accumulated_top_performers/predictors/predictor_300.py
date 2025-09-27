"""
Predictor 300
Generated on: 2025-09-09 07:43:29
Accuracy: 26.72%
"""


# PREDICTOR 300 - Accuracy: 26.72%
# Correct predictions: 2672/10000 (26.72%)

def predict_output(A, B, C, D, E):
    # Calculate key features using basic arithmetic operations
    sum_ABC = A + B + C
    sum_DE = D + E
    diff_AE = A - E
    diff_BD = B - D
    product_AE = A * E
    product_BC = B * C
    product_AD = A * D
    product_BE = B * E
    avg_all = (A + B + C + D + E) / 5
    sum_AB = A + B
    sum_CD = C + D
    sum_BE = B + E
    diff_CB = C - B
    sum_ADE = A + D + E
    ratio_CE = C / (E + 1)
    
    # Define refined threshold categories for pattern recognition
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
    
    # Primary decision tree with refined conditions from cross-cycle learning
    if high_C and not high_E and B < 80:
        if product_AE > product_BC and low_B and not high_D:
            return 1
        elif high_B and D < 35 and sum_AB < 140:
            return 2
        elif low_B and E < 50 and (D < 20 or E < 40) and diff_AE < 0:
            return 3
        else:
            return 1
    elif low_C and (high_E or high_D):
        if sum_AB < 85 or low_A or (high_A and sum_DE > 130):
            return 4
        else:
            return 4
    elif high_D and E < 35 and C < 30:
        if product_AD > product_BE:
            return 3
        return 3
    elif B > 70 and high_C and D < 30:
        return 2
    elif low_B and high_A:
        if product_AB > (C + D) * 10:
            return 4
        else:
            return 1
    elif A > 40 and B > 30 and low_C:
        if ratio_CE < 0.3 or sum_DE > 110:
            return 4
        else:
            return 3
    elif med_C and D > 50 and B < 60:
        if avg_all > 60 and diff_BD > 0:
            return 1
        else:
            return 3
    else:
        # Secondary decision tree with refined mathematical patterns from TOP #2 and #10
        if sum_ABC > 135 and ratio_BD > 0.95 and not high_D:
            return 1
        elif sum_DE > 155 and low_C and A < 35:
            return 4
        elif diff_AE < 0 and high_D and E < 45:
            return 3
        elif B > 60 and C > 50 and E < 65 and not high_D:
            return 2
        elif high_A and low_B and C > 40:
            return 1
        elif B > 80 and low_C and D > 50:
            return 4
        elif B > 70 and high_E and C > 50:
            return 2
        else:
            # Enhanced tertiary conditions with targeted fixes from cross-cycle failures
            # Fix for high B, high C cases that should be 2 with refined conditions (TOP #10 pattern)
            if high_B and high_C and (D > 70 or E > 50):
                return 2
            # Fix for high A, med