"""
Predictor 272
Generated on: 2025-09-09 06:57:01
Accuracy: 21.87%
"""


# PREDICTOR 272 - Accuracy: 21.87%
# Correct predictions: 2187/10000 (21.87%)

def predict_output(A, B, C, D, E):
    # Calculate key features using basic arithmetic operations
    sum_ABC = A + B + C
    sum_DE = D + E
    diff_AE = A - E
    ratio_BD = B / (D + 1)
    high_C = C > 60
    high_E = E > 80
    low_C = C < 25
    high_D = D > 70
    low_B = B < 25
    high_A = A > 70
    low_A = A < 30
    med_C = 25 <= C <= 50
    med_E = 30 <= E <= 60
    low_E = E < 30
    med_A = 30 <= A <= 70
    low_D = D < 20
    med_D = 20 <= D <= 70
    
    # Primary decision tree with refined conditions from top performers
    if high_C and not high_E:
        if low_B and not high_D:
            return 3
        elif high_B and low_D:
            return 2
        else:
            return 1
    elif low_C and (high_E or high_D):
        if low_B or low_A:
            return 4
        else:
            return 4
    elif high_D and E < 35 and C < 30:
        return 3
    elif B > 70 and high_C and D < 30:
        return 2
    elif low_B and high_A:
        if low_C:
            return 3
        else:
            return 4
    elif A > 40 and B > 30 and low_C:
        if D > 60 or E > 70 or sum_DE > 110:
            return 4
        else:
            return 3
    elif med_C and D > 50 and B < 60:
        if E < 45:
            return 1
        else:
            return 3
    else:
        # Secondary decision tree with improved patterns
        if sum_ABC > 130 and ratio_BD > 1.0:
            return 1
        elif sum_DE > 150 and low_C and A < 30:
            return 4
        elif diff_AE < 0 and high_D:
            return 3
        elif B > 60 and C > 50:
            return 2
        else:
            # Tertiary conditions combining fixes from top performers
            if high_B and high_C and (D > 70 or E > 50):
                return 2
            elif high_A and med_C and high_D and E < 40:
                return 3
            elif low_A and high_B and high_C and high_D:
                return 3
            elif med_A and med_B and high_C and E < 15:
                return 4
            elif high_A and med_B and med_C and high_E:
                return 4
            elif low_A and med_B and med_C and not high_D:
                return 1
            elif med_A and high_B and low_C and not high_D:
                return 1
            elif high_A and low_B and med_C and low_D and E < 15:
                return 3
            elif low_A and med_B and med_C and high_D and E < 10:
                return 4
            elif high_C and low_B and E < 50:
                if D < 20 or E < 40:
                    return 3
                else:
                    return 4
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
            elif high_D and low_E and C < 20 and B < 30:
                return 3
            elif med_A and med_B and med_C and med_D and med_E:
                return 2
            elif ratio_AD > 2.0 and B < 30 and C < 30:
                return 1
            elif high_B and med_D and med_E and C > 40:
                return 2
            elif low_A and high_D and low_B and C < 40:
                return 4
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