"""
Predictor 162
Generated on: 2025-09-09 20:33:55
Accuracy: 38.41%
"""


# PREDICTOR 162 - Accuracy: 38.41%
# Correct predictions: 3841/10000 (38.41%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C > 50:
            if E < 10:
                return 4
            else:
                return 2
        else:
            if D < 40:
                return 1
            else:
                if C < 20:
                    if D > 90:
                        return 4
                    else:
                        return 2
                else:
                    if E < 10:
                        return 2
                    else:
                        return 4
    else:
        if C > 50:
            if D < 50 or E < 10:
                return 4
            elif B > 70 and D > 80:
                return 3
            else:
                return 1
        else:
            if E < 20:
                return 1
            else:
                if D < 40 and E < 30:
                    return 1
                else:
                    return 3