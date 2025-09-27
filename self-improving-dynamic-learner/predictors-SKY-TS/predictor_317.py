"""
Predictor 317
Generated on: 2025-09-09 21:48:45
Accuracy: 44.07%
"""


# PREDICTOR 317 - Accuracy: 44.07%
# Correct predictions: 4407/10000 (44.07%)

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
                return 1
        else:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    if B > 40:
                        return 1
                    else:
                        return 3
            else:
                if D > 50:
                    if B > 60:
                        if C < 10 and E <= 25:
                            return 4
                        elif E < 30:
                            return 3