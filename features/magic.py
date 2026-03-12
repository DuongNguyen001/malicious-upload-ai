import magic

def get_file_type(path):

    try:
        file_type = magic.from_file(path, mime=True)
        return file_type

    except:
        return "unknown"
