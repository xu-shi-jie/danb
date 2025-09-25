"""Downloader module for bioinformatics data files."""

import argparse
import sys

import requests


def is_uniprot_id(protein_id: str) -> bool:
    """Check if the given ID is a UniProt ID.

    Args:
        protein_id: The protein identifier to check.

    Returns:
        True if the ID appears to be a UniProt ID, False otherwise.
    """
    return len(protein_id) >= 6 and protein_id[0].isalpha()


def make_url(file_format: str, protein_id: str) -> str:
    """Generate download URL based on format and protein ID.

    Args:
        file_format: The file format ('fasta', 'pdb', or 'cif').
        protein_id: The protein identifier (UniProt ID or PDB ID).

    Returns:
        The download URL for the specified protein and format.
    """
    lid = protein_id.lower()

    if file_format == "fasta":
        if is_uniprot_id(protein_id):
            return f"https://www.uniprot.org/uniprot/{protein_id}.fasta"
        else:
            return f"https://www.rcsb.org/fasta/entry/{lid}"
    elif file_format in ["pdb", "cif"]:
        if is_uniprot_id(protein_id):
            return f"https://alphafold.ebi.ac.uk/files/AF-{protein_id}-F1-model_v4.{file_format}"
        else:
            return f"https://files.rcsb.org/download/{lid}.{file_format}"

    return ""


def download_file(url: str, output_path: str) -> bool:
    """Download a file from URL to the specified path.

    Args:
        url: The URL to download from.
        output_path: The local path to save the file.

    Returns:
        True if download was successful, False otherwise.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Downloaded: {output_path}")
        return True

    except requests.RequestException as e:
        print(f"Download failed: {e}", file=sys.stderr)
        return False
    except IOError as e:
        print(f"Failed to write file {output_path}: {e}", file=sys.stderr)
        return False


def main() -> int:
    """Main entry point for the danb command-line tool."""
    parser = argparse.ArgumentParser(
        description="Download bioinformatics data files (PDB, CIF, FASTA)",
        prog="danb"
    )
    parser.add_argument(
        "format",
        choices=["pdb", "cif", "fasta"],
        help="File format to download"
    )
    parser.add_argument(
        "id",
        help="Protein identifier (UniProt ID or PDB ID)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path"
    )

    args = parser.parse_args()

    # Determine output path
    if args.output:
        output_path = args.output
    else:
        output_path = f"{args.id}.{args.format}"

    # Generate URL
    url = make_url(args.format, args.id)
    if not url:
        print("Error: Could not generate URL", file=sys.stderr)
        return 1

    # Download file
    if download_file(url, output_path):
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())