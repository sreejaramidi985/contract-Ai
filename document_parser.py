def parse_document(file_path: str) -> str:
    """
    Reads a contract document and returns plain text.
    Currently supports .txt files.
    """

    if not file_path.lower().endswith(".txt"):
        raise ValueError("Only .txt files are supported right now")

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text
