"""
Predictor 5
Generated on: 2025-09-09 18:58:34
Accuracy: 47.27%
"""


# PREDICTOR 5 - Accuracy: 47.27%
# Correct predictions: 4727/10000 (47.27%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if D + E > 100:
                    return 4
                else:
                    return 2
        else:
            if D < 50:
                return 1
            else:
                return 2
    else:
        if C > 50:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    return 4
            else:
                if A < 20:
                    return 3
                else:
                    return 1
        else:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    return 4
            else:
                if E > 80:
                    return 4
                elif E < 30:
                    return 1
                else:
                    return 3