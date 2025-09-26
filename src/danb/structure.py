import gzip
from biotite.structure.io import pdbx as cif
from biotite.structure.io import pdb as pdb
from biotite.structure import AtomArray

def read_protein_file(file: str, model_idx:int=0) -> AtomArray:
    """Reads a protein structure file and returns an AtomArray.

    This function supports PDB and CIF formats, both gzipped and uncompressed.

    Args:
        file: The path to the protein structure file.
        model_idx: The index of the model to read from the file.

    Returns:
        An AtomArray representing the protein structure.

    Raises:
        ValueError: If the file format is not supported.
    """
    data_type = None
    if file.endswith('.cif'):
        file = open(file, 'r')
        data_type = 'cif'
    elif file.endswith('.cif.gz'):
        file = gzip.open(file, 'rt')
        data_type = 'cif'
    elif file.endswith('.pdb') or file.endswith('.ent'):
        file = open(file, 'r')
        data_type = 'pdb'
    elif file.endswith('.pdb.gz'):
        file = gzip.open(file, 'rt')
        data_type = 'pdb'
    else:
        raise ValueError("Unsupported file format. Supported formats are .cif, .cif.gz, .pdb, .pdb.gz, .ent")
        
    if data_type == 'cif':
        cif_file = cif.PDBxFile.read(file)
        atoms = cif.get_structure(cif_file)[model_idx]
    elif data_type == 'pdb':
        pdb_file = pdb.PDBFile.read(file)
        atoms = pdb.get_structure(pdb_file)[model_idx]
    else:
        raise ValueError("Unsupported file format. Supported formats are .cif, .cif.gz, .pdb, .pdb.gz, .ent")
    
    file.close()
    return atoms


if __name__ == "__main__":
    # Example usage
    protein_structure = read_protein_file("tests/data/12ca.cif.gz")
    print(protein_structure)