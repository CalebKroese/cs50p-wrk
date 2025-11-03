def main():
    filename = input("File name: ").strip().lower()

    # dictionary mapping extensions to media types
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip",
    }

    # check each extension
    for ext, mtype in media_types.items():
        if filename.endswith(ext):
            print(mtype)
            return

    # default
    print("application/octet-stream")


main()