"""
Predictor 253
Generated on: 2025-09-09 21:19:40
Accuracy: 38.73%
"""


# PREDICTOR 253 - Accuracy: 38.73%
# Correct predictions: 3873/10000 (38.73%)

def predict_output(A, B, C, D, E):
    if B >= 68:
        if C > 70 and E > 60:
            return 2
        elif C < 40:
            if D < 30:
                return 1
            else:
                if E > 80:
                    return 1
                else:
                    return 4
        else:
            return 4
    else:
        if C > 50:
            if E < 20:
                if D < 10:
                    return 3
                else:
                    return 4
            else:
                if D <= 40:
                    return 4
                else:
                    return 1
        else:
            if E < 20:
                return 1
            else:
                if A < 20:
                    return 1
                else:
                    return 3