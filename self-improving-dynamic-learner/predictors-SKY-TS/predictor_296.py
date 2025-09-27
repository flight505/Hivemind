"""
Predictor 296
Generated on: 2025-09-09 21:37:20
Accuracy: 49.55%
"""


# PREDICTOR 296 - Accuracy: 49.55%
# Correct predictions: 4955/10000 (49.55%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                return 4
        else:
            return 2
    else:
        if C > 50:
            if E < 20:
                return 4
            else:
                return 1
        else:
            if E < 20:
                if E < 10 or C < 10:
                    return 3
                else:
                    return 1
            else:
                if D > 80:
                    return 1
                elif A > 60 and D < 10:
                    return 1
                elif A > 70 and C < 30:
                    return 4
                else:
                    return 3