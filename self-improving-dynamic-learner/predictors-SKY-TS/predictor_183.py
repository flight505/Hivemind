"""
Predictor 183
Generated on: 2025-09-09 20:46:35
Accuracy: 51.80%
"""


# PREDICTOR 183 - Accuracy: 51.80%
# Correct predictions: 5180/10000 (51.80%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if E > 70:
                    return 2
                else:
                    return 4
        else:
            if D < 50:
                return 2
            else:
                if C > 90:
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