import os
import math

def entropy(data):
    if not data:
        return 0

    occurences = [0] * 256

    for x in data:
        occurences[x] += 1

    entropy = 0

    for count in occurences:
        if count == 0:
            continue
        p = count / len(data)
        entropy -= p * math.log2(p)

    return entropy

def get_magic(data):

    if data.startswith(b'\xFF\xD8'):
        return "jpg"

    elif data.startswith(b'\x89PNG'):
        return "png"

    elif data.startswith(b'%PDF'):
        return "pdf"

    elif b'<?php' in data:
        return "php"

    else:
        return "unknown"


def extract_features(file_path):

    with open(file_path, "rb") as f:
        data = f.read()

    text = data.decode(errors="ignore")

    file_size = len(data)

    file_entropy = entropy(data)

    extension = os.path.splitext(file_path)[1].lower()

    magic = get_magic(data)

    magic_mismatch = 0

    if magic != "unknown" and magic != extension:
        magic_mismatch = 1

    multiple_extensions = file_path.count(".")

    suspicious_keywords = [
        "eval",
        "exec",
        "system",
        "shell_exec",
        "passthru",
        "base64_decode",
        "cmd",
        "wget",
        "curl"
    ]

    pattern_score = 0
    for keyword in suspicious_keywords:
        if keyword in text:
            pattern_score += 1

    php_tag = 1 if "<?php" in text else 0

    base64_count = text.count("base64")

    features = [
        file_size,
        file_entropy,
        pattern_score,
        php_tag,
        base64_count,
        multiple_extensions,
	magic_mismatch
    ]

    details = {
        "file_size": file_size,
        "entropy": round(file_entropy,2),
        "pattern_score": pattern_score,
        "php_tag": php_tag,
        "base64_count": base64_count,
        "multiple_extensions": multiple_extensions,
	"magic_mismatch": magic_mismatch
    }

    return features, details
