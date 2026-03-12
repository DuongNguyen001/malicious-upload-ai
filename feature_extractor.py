import os

from features.entropy import calculate_entropy
from features.pattern import detect_patterns
from features.magic import get_file_type


def extract_features(path):

    with open(path, "rb") as f:
        data = f.read()

    file_size = os.path.getsize(path)

    extension = path.split(".")[-1]

    entropy = calculate_entropy(data)

    pattern_score = detect_patterns(data)

    file_type = get_file_type(path)

    magic_mismatch = 0

    if extension not in file_type:
        magic_mismatch = 1

    features = [
        file_size,
        entropy,
        pattern_score,
        magic_mismatch,
        len(extension)
    ]

    details = {
        "file_size": file_size,
        "entropy": entropy,
        "pattern_score": pattern_score,
        "magic_mismatch": magic_mismatch
    }

    return features, details
