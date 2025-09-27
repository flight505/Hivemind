"""
Predictor 44
Generated on: 2025-09-09 19:25:48
Accuracy: 48.31%
"""


# PREDICTOR 44 - Accuracy: 48.31%
# Correct predictions: 4831/10000 (48.31%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                if E > 50:
                    return 4
                else:
                    return 1
            else:
                if D > 90 or E > 50:
                    return 4
                else:
                    return 1
        else:
            if B > 90:
                return 2
            else:
                return 1
    else:
        if C >= 50:
            if D + E > 100:
                return 1
            else:
                return 4
        else:
            if E < 20:
                if D > 60:
                    return 1
                else:
                    return 2
            else:
                if D > 50:
                    if B < 20 and D > 90:
                        return 1
                    else:
                        return 3
                else:
                    if E > 50:
                        if A > 90:
                            return 4
                        else:
                            return 1
                    else:
                        if A > 70:
                            return 1
                        else:
                            return 3