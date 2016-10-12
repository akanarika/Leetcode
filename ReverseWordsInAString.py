def reverse_words(s):
    print s.split()
    return " ".join((s.split())[::-1])

print reverse_words("the sky is blue")