"""
Predictor 171
Generated on: 2025-09-09 20:39:19
Accuracy: 50.33%
"""


# PREDICTOR 171 - Accuracy: 50.33%
# Correct predictions: 5033/10000 (50.33%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 4 if E > 60 else 1
            else:
                if E < 20:
                    return 4 if A > 50 else 2
                elif E > 50:
                    return 1 if D > 80 else 4
                else:
                    return 1 if D > 70 else 2
        else:
            if D < 50:
                return 2
            else:
                if D > 90:
                    return 3 if 30 <= E <= 70 else 2
                elif E <= 25 or A > 60 or E > 80:
                    return 1
                else:
                    return 2
    else:
        if C > 50:
            if E < 20:
                return 1 if A > 90 or D > 50 else 4
            else:
                if D < 20:
                    return 1 if A > 90 else 4
                else:
                    return 1
        else:
            if E < 20:
                if D > 50:
                    return 3 if B > 50 or C < 10 else 1
                else:
                    return 1 if A > 80 else (4 if E < 10 else 3)
            else:
                if D > 50:
                    if E > 60:
                        return 3
                    else:
                        if C < 10:
                            if A > 80:
                                return 1 if E < 50 else 4
                            else:
                                return 4
                        else:
                            return 3 if E < 50 else 1
                else:
                    if E > 70:
                        if B > 70:
                            return 4
                        elif A > 80:
                            return 1 if D < 20 else 4
                        else:
                            return 2
                    else:
                        return 3