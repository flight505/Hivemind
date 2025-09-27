"""
Predictor 191
Generated on: 2025-09-09 05:08:58
Accuracy: 49.94%
"""


# PREDICTOR 191 - Accuracy: 49.94%
# Correct predictions: 4994/10000 (49.94%)

def predict_output(A, B, C, D, E):
    # Calculate key features with refined combinations from cross-cycle analysis
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
    
    # Define threshold categories for pattern recognition (refined from successful patterns)
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
    
    # Primary decision tree with improved conditions based on cross-cycle learning
    if high_C and not high_E and B < 80:
        # Enhanced condition for high C cases - combines TOP #1 and #4 patterns
        if diff_CB > 30 and low_B and not high_D:
            return 1
        elif high_B and D < 40 and sum_AB < 140:
            return 2
        elif low_B and E < 50 and (D < 20 or E < 40):
            return 3
        else:
            return 1
    elif low_C and (high_E or high_D):
        # Improved condition for low C cases - handles high A cases better (fixes TOP #5 failure)
        if sum_AB < 85 or low_A or (high_A and sum_DE > 130):
            return 4
        else:
            return 4
    elif high_D and E < 35 and C < 30:
        return 3
    elif B > 70 and high_C and D < 30:
        return 2
    elif low_B and high_A:
        # Refined condition for low B, high A cases - better C handling (fixes TOP #7 failure)
        if C < 30 or (sum_AB > 80 and not high_C):
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
        # Improved medium C condition with better E handling
        if E < 45 or ratio_AD > 1.1:
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
            # Fix for high A, high B, low C cases that should be 1 (TOP #1 failure pattern)
            if high_A and high_B and low_C and med_D and med_E and B > 70:
                return 1
            # Fix for low A, high B, high C cases that should be 4 (TOP #5 failure)
            elif low_A and high_B and high_C and med_D and low_E:
                return 4
            # Fix for balanced medium values that should be 3 (TOP #10 pattern)
            elif med_A and med_B and med_C and med_D and med_E and B > 50 and D > 55:
                return 3
            # Fix for high A, low B, high C cases that should be 4 (TOP #7 failure)
            elif high_A and low_B and high_C and med_D and low_E:
                return 4
            # Fix for low A, med B, low C cases that should be 1 (TOP #11 pattern)
            elif low_A and med_B and low_C and high_D and med_E and E < 65:
                return 1
            # Fix for med A, high B, med C cases that should be 2 (TOP #12 pattern)
            elif med_A and high_B and med_C and low_D and high_E:
                return 2
            # Fix for high A, high B, low C cases that should be 4 (TOP #16 failure)
            elif high_A and high_B and low_C and med_D and med_E and B > 80:
                return 4
            # Fix for low A, med B, low C cases that should be 3 (TOP #17 pattern)
            elif low_A and med_B and low_C and low_D and med_E and B > 50:
                return 3
            # Fix for high A, low B, med C cases that should be 3 (TOP #23 pattern)
            elif high_A and low_B and med_C and med_D and med_E:
                return 3
            # Fix for med A, high B, low C cases that should be 3 (TOP #25 pattern)
            elif med_A and high_B and low_C and high_D and med_E:
                return 3
            # Fix for low A, med B, low C cases that should be 3 (TOP #26 pattern)
            elif low_A and med_B and low_C and med_D and low_E:
                return 3
            # Fix for low A, low B, low C cases that should be 3 (TOP #27 pattern)
            elif low_A and low_B and low_C and med_D and low_E:
                return 3
            # Fix for high A, low B, low C cases that should be 3 (TOP #28 pattern)
            elif high_A and low_B and low_C and low_D and med_E:
                return 3
            # Fix for med A, high B, low C cases that should be 4 (TOP #29 pattern)
            elif med_A and high_B and low_C and high_D and high_E:
                return 4
            # Fix for low A, low B, high C cases that should be 1 (TOP #30 pattern)
            elif low_A and low_B and high_C and med_D and med_E:
                return 1
            # Fix for low A, low B, med C cases that should be 1 (TOP #31 pattern)
            elif low_A and low_B and med_C and high_D and med_E:
                return 1
            
            # Enhanced fix for low B, high C cases that should be 3 or 4 (TOP #10 pattern)
            elif high_C and low_B and E < 50:
                if D < 20 or E < 40 or sum_ADE < 105:
                    return 3
                elif B < 10 and C > 70:
                    return 4
                else:
                    return 4
            
            # Refined conditions for high B cases (TOP #23 pattern)
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
            
            # Additional pattern-based fixes for common error types (TOP #11 and #13)
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
            
            # Innovative mathematical patterns for better generalization (creative combination)
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
            
            # Mathematical pattern-based conditions with refined logic (TOP #11 and #13)
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
            # Enhanced creative patterns with new mathematical insights (TOP #10 and #13)
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