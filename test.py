
# Bioinformatics: 
#Recursively find all FASTQ files in a directory and report  each file name and the percent of sequences in that file that are greater than 30 nucleotides long. 
def read_dnafile_v2(filename):
    dna = ''
    for line in open(filename, 'r'):
        dna += line.strip()
    return dna

dna = read_dnafile_v2(dna_file)
dna_freq = get_base_frequencies(dna)
    for dna in dna_freq:
        if dna_freq > .30:
    print "Base frequencies of DNA (length %d):\n%s" % \
      (len(dna), format_frequencies(dna_freq))


#Given a FASTA file with DNA sequences, find 10 most frequent sequences and return the sequence and their counts in the file. 

dna = 'ACCAGAGT'
frequencies = find_frequencies(dna)

def format_frequencies(frequencies):
    return ', '.join(['%s: %.2f' % (base, frequencies[base])
                      for base in frequencies])
                      if frequencies >10:
print "frequencies of sequence '%s':\n%s" % \
      (dna, format_frequencies(frequencies))


#Given a chromosome and coordinates, write a program for looking up its annotation. Keep in mind you'll be doing this annotation millions of times.

# beyond my knowledge base
