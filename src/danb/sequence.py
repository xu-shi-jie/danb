from pathlib import Path
import requests
from Bio.SeqIO import parse
import subprocess


def read_or_download(pdbid, cache_dir):
    """Reads a FASTA file from cache or downloads it from RCSB PDB.

    Args:
        pdbid: The PDB ID of the protein.
        cache_dir: The directory to cache the FASTA file.

    Returns:
        A list of tuples, where each tuple contains the ID and sequence of a
        record in the FASTA file.
    """
    Path(cache_dir).mkdir(exist_ok=True, parents=True)
    fasta_file = f'{cache_dir}/{pdbid}.fasta'
    if not Path(fasta_file).exists():
        with open(fasta_file, 'w') as f:
            f.write(requests.get(
                    f'https://www.rcsb.org/fasta/entry/{pdbid}').text)
    return [(r.id, str(r.seq)) for r in parse(fasta_file, 'fasta')]


def cluster(fasta_file, cache_dir, seq_id=0.3):
    """Clusters sequences in a FASTA file using MMseqs2.

    Args:
        fasta_file: The path to the FASTA file to cluster.
        cache_dir: The directory to store temporary files.
        seq_id: The minimum sequence identity for clustering.
    """
    for cmd in [
        f"mmseqs easy-cluster {fasta_file} clusterRes {cache_dir} --min-seq-id {seq_id} -c 0.8 --cov-mode 1",
    ]:
        subprocess.run(
            cmd, shell=True, check=True,
            stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL
        )


def search(fasta1, fasta2, cache_dir, seq_id=0.3):
    """Searches for similar sequences between two FASTA files using MMseqs2.

    Args:
        fasta1: The path to the query FASTA file.
        fasta2: The path to the target FASTA file.
        cache_dir: The directory to store temporary files.
        seq_id: The minimum sequence identity for searching.
    """
    cmd = f'mmseqs easy-search {fasta1} {fasta2} alnRes.m8 {cache_dir} --min-seq-id {seq_id} -c 0.8 --cov-mode 1'
    subprocess.run(
        cmd, check=True, shell=True,
        stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL
    )