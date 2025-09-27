"""
Predictor 331
Generated on: 2025-09-09 08:36:16
Accuracy: 40.72%
"""


# PREDICTOR 331 - Accuracy: 40.72%
# Correct predictions: 4072/10000 (40.72%)

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
    
    # Primary decision tree with refined conditions based on cross-cycle learning
    if high_C and not high_E and B < 80:
        # Enhanced condition for high C cases - combines successful patterns with improved logic
        if diff_CB > 25 and low_B and not high_D:
            return 1
        elif high_B and D < 35:
            return 2
        elif low_B and E < 50 and (D < 20 or E < 40):
            return 3
        else:
            return 1
    elif low_C and (high_E or high_D):
        # Improved condition for low C cases - handles edge cases better from cross-cycle analysis
        if sum_AB < 85 or low_A or (high_A and sum_DE > 130):
            return 4
        else:
            return 4
    elif high_D and E < 35 and C < 30:
        return 3
    elif B > 70 and high_C and D < 30:
        return 2
    elif low_B and high_A:
        # Refined condition for low B, high A cases - better C handling
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
        # Improved medium C condition with better E handling
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
            # Enhanced tertiary conditions with targeted fixes from cross-cycle learning
            # Fix for high B, high C cases that should be 2
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
            # Pattern for low A with high