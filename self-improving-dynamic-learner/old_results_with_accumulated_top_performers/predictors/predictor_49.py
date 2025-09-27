"""
Predictor 49
Generated on: 2025-09-09 03:10:40
Accuracy: 42.24%
"""


# PREDICTOR 49 - Accuracy: 42.24%
# Correct predictions: 4224/10000 (42.24%)

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
    med_B = 25 <= B <= 70
    high_A = A > 70
    high_B = B > 70
    low_A = A < 30
    med_A = 30 <= A <= 70
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
            # Enhanced tertiary conditions with specific fixes
            # Fix for med A, med B, high C, med D, med E cases that should be 2
            if med_A and med_B and high_C and med_D and med_E:
                return 2
            # Fix for med A, med B, high C, low D, low E cases that should be 4
            elif med_A and med_B and high_C and low_D and low_E:
                return 4
            # Fix for high A, low B, med C, med D, med E cases that should be 1
            elif high_A and low_B and med_C and med_D and med_E:
                return 1
            # Fix for med A, med B, med C, med D, low E cases that should be 2
            elif med_A and med_B and med_C and med_D and low_E:
                return 2
            # Fix for low A, low B, high C, low D, med E cases that should be 4
            elif low_A and low_B and high_C and low_D and med_E:
                return 4
            # Fix for med A, med B, low C, med D, med E cases that should be 4
            elif med_A and med_B and low_C and med_D and med_E:
                return 4
            # Fix for med A, high B, med C, med D, low E cases that should be 2
            elif med_A and high_B and med_C and med_D and low_E:
                return 2
            # Fix for low A, low B, high C, low D, med E cases that should be 3
            elif low_A and low_B and high_C and low_D and med_E:
                return 3
            # Fix for high B, high C cases that should be 2 with refined conditions
            elif high_B and high_C and (D > 70 or E > 50):
                return 2
            # Fix for high A, med C, high D cases that should be 3
            elif high_A and med_C and high_D and E < 40:
                return 3
            # Fix for low A, high