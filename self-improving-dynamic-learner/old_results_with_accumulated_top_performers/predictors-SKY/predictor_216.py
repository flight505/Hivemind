"""
Predictor 216
Generated on: 2025-09-09 08:45:32
Accuracy: 49.85%
"""


# PREDICTOR 216 - Accuracy: 49.85%
# Correct predictions: 4985/10000 (49.85%)

def predict_output(A, B, C, D, E):
    if C < 15:
        if B > 80:
            return 2
        elif B > 50 and E > 70:
            return 1
        else:
            return 3
    elif C == 20:
        return 4
    elif C < 70:
        if E > 80:
            return 4
        else:
            return 1
    else:
        if A > 40:
            return 1
        else:
            if B > 20:
                return 2
            else:
                return 1