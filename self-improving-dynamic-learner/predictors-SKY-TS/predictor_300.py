"""
Predictor 300
Generated on: 2025-09-09 21:39:25
Accuracy: 50.80%
"""


# PREDICTOR 300 - Accuracy: 50.80%
# Correct predictions: 5080/10000 (50.80%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C >= 50:
            return 2
        else:
            if D < 35:
                return 1
            elif D > 95 and E > 80:
                return 3
            else:
                return 4
    else:
        if C > 50:
            if E < 20:
                return 4
            elif D < 20:
                return 3
            else:
                return 1
        else:
            if E > 50 and D < 30 and B < 30:
                return 4
            elif D < 40:
                if A > 60:
                    return 1
                else:
                    return 3
            else:
                if E < 20 or B < 20:
                    return 1
                else:
                    return 3