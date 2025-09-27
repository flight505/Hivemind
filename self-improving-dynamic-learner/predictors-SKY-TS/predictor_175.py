"""
Predictor 175
Generated on: 2025-09-09 20:42:15
Accuracy: 47.44%
"""


# PREDICTOR 175 - Accuracy: 47.44%
# Correct predictions: 4744/10000 (47.44%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C >= 50:
            if E < 10:
                return 1
            else:
                return 2
        else:
            if D > 45:
                return 4
            else:
                return 1
    else:
        if C > 50:
            if E > 50:
                return 1
            else:
                if A > 60:
                    return 1
                else:
                    return 4
        else:
            if E < 20:
                return 1
            else:
                if B > 70 or (A > 90 and D < 30):
                    return 1
                elif C < 10 and D > 90:
                    return 4
                elif E > 80 and D < 10:
                    return 1
                else:
                    return 3