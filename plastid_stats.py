import glob
plastidseqlist = []
for seq_record in SeqIO.parse("plastid_scaffolds.fasta", "fasta"):
    plastidseqlist.append(seq_record.id)
print(plastidseqlist)

filelist = glob.glob("bins/*.fa")
binfasta = filelist
out = open("plastid_stats.txt", "w")
out.write("ID\ttotal_ids\tplastid_ids\tplastid_percentage\n")
for file in binfasta:
    binid = file.replace(".fa", "")
    binseq = list(SeqIO.parse( file, "fasta"))

    
    total_ids = 0
    plastid_ids = 0

    for seq_record in binseq:
            total_ids += 1
            if seq_record.id in plastidseqlist:
                plastid_ids += 1
    out.write(binid + "\t" + str(total_ids) + "\t" + str(plastid_ids)  + "\t" + str(round((plastid_ids/total_ids)*100, 2)) +"%" + "\n")
    out.flush()
out.close()  