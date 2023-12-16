def count_alignments_and_shifts(text, subsequence):
    alignments = 0
    shifts = 1

    # Iterate through the text
    for i in range(len(text) - len(subsequence) + 1):
        match = True

        # Check if the subsequence matches the current substring of the text
        for j in range(len(subsequence)):
            if text[i + j] != subsequence[j]:
                match = False
                break

        # If a match is found, increment alignments
        if match:
            alignments += 1

        # If the match starts at a position greater than 0, increment shifts
        if i > 0:
            shifts += 1

    return f"Number of alignments: {alignments}, Number of shifts needed: {shifts}"
