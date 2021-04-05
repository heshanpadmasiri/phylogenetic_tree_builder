output/helix-turn-helix_transcriptional_regulator.png output/helix-turn-helix_transcriptional_regulator_tree.nex output/LysR_family_transcriptional_regulator.png output/LysR_family_transcriptional_regulator_tree.nex output/helix-turn-helix_domain-containing_protein.png output/helix-turn-helix_domain-containing_protein_tree.nex output/efflux_transporter_outer_membrane_subunit.png output/efflux_transporter_outer_membrane_subunit_tree.nex : output/helix-turn-helix_transcriptional_regulator_alignment.fasta output/LysR_family_transcriptional_regulator_alignment.fasta output/helix-turn-helix_domain-containing_protein_alignment.fasta output/efflux_transporter_outer_membrane_subunit_alignment.fasta
	python src/tree_builder.py output/helix-turn-helix_transcriptional_regulator_alignment.fasta
	python src/tree_builder.py output/LysR_family_transcriptional_regulator_alignment.fasta
	python src/tree_builder.py output/helix-turn-helix_domain-containing_protein_alignment.fasta
	python src/tree_builder.py output/efflux_transporter_outer_membrane_subunit_alignment.fasta

output/helix-turn-helix_transcriptional_regulator_alignment.fasta: output/helix-turn-helix_transcriptional_regulator.fasta
	./clustalo-1.2.4-Ubuntu-x86_64 -i $< --outfile $@

output/LysR_family_transcriptional_regulator_alignment.fasta: output/LysR_family_transcriptional_regulator.fasta
	./clustalo-1.2.4-Ubuntu-x86_64 -i $< --outfile $@

output/helix-turn-helix_domain-containing_protein_alignment.fasta: output/helix-turn-helix_domain-containing_protein.fasta
	./clustalo-1.2.4-Ubuntu-x86_64 -i $< --outfile $@

output/efflux_transporter_outer_membrane_subunit_alignment.fasta: output/efflux_transporter_outer_membrane_subunit.fasta
	./clustalo-1.2.4-Ubuntu-x86_64 -i $< --outfile $@

output/helix-turn-helix_transcriptional_regulator.fasta: data/*.csv data/*.fasta
	python src/gene_sequence_creator.py helix-turn-helix_transcriptional_regulator

output/LysR_family_transcriptional_regulator.fasta: data/*.csv data/*.fasta
	python src/gene_sequence_creator.py LysR_family_transcriptional_regulator

output/helix-turn-helix_domain-containing_protein.fasta: data/*.csv data/*.fasta
	python src/gene_sequence_creator.py helix-turn-helix_domain-containing_protein

output/efflux_transporter_outer_membrane_subunit.fasta: data/*.csv data/*.fasta
	python src/gene_sequence_creator.py efflux_transporter_outer_membrane_subunit

clean:
	rm -f output/*
