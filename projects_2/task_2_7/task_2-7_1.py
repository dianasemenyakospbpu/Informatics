files = ["seq1", "seq2", "seq3", "seq4"]

for name in files:

   new_name = name + ".fasta"
   data_name = new_name + "\tдата взятия образца: 23.02.2026"
   
   print(f"{data_name}")