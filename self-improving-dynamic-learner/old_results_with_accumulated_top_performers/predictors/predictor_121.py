"""
Predictor 121
Generated on: 2025-09-09 04:11:03
Accuracy: 49.32%
"""


# PREDICTOR 121 - Accuracy: 49.32%
# Correct predictions: 4932/10000 (49.32%)

def predict_output(A, B, C, D, E):
    # Calculate key mathematical features using basic arithmetic
    sum_ABC = A + B + C
    sum_DE = D + E
    diff_AE = A - E
    diff_BD = B - D
    ratio_BD = B / (D + 1)
    ratio_AD = A / (D + 1)
    ratio_BE = B / (E + 1)
    avg_all = (A + B + C + D + E) / 5
    sum_AB = A + B
    sum_CD = C + D
    sum_BE = B + E
    diff_CB = C - B
    sum_ADE = A + D + E
    
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
    
    # Primary decision tree with refined conditions from successful patterns
    if high_C and not high_E and B < 80:
        if diff_CB > 25 and low_B and not high_D:
            return 1
        elif high_B and D < 35:
            return 2
        elif low_B and E < 50 and (D < 20 or E < 40):
            return 3
        else:
            return 1
    elif low_C and (high_E or high_D):
        if sum_AB < 85 or low_A or ratio_BE > 0.8:
            return 4
        else:
            return 1
    elif high_D and E < 35 and C < 30:
        return 3
    elif B > 70 and high_C and D < 30:
        return 2
    elif low_B and high_A:
        if C > 35 or sum_AB > 75:
            return 1
        else:
            return 4
    elif A > 40 and B > 30 and low_C:
        if D > 60 or E > 70 or sum_DE > 110:
            return 4
        else:
            return 3
    elif med_C and D > 50 and B < 60:
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
            # Enhanced tertiary conditions with targeted fixes for specific error patterns
            # Fix for high A, high B, low C, low D, med E cases that should be 1
            if high_A and high_B and low_C and low_D and med_E and B > 70:
                return 1
            # Fix for low A, low B, high C, low D, med E cases that should be 3
            elif low_A and low_B and high_C and low_D and med_E and E < 25:
                return 3
            # Fix for low A, high B, med C, low D, high E cases that should be 2
            elif low_A and high_B and med_C and low_D and high_E and C > 55:
                return 2
            # Fix for high A, high B, low C, med D, med E cases that should be 4
            elif high_A and high_B and low_C and med_D and med_E and B > 90:
                return 4
            # Fix for low A, high B, high C, low D, low E cases that should be 2
            elif low_A and high_B and high_C and low_D and low_E and B > 95:
                return 2
            # Fix for low A, med B, med C, high D, med E cases that should be 1
            elif low_A and med_B and med_C and high_D and med_E and C < 55:
                return 1
            # Fix for med A, med B, low C, low D, med E cases that should be 3
            elif med_A and med_B and low_C and low_D and med_E and B > 50:
                return 3
            # Fix for med A, high B, high C, high D, low E cases that should be 2
            elif med_A and high_B and high_C and high_D and low_E and B > 80:
                return 2
            # Fix for med A, med B, med C, med D, low E cases that should be 4
            elif med_A and med_B and med_C and med_D and low_E and E < 10:
                return 4
            # Fix for low A, med B, low C, med D, med E cases that should be 3
            elif low_A and med_B and low_C and med_D and med_E and D > 45:
                return 3
            # Fix for low A, low B, med C, high D, med E cases that should be 1
            elif low_A and low_B and med_C and high_D and med_E:
                return 1
            # Fix for high A, low B, med C, med D, med E cases that should be 3
            elif high_A and low_B and med_C and med_D and med_E:
                return 3
            # Fix for med A, high B, low C, high D, med E cases that should be 3
            elif med_A and high_B and low_C and high_D and med_E:
                return 3
            # Fix for low A, med B, low C, med D, low E cases that should be 3
            elif low_A and med_B and low_C and med_D and low_E:
                return 3
            # Fix for low A, low B, low C, med D, low E cases that should be 3
            elif low_A and low_B and low_C and med_D and low_E:
                return 3
            # Fix for high A, low B, low C, low D, med E cases that should be 3
            elif high_A and low_B and low_C and low_D and med_E:
                return 3
            # Fix for med A, high B, low C, high D, high E cases that should be 4
            elif med_A and high_B and low_C and high_D and high_E:
                return 4
            # Fix for low A, low B, high C, med D, med E cases that should be 1
            elif low_A and low_B and high_C and med_D and med_E:
                return 1
            # Fix for low A, low B, med C, high D, med E cases that should be 1
            elif low_A and low_B and med_C and high_D and med_E:
                return 1
            
            # Enhanced fix for low B, high C cases with refined logic
            elif high_C and low_B and E < 50:
                if D < 20 or E < 40 or sum_ADE < 105:
                    return 3
                elif B < 10 and C > 70:
                    return 4
                else:
                    return 4
            
            # Refined conditions for high B cases
            elif high_B and med_C and not high_E:
                if D < 30 or sum_AB > 140:
                    return 2
                else:
                    return 1
            elif low_B and med_C and E < 40:
                if A > 60 or D > 60:
                    return 3
                else:
                    return 1
            elif high_B and low_C and not high_D:
                if E > 60 or sum_DE > 100:
                    return 1
                else:
                    return 4
            elif low_A and high_B and high_E:
                return 4
            elif high_A and med_B and low_C and high_D:
                return 3
            elif high_A and low_B and med_C and high_E:
                if D < 50:
                    return 4
                else:
                    return 1
            elif med_A and high_B and med_C and D < 20 and E < 30:
                return 2
            elif high_A and med_B and med_C and high_D and E < 20:
                return 4
            elif high_A and high_B and med_C and D < 15 and E > 70:
                return 1
            elif med_A and high_B and med_C and high_D and E < 15:
                return 2
            
            # Additional pattern-based fixes for common error types
            if high_B and high_C and (D > 70 or E > 50):
                if sum_CD > 120:
                    return 1
                else:
                    return 2
            elif high_A and med_C and high_D and E < 40:
                return 3
            elif low_A and high_B and high_C and high_D:
                if E > 50:
                    return 3
                else:
                    return 2
            elif med_A and med_B and high_C and E < 15:
                return 4
            elif high_A and med_B and med_C and high_E:
                if D < 40:
                    return 4
                else:
                    return 1
            elif low_A and med_B and med_C and not high_D:
                if sum_BE > 100:
                    return 2
                else:
                    return 1
            elif med_A and high_B and low_C and not high_D:
                return 1
            elif high_A and low_B and med_C and low_D and E < 15:
                return 3
            elif low_A and med_B and med_C and high_D and E < 10:
                return 4
            
            # Innovative mathematical patterns for better generalization
            if high_D and low_E and C < 20 and B < 30:
                return 3
            elif med_A and med_B and med_C and med_D and med_E and diff_AE < 25:
                if B > 45 and D > 50:
                    return 3
                else:
                    return 2
            elif ratio_AD > 2.0 and B < 30 and C < 30:
                return 1
            elif high_B and med_D and med_E and C > 40:
                if sum_CD > 90:
                    return 1
                else:
                    return 2
            elif low_A and high_D and low_B and C < 40:
                return 4
            
            # Mathematical pattern-based conditions with creative combinations
            if avg_all > 60 and diff_BD > 0 and C > 20 and B < 40:
                return 1
            elif E < 10 and high_D:
                return 3
            elif A > 50 and B > 40 and C > 40 and D < 50:
                if sum_AB > 90:
                    return 2
                else:
                    return 1
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
                if A > 70:
                    return 3
                else:
                    return 1
            # Enhanced creative patterns with new mathematical insights
            elif ratio_AD > 1.5 and B < 20 and C > 30 and E < 20:
                return 3
            elif B > 90 and C > 70 and D > 50:
                if E < 40:
                    return 2
                else:
                    return 1
            elif A < 30 and D > 60 and E < 20 and C > 40:
                return 4
            elif low_B and med_E and (C > 30 or high_C) and not high_D:
                return 3
            elif sum_CD > 100 and B < 20 and E < 30:
                return 4
            elif (B + C) / (D + 1) > 2.0 and A > 50:
                return 2
            # New innovative mathematical combinations for edge cases
            elif sum_BE > 140 and high_C and D < 30:
                return 2
            elif diff_CB > 30 and low_B and high_D:
                return 1
            elif sum_AB < 60 and high_C and low_E:
                return 4
            elif med_C and high_B and low_D and E > 60:
                return 2
            elif low_C and high_D and med_E and B > 50 and A < 20:
                return 3
            elif sum_ADE > 180 and low_C and high_B:
                return 1
            elif (C * E) / (B + 1) < 50 and high_D:
                return 3
            else:
                return 1