output/helix-turn-helix_transcriptional_regulator_tree.nex: output/helix-turn-helix_transcriptional_regulator_alignment.fasta
	python src/tree_builder.py --silent True output/helix-turn-helix_transcriptional_regulator_alignment.fasta

output/helix-turn-helix_transcriptional_regulator_alignment.fasta: output/helix-turn-helix_transcriptional_regulator.fasta
	./clustalo-1.2.4-Ubuntu-x86_64 -i output/helix-turn-helix_transcriptional_regulator.fasta --outfile output/helix-turn-helix_transcriptional_regulator_alignment.fasta

output/helix-turn-helix_transcriptional_regulator.fasta: data/*.csv data/*.fasta
	python src/gene_sequence_creator.py helix-turn-helix_transcriptional_regulator

clean:
	rm output/*
