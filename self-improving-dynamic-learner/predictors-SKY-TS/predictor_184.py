"""
Predictor 184
Generated on: 2025-09-09 20:46:35
Accuracy: 44.22%
"""


# PREDICTOR 184 - Accuracy: 44.22%
# Correct predictions: 4422/10000 (44.22%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if E > 80:
                    return 2
                else:
                    return 4
        else:
            if D < 50:
                return 2
            else:
                if E > 60:
                    return 2
                else:
                    return 1
    else:
        if C > 50:
            if D + E > 100:
                return 1
            else:
                return 4
        else:
            if E < 20:
                if D > 50:
                    if C > 20:
                        return 1
                    else:
                        return 4
                else:
                    return 3
            else:
                if D > 50:
                    return 3
                else:
                    if A > 80 and E > 50:
                        return 4
                    elif A < 20 and E > 60:
                        return 2
                    else:
                        return 3