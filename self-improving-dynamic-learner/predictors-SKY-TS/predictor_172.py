"""
Predictor 172
Generated on: 2025-09-09 20:39:19
Accuracy: 49.40%
"""


# PREDICTOR 172 - Accuracy: 49.40%
# Correct predictions: 4940/10000 (49.40%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C >= 50:
            return 2
        else:
            if D < 40:
                return 1
            else:
                if D > 50 and E < 20:
                    return 4
                elif 50 < E < 60:
                    return 4
                elif E > 70:
                    return 1
                else:
                    return 1
    else:
        if C > 50:
            if D < 30:
                if E < 20:
                    return 4
                else:
                    return 1
            else:
                return 1
        else:
            if E < 20:
                return 1
            else:
                if C < 10 and D > 40 and E < 50:
                    return 1
                elif C < 10 and D > 50 and E > 50:
                    return 4
                elif E > 70:
                    if D < 20:
                        return 1
                    elif B > 70 and A < 60:
                        return 4
                    elif A < 50:
                        return 2
                    else:
                        return 4
                else:
                    return 3