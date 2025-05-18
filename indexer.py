def build_inverted_index(files_content):
    inverted_index = {}
    for filename, text in files_content.items():
        words = text.lower().split()
        for word in words:
            if word not in inverted_index:
                inverted_index[word] = set()
            inverted_index[word].add(filename)
    return inverted_index