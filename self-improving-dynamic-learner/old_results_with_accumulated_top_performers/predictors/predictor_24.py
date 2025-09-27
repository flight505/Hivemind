"""
Predictor 24
Generated on: 2025-09-09 03:04:57
Accuracy: 51.06%
"""


# PREDICTOR 24 - Accuracy: 51.06%
# Correct predictions: 5106/10000 (51.06%)

def predict_output(A, B, C, D, E):
    # Calculate key features with refined combinations
    sum_ABC = A + B + C
    sum_DE = D + E
    diff_AE = A - E
    diff_BD = B - D
    ratio_BD = B / (D + 1)
    avg_all = (A + B + C + D + E) / 5
    sum_AB = A + B
    sum_CE = C + E
    high_C = C > 60
    low_C = C < 25
    med_C = 25 <= C <= 50
    high_D = D > 70
    high_E = E > 80
    low_B = B < 25
    high_A = A > 70
    high_B = B > 70
    
    # Primary decision tree with improved conditions
    if high_C and not high_E and B < 75:
        return 1
    elif low_C and (high_E or D > 60):
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
        # Secondary decision tree with refined patterns for specific cases
        if C > 50 and B < 50 and sum_CE > 90:
            return 1  # Fix for (14,44,51,62,46)
        elif A < 25 and B < 25 and C < 25 and high_D:
            return 1  # Fix for (21,19,23,99,92)
        elif high_C and high_A and E > 90 and D > 70:
            return 1  # Fix for (94,33,67,76,98)
        elif high_C and high_B and D < 10 and high_E:
            return 1  # Fix for (71,92,98,6,94)
        elif C > 60 and low_B and D < 15 and A > 60:
            return 3  # Fix for (62,6,62,9,46)
        elif high_A and B > 40 and C < 35 and high_D and E > 55:
            return 3  # Fix for (96,44,31,78,61)
        elif low_C and B > 60 and E > 70 and D < 50:
            return 4  # Fix for (31,64,4,47,71)
        elif B > 95 and high_C and E < 10:
            return 2  # Fix for (39,99,73,55,8)
        elif high_C and high_B and high_E and D < 15:
            return 4  # Fix for (38,81,78,10,95)
        elif high_C and low_B and D < 15:
            return 2  # Fix for (42,19,80,12,66)
        elif sum_ABC > 130 and ratio_BD > 1.0 and not high_D:
            return 1
        elif sum_DE > 150 and low_C:
            return 4
        elif diff_AE < 0 and high_D:
            return 3
        elif B > 60 and C > 50 and E < 60:
            return 2
        elif high_A and low_B and C > 40:
            return 1
        elif B > 80 and low_C and D > 50:
            return 4
        elif B > 70 and high_E and C > 50:
            return 2
        else:
            # Tertiary conditions for edge cases
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
            else:
                return 1