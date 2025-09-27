"""
Predictor 41
Generated on: 2025-09-09 03:08:34
Accuracy: 53.21%
"""


# PREDICTOR 41 - Accuracy: 53.21%
# Correct predictions: 5321/10000 (53.21%)

def predict_output(A, B, C, D, E):
    # Calculate key features with refined combinations
    sum_ABC = A + B + C
    sum_DE = D + E
    diff_AE = A - E
    diff_BD = B - D
    ratio_BD = B / (D + 1)
    ratio_AD = A / (D + 1)
    avg_all = (A + B + C + D + E) / 5
    sum_AB = A + B
    sum_CD = C + D
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
    med_D = 20 <= D <= 70
    low_E = E < 30
    med_E = 30 <= E <= 60
    
    # Primary decision tree with improved conditions
    if high_C and not high_E and B < 80:
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
        # Secondary decision tree with refined patterns
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
            # Fix for high B, high C cases that should be 2 with refined conditions
            if high_B and high_C and (D > 70 or E > 50):
                return 2
            # Fix for high A, med C, high D cases that should be 3
            elif high_A and med_C and high_D and E < 40:
                return 3
            # Fix for low A, high B, high C cases that should be 3
            elif low_A and high_B and high_C and high_D:
                return 3
            # Fix for med A, med B, high C cases that should be 4
            elif med_A and med_B and high_C and E < 15:
                return 4
            # Fix for high A, med B, med C cases that should be 4
            elif high_A and med_B and med_C and high_E:
                return 4
            # Fix for low A, med B, med C cases that should be 1
            elif low_A and med_B and med_C and not high_D:
                return 1
            # Fix for med A, high B, low C cases that should be 1
            elif med_A and high_B and low_C and not high_D:
                return 1
            # Fix for high A, low B, med C cases that should be 3
            elif high_A and low_B and med_C and low_D and E < 15:
                return 3
            # Fix for low A, med B, med C cases that should be 4
            elif low_A and med_B and med_C and high_D and E < 10:
                return 4
            # Enhanced fix for low B, high C cases that should be 3 or 4
            elif high_C and low_B and E < 50:
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
            # Fix for high A, low B, med C cases that should be 4
            elif high_A and low_B and med_C and high_E:
                return 4
            # Fix for med A, high B, med C cases that should be 2
            elif med_A and high_B and med_C and D < 20 and E < 30:
                return 2
            # Fix for high A, med B, med C cases that should be 4
            elif high_A and med_B and med_C and high_D and E < 20:
                return 4
            # Fix for high A, high B, med C cases that should be 1
            elif high_A and high_B and med_C and D < 15 and E > 70:
                return 1
            # Fix for med A, high B, med C cases that should be 2
            elif med_A and high_B and med_C and high_D and E < 15:
                return 2
            # New mathematical pattern for high D, low E cases
            elif high_D and low_E and C < 20 and B < 30:
                return 3
            # New pattern for balanced inputs that should be 2
            elif med_A and med_B and med_C and med_D and med_E:
                return 2
            # Pattern for very high A relative to others
            elif ratio_AD > 2.0 and B < 30 and C < 30:
                return 1
            # Pattern for high B with moderate D and E
            elif high_B and med_D and med_E and C > 40:
                return 2
            # Pattern for low A with high D and low B
            elif low_A and high_D and low_B and C < 40:
                return 4
            # Mathematical pattern-based conditions
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
            # Creative new patterns for better generalization
            elif ratio_AD > 1.5 and B < 20 and C > 30 and E < 20:
                return 3
            elif B > 90 and C > 70 and D > 50:
                return 2
            elif A < 30 and D > 60 and E < 20 and C > 40:
                return 4
            elif low_B and med_E and (C > 30 or high_C):
                return 3
            elif sum_CD > 100 and B < 20 and E < 30:
                return 4
            elif (B + C) / (D + 1) > 2.0 and A > 50:
                return 2
            else:
                return 1