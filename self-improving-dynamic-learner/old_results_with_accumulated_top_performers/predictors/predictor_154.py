"""
Predictor 154
Generated on: 2025-09-09 04:34:29
Accuracy: 43.33%
"""


# PREDICTOR 154 - Accuracy: 43.33%
# Correct predictions: 4333/10000 (43.33%)

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
    
    # Define threshold categories for pattern recognition
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
        if diff_CB > 25 and low_B and D < 30:
            return 1
        elif high_B and D < 35:
            return 2
        else:
            return 1
    elif low_C and (high_E or high_D):
        if A < 40 or sum_AB < 80:
            return 4
        else:
            return 4
    elif high_D and E < 35 and C < 30:
        return 3
    elif B > 70 and high_C and D < 30:
        return 2
    elif low_B and high_A:
        if C < 30:
            return 4
        else:
            return 1
    elif A > 40 and B > 30 and low_C:
        if D > 60 or E > 70:
            return 4
        else:
            return 3
    elif med_C and D > 50 and B < 60:
        return 1
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
            return 2
        else:
            # Enhanced tertiary conditions with specific fixes for current errors
            # Fix for cases with high C and low B that should be 3 or 4
            if high_C and low_B and E < 50:
                if D < 20 or E < 40:
                    return 3
                else:
                    return 4
            # Fix for high B cases that should be 2
            elif high_B and med_C and not high_E:
                return 2
            # Fix for low B, med C cases that should be 3
            elif low_B and med_C and E < 40:
                return 3
            # Fix for high B, low C cases that should be 1
            elif high_B and low_C and not high_D:
                return 1
            # Fix for low A, high B cases that should be 4
            elif low_A and high_B and high_E:
                return 4
            # Fix for high A, med B, low C cases that should be 3
            elif high_A and med_B and low_C and high_D:
                return 3
            # Fix for high A, low B, med