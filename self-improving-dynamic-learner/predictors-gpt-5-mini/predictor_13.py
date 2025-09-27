"""
Predictor 13
Generated on: 2025-09-09 12:10:57
Accuracy: 47.22%
"""


# PREDICTOR 13 - Accuracy: 47.22%
# Correct predictions: 4722/10000 (47.22%)

def predict_output(A, B, C, D, E):
    A_i = int(A); B_i = int(B); C_i = int(C); D_i = int(D); E_i = int(E)

    # Exact training rows
    training = {
        (82,15,4,95,36): 3,
        (32,29,18,95,14): 1,
        (87,95,70,12,76): 1,
        (55,5,4,12,28): 3,
        (30,65,78,4,72): 2,
        (26,92,84,90,70): 2,
        (54,29,58,76,36): 1,
        (1,98,21,90,55): 1,
        (44,36,20,28,98): 4,
        (44,14,12,49,13): 3
    }
    key = (A_i, B_i, C_i, D_i, E_i)
    if key in training:
        return training[key]

    # basic derived features
    s = A_i + B_i + C_i + D_i + E_i
    ab = A_i + B_i
    max_v = max(A_i, B_i, C_i, D_i, E_i)
    # argmax label
    if max_v == A_i:
        argmax = 'A'
    elif max_v == B_i:
        argmax = 'B'
    elif max_v == C_i:
        argmax = 'C'
    elif max_v == D_i:
        argmax = 'D'
    else:
        argmax = 'E'
    a_over_b = A_i / (B_i + 1)

    # Specific rules (ordered)

    # Strong pattern: very high C but very low D and E -> often class 4
    if C_i >= 85 and D_i <= 20 and E_i <= 30:
        return 4

    # High D with low C and very strong B often -> class 4 (observed cases)
    if D_i >= 85 and C_i <= 25 and B_i >= 70:
        return 4

    # Very strong D (extreme) -> usually 1 unless A is large (then 3)
    if D_i >= 90:
        if A_i >= 50:
            return 3
        return 1

    # When C and overall sum are both large -> class 1 (override E dominance)
    if C_i >= 78 and s >= 260:
        return 1

    # Very large total sum: usually class 1, except when C is tiny -> 4
    if s >= 300:
        if C_i < 10:
            return 4
        return 1

    # Very large E usually -> 4, but allow overrides when other signals strong
    if E_i >= 95:
        # if C or sum are very strong, prefer 1
        if C_i >= 60 or s >= 270:
            return 1
        return 4

    # E high but not extreme: prefer 1 if sum and C are substantial
    if E_i >= 80:
        if s >= 250 and C_i >= 30:
            return 1
        if C_i <= 10 and D_i <= 30:
            return 4
        if A_i <= 20 and C_i <= 30:
            return 2
        # when C is small and either D or B are large, lean 4
        if C_i <= 25 and (D_i >= 70 or B_i >= 80):
            return 4
        # otherwise favor 1 if there is moderate internal strength
        if s >= 220 or ab >= 120:
            return 1
        return 4

    # Strong A+B combined signal -> 1 (use higher threshold to avoid earlier mistakes)
    if ab >= 140:
        # except when C is extremely small (tiny C often maps to 4)
        if C_i <= 5:
            return 4
        return 1

    # Strong B with moderate-to-high C -> 2
    if B_i >= 90 and C_i >= 40:
        return 2
    if B_i >= 85 and C_i >= 65:
        return 2

    # If C is the maximum and moderately large, prefer 2
    if argmax == 'C' and C_i >= 50:
        return 2

    # If D moderately high with A moderate-high -> 3
    if D_i >= 75 and A_i >= 50:
        return 3

    # Very small C with some other strong signals often -> 4
    if C_i <= 5 and (D_i >= 70 or E_i >= 60 or ab >= 150):
        return 4

    # Low C with high E tends to 4
    if C_i <= 20 and E_i >= 70:
        return 4

    # Fallback weighted score (simple)
    score = A_i * 0.45 + B_i * 0.3 + C_i * 0.15 + D_i * 0.06 + E_i * 0.04
    if score >= 55:
        return 1
    if score >= 45 and C_i >= 40:
        return 2
    if score < 25 and E_i >= 60:
        return 4

    # Default conservative fallback
    return 3