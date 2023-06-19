from table import table

def read_seq(inputfile):
    """Reads and returns the input sequence with special characters removed."""
    with open(inputfile, "r") as f:
        seq = f.read()
        seq = seq.replace("\n", "")
        seq = seq.replace("\r", "")
        return seq

def translate(seq):
    """Translate a string containing a nucleotide sequence into a string containing the corresponding sequence of amino acids. Nucleotides are translated in triplets using the table dictionary; each amino acid is encoded with a string of length 1."""
    read_seq(dna_file)

    original_seq = seq  # Store the original case
    seq = seq.upper()  # Convert to uppercase
    
    if seq not in table or len(seq) != 3:
        print("\033[91mInvalid codon: \033[0m", original_seq)

        seq = input("\n\033[93mDNA Sequence: \033[0m")
        return translate(seq)
    
    protein = ''
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        protein += table[codon]
    
    return protein


def main(dna_file, protein_file):    
    if not previous_output:
        print("\nEnter a DNA sequence for translation.\nType 'help' for a list of DNA sequences.\n___________\n") 
    user_input = input("\033[93mDNA Sequence: \033[0m")
            
    if user_input.lower() == "help":
        print("List of DNA sequences:")
        dna_sequences = ", ".join(table.keys())
        print(dna_sequences)
    
    else:
        protein_seq = translate(user_input)
        print(f"\nTranslated protein sequence: \033[92m{protein_seq}\033[0m")


# Specify the input file paths
dna_file = "dna.txt"
protein_file = "protein.txt"

previous_output = False

# Main loop
while True:
    if previous_output:
        print("--------------------------------------------------")
    main(dna_file, protein_file)
    previous_output = True
