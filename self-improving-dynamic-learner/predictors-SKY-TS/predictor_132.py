"""
Predictor 132
Generated on: 2025-09-09 20:17:06
Accuracy: 35.70%
"""


# PREDICTOR 132 - Accuracy: 35.70%
# Correct predictions: 3570/10000 (35.70%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if A > 80:
                    return 2
                elif E > 80:
                    return 1
                else:
                    return 4
        else:
            return 2
    else:
        if C >= 50:
            if B >= 70:
                return 2
            elif D < 20:
                return 3
            elif B >= 50:
                return 1
            else:
                return 4
        else:
            if E < 20:
                return 1
            elif B >= 50:
                if E < 60:
                    return 3
                else:
                    return 4
            elif C < 20:
                if D > 50:
                    if A > 50:
                        return 4
                    else:
                        return 3
                else:
                    return 3
            else:
                if D < 40:
                    return 1
                else:
                    if A < 50:
                        return 1
                    elif E > 70:
                        return 4
                    else:
                        return 3