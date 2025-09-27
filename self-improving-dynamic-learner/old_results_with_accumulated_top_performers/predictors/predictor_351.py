"""
Predictor 351
Generated on: 2025-09-09 09:19:39
Accuracy: 57.91%
"""


# PREDICTOR 351 - Accuracy: 57.91%
# Correct predictions: 5791/10000 (57.91%)

def predict_output(A, B, C, D, E):
    high_C = C > 60
    low_C = C < 25
    high_B = B > 70
    high_A = A > 70
    high_E = E > 80
    low_B = B < 25
    med_C = 25 <= C <= 50
    
    if high_C:
        if high_B:
            if high_A:
                return 1
            else:
                return 2
        else:
            return 1
    elif low_C:
        if high_E:
            return 4
        elif low_B:
            return 3
        else:
            return 1
    else:  # med_C
        return 1