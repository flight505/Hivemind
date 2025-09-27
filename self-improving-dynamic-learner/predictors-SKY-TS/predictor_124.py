"""
Predictor 124
Generated on: 2025-09-09 20:11:38
Accuracy: 48.95%
"""


# PREDICTOR 124 - Accuracy: 48.95%
# Correct predictions: 4895/10000 (48.95%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if C > 45:
                    return 2
                else:
                    return 4
        else:
            if C > 90:
                return 1
            else:
                return 2
    else:
        if C > 50:
            if A > 80:
                return 1
            elif E > 50:
                return 1
            else:
                return 4
        else:
            if E > 70:
                return 4
            elif E < 20:
                return 1
            elif D > 50 and E < 40:
                return 1
            else:
                return 3