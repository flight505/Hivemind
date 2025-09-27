"""
Predictor 96
Generated on: 2025-09-09 19:57:12
Accuracy: 49.47%
"""


# PREDICTOR 96 - Accuracy: 49.47%
# Correct predictions: 4947/10000 (49.47%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C >= 50:
            return 2
        else:
            if D < 40:
                return 1
            else:
                if E > 80:
                    return 2
                else:
                    return 4
    else:
        if C > 50:
            if E < 20:
                return 4
            else:
                if D < 20:
                    if E < 50:
                        return 4
                    else:
                        if A > 50:
                            return 1
                        else:
                            return 2
                else:
                    return 1
        else:
            if E < 20:
                return 1
            else:
                if B >= 70:
                    return 1
                elif E > 90:
                    return 1
                elif D > 50 and B < 20:
                    return 1
                elif A > 70 and E > 70:
                    return 4
                else:
                    return 3