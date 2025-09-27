"""
Predictor 271
Generated on: 2025-09-09 21:27:39
Accuracy: 46.59%
"""


# PREDICTOR 271 - Accuracy: 46.59%
# Correct predictions: 4659/10000 (46.59%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D > 50:
                if E < 20:
                    return 4
                else:
                    return 2
            elif E > 50:
                return 4
            elif E < 20:
                return 1
            else:
                return 2
        else:
            return 2
    else:
        if C >= 50:
            if D >= 30:
                return 1
            else:
                if B < 50:
                    return 4
                else:
                    return 1
        else:
            if E < 20:
                if D < 20:
                    return 3
                else:
                    return 1
            else:
                if A < 30 and E > 70:
                    return 1
                else:
                    return 3