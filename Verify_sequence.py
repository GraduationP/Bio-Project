def verify(sequence):
    '''This code verifies if a sequence is a DNA or RNA'''
    # set the input sequence
    seq = set(sequence)

    # confirm if its elements is equal to the
    # set of valid DNA bases
    # Use a union method to ensure the sequence is
    # verified if does not contain all the bases
    if seq == {"A", "T", "C", "G"}.union(seq):
        return "DNA"
    elif seq == {"A", "U", "C", "G"}.union(seq):
        return "RNA"
    else:
        return "Invalid sequence"

