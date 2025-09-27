"""
Predictor 119
Generated on: 2025-09-09 20:09:30
Accuracy: 42.72%
"""


# PREDICTOR 119 - Accuracy: 42.72%
# Correct predictions: 4272/10000 (42.72%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C >= 50:
            return 2
        else:
            if D > 40 or E > 40:
                return 4
            else:
                return 1
    else:
        if C > 50:
            if E > 50:
                return 1
            else:
                return 4
        else:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    return 3
            else:
                if D > 90 or (E > 45 and D < 40) or (D > 70 and E > 70 and B < 40):
                    return 1
                else:
                    return 3