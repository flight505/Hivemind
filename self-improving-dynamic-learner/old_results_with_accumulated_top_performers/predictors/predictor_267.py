"""
Predictor 267
Generated on: 2025-09-09 06:49:03
Accuracy: 37.82%
"""


# PREDICTOR 267 - Accuracy: 37.82%
# Correct predictions: 3782/10000 (37.82%)

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
    product_AB = A * B
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
    med_E_high = 60 <= E <= 80
    
    # Primary decision tree with refined conditions based on successful patterns from high-performers
    if high_C and not high_E and B < 80:
        # Enhanced condition combining TOP #1 and #4 patterns with new B+C analysis
        if diff_CB > 25 and low_B and not high_D:
            return 1
        elif high_B and D < 35 and (B + C) / (D + 1) < 2.0:
            return 2
        elif low_B and E < 50 and (D < 20 or E < 40):
            return 3
        else:
            return 1
    elif low_C and (high_E or high_D):
        # Improved condition for low C cases - handles high A cases better
        if sum_AB < 85 or low_A or (high_A and sum_DE > 130):
            return 4
        else:
            return 4
    elif high_D and E < 35 and C < 30:
        return 3
    elif B > 70 and high_C and D < 30:
        # Fix for error #2: high B, high C cases should be 1 when E is moderate
        if high_E and E < 60:
            return 1
        return 2
    elif low_B and high_A:
        # Refined condition for low B, high A cases
        if C < 30 or sum_AB > 80:
            return 4
        else:
            return 1
    elif A > 40 and B > 30 and low_C:
        # Enhanced condition for moderate A,B with low C
        if D > 60 or E > 70 or sum_DE > 110:
            return 4
        else:
            return 3
    elif med_C and D > 50 and B < 60:
        # Improved medium C condition
        if E < 45 or ratio_AD > 1.1:
            return 1
        else:
            return 3
    else:
        # Secondary decision tree with improved mathematical patterns
        if sum_ABC > 135 and ratio_BD > 0.95 and not high_D:
            return 1
        elif sum_DE > 155 and low_C and A < 35:
            return 4
        elif diff_AE < 0 and high_D and E < 45:
            return