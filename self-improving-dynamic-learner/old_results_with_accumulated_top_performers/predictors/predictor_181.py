"""
Predictor 181
Generated on: 2025-09-09 05:01:27
Accuracy: 49.79%
"""


# PREDICTOR 181 - Accuracy: 49.79%
# Correct predictions: 4979/10000 (49.79%)

def predict_output(A, B, C, D, E):
    # Calculate key mathematical features using basic arithmetic operations
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
    
    # Primary decision tree with refined conditions based on successful patterns from high-performers
    if high_C and not high_E and B < 80:
        # Refined condition for high C cases - improved from TOP #1 and #4 patterns
        if diff_CB > 25 and low_B and not high_D:
            return 1
        elif high_B and D < 35:
            return 2
        elif low_B and E < 50 and (D < 20 or E < 40):
            return 3
        else:
            return 1
    elif low_C and (high_E or high_D):
        # Improved condition for low C cases - handles cases where A is high but should still be 4
        if sum_AB < 85 or low_A or (high_A and sum_DE > 130):
            return 4
        else:
            return 4
    elif high_D and E < 35 and C < 30:
        return 3
    elif B > 70 and high_C and D < 30:
        return 2
    elif low_B and high_A:
        # Refined condition for low B, high A cases - handles C variations better
        if C < 30 or sum_AB > 75:
            return 4
        else:
            return 1
    elif A > 40 and B > 30 and low_C:
        # Enhanced condition for low C with moderate A,B
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
        # Secondary decision tree with improved mathematical patterns from TOP #2 and #3
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
            # Enhanced tertiary conditions with targeted fixes from cross-cycle learning
            # Fix for high A, high B, low C cases that should be 1 (from TOP #1 failures)
            if high_A and high_B and low_C and med_D and med_E and B > 70:
                return 1
            # Fix for low A, high B, high C cases that should be 4 (from TOP #5 failures)
            elif low_A and high_B and high_C and med_D and low_E:
                return 4
            # Fix for balanced medium values that should be 3 (from TOP #10 patterns)
            elif med_A and med_B and med_C and med_D and med_E and B > 50 and D > 55:
                return 3
            # Fix for high A, low B, high C cases that should be 4 (from TOP #7 failures)
            elif high_A and low_B and high_C and med_D and low_E:
                return 4
            # Fix for low A, med B, low C cases that should be 1 (from TOP #11 patterns)
            elif low_A and med_B and low_C and high_D and med_E and E < 65:
                return 1
            # Fix for med A, high B, med C cases that should be 2 (from TOP #12 patterns)
            elif med_A and high_B and med_C and low_D and high_E:
                return 2
            # Fix for high A, high B, low C cases that should be 4 (from TOP #16 failures)
            elif high_A and high_B and low_C and med_D and med_E and B > 80:
                return 4
            # Fix for low A, med B, low C cases that should be 3 (from TOP #17 patterns)
            elif low_A and med_B and low_C and low_D and med_E and B > 50:
                return 3
            
            # Enhanced fix for low B, high C cases that should be 3 or 4 (from TOP #10)
            elif high_C and low_B and E < 50:
                if D < 20 or E < 40:
                    return 3
                else:
                    return 4
            
            # Fix for high B cases that should be 2 (from TOP #23 patterns)
            elif high_B and med_C and not high_E:
                return 2
            elif low_B and med_C and E < 40:
                return 3
            elif high_B and low_C and not high_D:
                return 1
            elif low_A and high_B and high_E:
                return 4
            elif high_A and med_B and low_C and high_D:
                return 3
            elif high_A and low_B and med_C and high_E:
                return 4
            elif med_A and high_B and med_C and D < 20 and E < 30:
                return 2
            elif high_A and med_B and med_C and high_D and E < 20:
                return 4
            elif high_A and high_B and med_C and D < 15 and E > 70:
                return 1
            elif med_A and high_B and med_C and high_D and E < 15:
                return 2
            
            # New mathematical patterns for better generalization (creative innovation)
            if high_D and low_E and C < 20 and B < 30:
                return 3
            elif med_A and med_B and med_C and med_D and med_E and diff_AE < 25:
                return 2
            elif ratio_AD > 2.0 and B < 30 and C < 30:
                return 1
            elif high_B and med_D and med_E and C > 40:
                return 2
            elif low_A and high_D and low_B and C < 40:
                return 4
            
            # Mathematical pattern-based conditions with refined logic (from TOP #11 and #13)
            if avg_all > 60 and diff_BD > 0 and C > 20:
                return 1
            elif E < 10 and high_D:
                return 3
            elif A > 50 and B > 40 and C > 40 and D < 50:
                return 2
            elif A > 80 and B < 20 and C < 10:
                return 1
            elif D > 80 and B < 30 and C < 20:
                return 3
            elif sum_AB > 150 and low_C:
                return 1
            elif (A * B) / (C + 1) > 200 and D < 30:
                return 2
            elif (D + E) / (A + 1) > 2.0 and C < 30:
                return 4
            elif (A + D) > (B + E) and C < 20:
                return 3
            # Creative new patterns for better generalization (innovation from TOP #10 and #13)
            elif ratio_AD > 1.5 and B < 20 and C > 30 and E < 20:
                return 3
            elif B > 90 and C > 70 and D > 50:
                return 2
            elif A < 30 and D > 60 and E < 20 and C > 40:
                return 4
            elif low_B and med_E and (C > 30 or high_C) and not high_D:
                return 3
            elif sum_CD > 100 and B < 20 and E < 30:
                return 4
            elif (B + C) / (D + 1) > 2.0 and A > 50:
                return 2
            else:
                return 1