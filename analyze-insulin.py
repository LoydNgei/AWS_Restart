# open the file in reading mode
with open("preproinsulin-seq.txt", "r") as file:
    lines = file.readlines()
cleaned_sequence = ""

for line in lines:
    if 'ORIGIN' in line or '//' in line:
        continue
    cleaned_sequence += line[10:].strip()
print(cleaned_sequence)

with open('preproinsulin-seq-clean.txt', 'w') as file:
    file.write(cleaned_sequence)
    

preproinsulin_sequence = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"


lsinsulin_seq = preproinsulin_sequence[:24]
binsulin_seq = preproinsulin_sequence[24:54]
cinsulin_seq = preproinsulin_sequence[54:89]
ainsulin_seq = preproinsulin_sequence[89:]

with open('lsinsulin-seq-clean.txt', 'w') as file:
    file.write(lsinsulin_seq)
    
with open('binsulin-seq-clean.txt', 'w') as file:
    file.write(binsulin_seq)
    
with open('cinsulin-seq-clean.txt', 'w') as file:
    file.write(cinsulin_seq)

with open('ainsulin-seq-clean.txt', 'w') as file:
    file.write(ainsulin_seq)




