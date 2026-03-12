def get_file_type(file_path):
    with open(file_path, "rb") as f:
        header = f.read(4)

    if header.startswith(b'\xFF\xD8'):
        return "jpg"
    elif header.startswith(b'\x89PNG'):
        return "png"
    elif header.startswith(b'%PDF'):
        return "pdf"
    else:
        return "unknown"
