"""
Predictor 75
Generated on: 2025-09-09 19:45:42
Accuracy: 50.44%
"""


# PREDICTOR 75 - Accuracy: 50.44%
# Correct predictions: 5044/10000 (50.44%)

def predict_output(A, B, C, D, E):
    if C >= 50:
        if B < 40:
            if E > 20:
                return 1
            else:
                return 4
        elif B >= 90:
            return 2
        else:
            return 1
    else:
        if B >= 80:
            if D < 30:
                return 1
            else:
                return 4
        else:
            if E < 20:
                if A > 50:
                    return 1
                else:
                    return 4
            else:
                if B >= 70 and E > 50:
                    return 1
                elif B > 10 and D < 40:
                    return 4
                else:
                    return 3