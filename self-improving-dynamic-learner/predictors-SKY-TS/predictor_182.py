"""
Predictor 182
Generated on: 2025-09-09 20:46:35
Accuracy: 52.69%
"""


# PREDICTOR 182 - Accuracy: 52.69%
# Correct predictions: 5269/10000 (52.69%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if C + E > 100:
                    return 2
                else:
                    return 4
        else:
            if D < 50:
                return 2
            else:
                if C + D > 170:
                    return 1
                else:
                    return 2
    else:
        if C > 50:
            if D + E < 70:
                return 4
            else:
                return 1
        else:
            if E < 20:
                if D > 50:
                    if B < 20:
                        return 1
                    else:
                        return 4
                else:
                    return 3
            else:
                if D > 50:
                    return 3
                else:
                    if E > 50:
                        if A < 10:
                            return 2
                        else:
                            return 4
                    else:
                        return 3