"""
Predictor 255
Generated on: 2025-09-09 21:19:40
Accuracy: 41.55%
"""


# PREDICTOR 255 - Accuracy: 41.55%
# Correct predictions: 4155/10000 (41.55%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C >= 50:
            return 2
        else:
            if D < 35:
                return 1
            elif E > 60:
                return 1
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
                if D + E > 100:
                    return 1
                else:
                    return 4
        else:
            if E < 20:
                return 1
            else:
                if C > 30 and A < 20:
                    return 1
                else:
                    return 3