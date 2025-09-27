"""
Predictor 71
Generated on: 2025-09-09 03:30:28
Accuracy: 53.57%
"""


# PREDICTOR 71 - Accuracy: 53.57%
# Correct predictions: 5357/10000 (53.57%)

def predict_output(A, B, C, D, E):
    # Calculate key mathematical features using basic arithmetic
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
    diff_AE_abs = abs(A - E)
    
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
        if diff_CB > 30 and low_B:
            return 1
        elif high_B and D < 40:
            return 2
        else:
            return 1
    elif low_C and (high_E or high_D):
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
            # Enhanced tertiary conditions with creative mathematical fixes
            # Pattern for high A with low B and medium C that should be 1
            if high_A and low_B and med_C and not high_E:
                if D < 50 or E < 40:
                    return 1
                else:
                    return 3
            # Pattern for balanced medium values that should be 3
            elif med_A and med_B and med_C and med_D and med_E and B > 50 and D > 55:
                return 3
            # Pattern for low A with medium B and low C that should be 1
            elif low_A and med_B and low_C and high_D and med_E and E < 65:
                return 1
            # Pattern for medium A with high B and medium C that should be 2
            elif med_A and high_B and med_C and low_D and high_E:
                return 2
            # Pattern for high A with high B and low C that should be 4
            elif high_A and high_B and low_C and med_D and med_E and B > 80:
                return 4
            # Pattern for low A with medium B and low C that should be 3
            elif low_A and med_B and low_C and low_D and med_E and B > 50:
                return 3
            # Pattern for medium A with low B and low C that should be 3
            elif med_A and low_B and low_C and low_D and low_E:
                return 3
            # Pattern for low A with high B and medium C that should be 1
            elif low_A and high_B and med_C and med_D and med_E and C < 30:
                return 1
            # Pattern for low A with high B and medium C that should be 2
            elif low_A and high_B and med_C and high_D and low_E and B > 95:
                return 2
            # Pattern for medium A with medium B and medium C that should be 2
            elif med_A and med_B and med_C and low_D and high_E and C > 50:
                return 2
            # Pattern for low A with low B and high C that should be 4
            elif low_A and low_B and high_C and med_D and med_E:
                return 4
            # Pattern for high A with medium B and medium C that should be 4
            elif high_A and med_B and med_C and med_D and high_E:
                return 4
            # Pattern for low A with medium B and high C that should be 3
            elif low_A and med_B and high_C and low_D and low_E:
                return 3
            # Pattern for low A with low B and medium C that should be 2
            elif low_A and low_B and med_C and low_D and high_E:
                return 2
            # Pattern for low A with low B and low C that should be 1
            elif low_A and low_B and low_C and med_D and med_E:
                return 1
            # Pattern for low A with high B and high C that should be 2
            elif low_A and high_B and high_C and med_D and high_E:
                return 2
            # Pattern for low A with high B and medium C that should be 4
            elif low_A and high_B and med_C and low_D and med_E:
                return 4
            # Pattern for low A with medium B and medium C that should be 2
            elif low_A and med_B and med_C and low_D and (60 <= E <= 80):
                return 2
            # Pattern for high A with high B and high C that should be 4
            elif high_A and high_B and high_C and low_D and high_E:
                return 4
            # Pattern for high A with medium B and low C that should be 1
            elif high_A and med_B and low_C and low_D and med_E:
                return 1
            # Pattern for medium A with low B and low C that should be 1
            elif med_A and low_B and low_C and high_D and low_E:
                return 1
            # Pattern for medium A with medium B and low C that should be 3
            elif med_A and med_B and low_C and low_D and med_E:
                return 3
            # Pattern for high A with medium B and low C that should be 1
            elif high_A and med_B and low_C and low_D and high_E:
                return 1
            # Pattern for medium A with low B and medium C that should be 2
            elif med_A and low_B and med_C and low_D and high_E:
                return 2
            
            # Enhanced fix for low B, high C cases that should be 3 or 4
            elif high_C and low_B and E < 50:
                if D < 20 or E < 40:
                    return 3
                else:
                    return 4
            
            # Fix for high B cases that should be 2
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
            
            # New mathematical patterns for better generalization
            if high_D and low_E and C < 20 and B < 30:
                return 3
            elif med_A and med_B and med_C and med_D and med_E and diff_AE_abs < 20:
                return 2
            elif ratio_AD > 2.0 and B < 30 and C < 30:
                return 1
            elif high_B and med_D and med_E and C > 40:
                return 2
            elif low_A and high_D and low_B and C < 40:
                return 4
            
            # Mathematical pattern-based conditions with refined logic
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
            # Enhanced creative patterns
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
            # New innovative mathematical combinations
            elif sum_BE > 140 and high_C and D < 30:
                return 2
            elif diff_CB > 30 and low_B and high_D:
                return 1
            elif sum_AB < 60 and high_C and low_E:
                return 4
            elif med_C and high_B and low_D and E > 60:
                return 2
            elif low_C and high_D and med_E and B > 50:
                return 3
            else:
                return 1