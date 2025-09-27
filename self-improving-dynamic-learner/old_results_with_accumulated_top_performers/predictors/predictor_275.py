"""
Predictor 275
Generated on: 2025-09-09 07:01:14
Accuracy: 45.61%
"""


# PREDICTOR 275 - Accuracy: 45.61%
# Correct predictions: 4561/10000 (45.61%)

def predict_output(A, B, C, D, E):
    high_A = A > 70
    high_B = B > 70
    high_C = C > 60
    high_D = D > 70
    high_E = E > 80
    low_A = A < 30
    low_B = B < 25
    low_C = C < 25
    low_D = D < 20
    med_A = 30 <= A <= 70
    med_B = 25 <= B <= 70
    med_C = 25 <= C <= 50
    med_D = 20 <= D <= 70
    med_E = 30 <= E <= 60
    if low_B and low_C:
        if high_D:
            if high_A:
                return 3
            else:
                return 1
        else:
            return 3
    elif high_E:
        return 4
    elif med_C:
        if high_E:
            return 4
        elif high_B:
            return 3
        else:
            return 1
    elif high_C:
        if low_B:
            if high_A:
                return 3
            else:
                return 1
        else:
            if high_B:
                if low_D:
                    return 1
                else:
                    return 2
            else:
                return 1
    else:
        return 1