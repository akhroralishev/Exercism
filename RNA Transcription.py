def to_rna(dna_sequence):
    transcription_map = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    try:
        return ''.join(transcription_map[nucleotide] for nucleotide in dna_sequence)
    except KeyError:
        raise ValueError("Invalid DNA nucleotide found")
