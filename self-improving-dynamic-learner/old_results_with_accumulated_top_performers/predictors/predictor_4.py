"""
Predictor 4
Generated on: 2025-09-09 03:03:30
Accuracy: 40.01%
"""


# PREDICTOR 4 - Accuracy: 40.01%
# Correct predictions: 4001/10000 (40.01%)

def predict_output(A, B, C, D, E):
    # Calculate key features
    sum_CDE = C + D + E
    diff_A_B = A - B
    ratio_AE = A / (E + 1)
    high_C = C > 60
    high_D = D > 80
    low_B = B < 30
    high_E = E > 70
    low_E = E < 20
    high_A = A > 50
    
    if high_C and not low_B:
        return 1
    elif high_D and low_E:
        return 3
    elif high_E and B > 70:
        return 4
    elif C > 80 and low_B:
        return 4
    elif sum_CDE > 200 and A < 40:
        return 2
    else:
        # Secondary decision logic
        if ratio_AE > 1.5 and high_A:
            return 1
        elif diff_A_B < -20 and high_D:
            return 3
        elif B > 80 and C < 30:
            return 1
        elif high_E and D < 30:
            return 4
        else:
            return 2