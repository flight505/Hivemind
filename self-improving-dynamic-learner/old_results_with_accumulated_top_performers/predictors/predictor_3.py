"""
Predictor 3
Generated on: 2025-09-09 03:03:27
Accuracy: 40.54%
"""


# PREDICTOR 3 - Accuracy: 40.54%
# Correct predictions: 4054/10000 (40.54%)

def predict_output(A, B, C, D, E):
    # Calculate key features
    sum_BC = B + C
    sum_ABC = A + B + C
    diff_DE = D - E
    high_B = B > 80
    low_A = A < 50
    high_C = C > 70
    high_D = D > 70
    low_E = E < 40
    
    if high_B and sum_BC > 140:
        return 2
    elif high_C and low_A and high_D:
        return 2
    elif low_E and D > 40 and A > 40:
        return 4
    elif high_B and C < 30:
        return 1
    elif diff_DE > 30 and E < 50:
        return 3
    elif low_A and C > 50 and B < 20:
        return 1
    else:
        # Secondary decision logic
        if sum_ABC > 150 and B > 50:
            return 1
        elif E > 80 and D < 30:
            return 4
        elif A > 70 and D > 60:
            return 3
        else:
            return 1