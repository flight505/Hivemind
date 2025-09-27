"""
Predictor 142
Generated on: 2025-09-09 20:24:26
Accuracy: 48.60%
"""


# PREDICTOR 142 - Accuracy: 48.60%
# Correct predictions: 4860/10000 (48.60%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C >= 50:
            if C > 70 and (D > 50 or E > 50):
                return 2
            else:
                return 1
        else:
            if D > 40 or E > 50:
                return 4
            else:
                return 1
    else:
        if C >= 50:
            if D > 50:
                return 1
            elif E > 50:
                if B >= 60 and C < 70:
                    return 2
                else:
                    return 1
            else:
                if A < 20:
                    return 3
                else:
                    return 4
        else:
            if B < 20 and D > 50 and A > 50:
                return 1
            else:
                return 3