"""
Predictor 6
Generated on: 2025-09-09 18:58:34
Accuracy: 43.20%
"""


# PREDICTOR 6 - Accuracy: 43.20%
# Correct predictions: 4320/10000 (43.20%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if E > 50 or C < 20:
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
                if D < 20 or A < 20:
                    return 3
                else:
                    return 1
        else:
            if E < 20:
                if D >= 50:
                    return 1
                else:
                    return 4
            else:
                if D + E > 150:
                    return 4
                elif E < 30:
                    return 1
                else:
                    return 3