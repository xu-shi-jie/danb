# Table of Contents

* [danb](#danb)
* [danb.config](#danb.config)
  * [Config](#danb.config.Config)
    * [\_\_init\_\_](#danb.config.Config.__init__)
    * [update](#danb.config.Config.update)
    * [save](#danb.config.Config.save)
* [danb.cli](#danb.cli)
  * [cli](#danb.cli.cli)
* [danb.structure](#danb.structure)
  * [read\_protein\_file](#danb.structure.read_protein_file)
* [danb.downloader](#danb.downloader)
  * [is\_uniprot\_id](#danb.downloader.is_uniprot_id)
  * [make\_url](#danb.downloader.make_url)
  * [download\_file](#danb.downloader.download_file)
  * [main](#danb.downloader.main)
* [danb.plm](#danb.plm)
  * [EsmModelInfo](#danb.plm.EsmModelInfo)
  * [EsmEncoder](#danb.plm.EsmEncoder)
    * [\_\_init\_\_](#danb.plm.EsmEncoder.__init__)
    * [forward](#danb.plm.EsmEncoder.forward)
  * [T5Encoder](#danb.plm.T5Encoder)
    * [\_\_init\_\_](#danb.plm.T5Encoder.__init__)
    * [forward](#danb.plm.T5Encoder.forward)
  * [get\_model](#danb.plm.get_model)
* [danb.sequence](#danb.sequence)
  * [read\_or\_download](#danb.sequence.read_or_download)
  * [cluster](#danb.sequence.cluster)
  * [search](#danb.sequence.search)

<a id="danb"></a>

# danb

danb: Python utilities and tools for bioinformatics data processing.

<a id="danb.config"></a>

# danb.config

<a id="danb.config.Config"></a>

## Config Objects

```python
class Config()
```

A class to manage configuration from YAML files.

This class allows for reading, updating, and saving configuration settings
from and to YAML files. Configuration values are stored as attributes of
the class instance.

<a id="danb.config.Config.__init__"></a>

#### \_\_init\_\_

```python
def __init__(yaml_file: str)
```

Initializes the Config object from a YAML file.

**Arguments**:

- `yaml_file` - The path to the YAML file to load configuration from.

<a id="danb.config.Config.update"></a>

#### update

```python
def update(new_yaml_file: str)
```

Updates the configuration from a new YAML file.

Existing configuration values are overwritten by values from the new
file. New configuration values are added.

**Arguments**:

- `new_yaml_file` - The path to the YAML file to update the
  configuration from.

<a id="danb.config.Config.save"></a>

#### save

```python
def save(yaml_file: str)
```

Saves the current configuration to a YAML file.

**Arguments**:

- `yaml_file` - The path to the YAML file to save the configuration to.

<a id="danb.cli"></a>

# danb.cli

Command-line interface for danb.

<a id="danb.cli.cli"></a>

#### cli

```python
def cli()
```

Entry point for the danb command-line tool.

<a id="danb.structure"></a>

# danb.structure

<a id="danb.structure.read_protein_file"></a>

#### read\_protein\_file

```python
def read_protein_file(file: str, model_idx: int = 0) -> AtomArray
```

Reads a protein structure file and returns an AtomArray.

This function supports PDB and CIF formats, both gzipped and uncompressed.

**Arguments**:

- `file` - The path to the protein structure file.
- `model_idx` - The index of the model to read from the file.
  

**Returns**:

  An AtomArray representing the protein structure.
  

**Raises**:

- `ValueError` - If the file format is not supported.

<a id="danb.downloader"></a>

# danb.downloader

Downloader module for bioinformatics data files.

<a id="danb.downloader.is_uniprot_id"></a>

#### is\_uniprot\_id

```python
def is_uniprot_id(protein_id: str) -> bool
```

Check if the given ID is a UniProt ID.

**Arguments**:

- `protein_id` - The protein identifier to check.
  

**Returns**:

  True if the ID appears to be a UniProt ID, False otherwise.

<a id="danb.downloader.make_url"></a>

#### make\_url

```python
def make_url(file_format: str, protein_id: str) -> str
```

Generate download URL based on format and protein ID.

**Arguments**:

- `file_format` - The file format ('fasta', 'pdb', or 'cif').
- `protein_id` - The protein identifier (UniProt ID or PDB ID).
  

**Returns**:

  The download URL for the specified protein and format.

<a id="danb.downloader.download_file"></a>

#### download\_file

```python
def download_file(url: str, output_path: str) -> bool
```

Download a file from URL to the specified path.

**Arguments**:

- `url` - The URL to download from.
- `output_path` - The local path to save the file.
  

**Returns**:

  True if download was successful, False otherwise.

<a id="danb.downloader.main"></a>

#### main

```python
def main() -> int
```

Main entry point for the danb command-line tool.

<a id="danb.plm"></a>

# danb.plm

<a id="danb.plm.EsmModelInfo"></a>

#### EsmModelInfo

```python
def EsmModelInfo(name: str)
```

Get model information by name.

**Arguments**:

- `name` - The name of the ESM model.
  

**Returns**:

  A dictionary containing model information, including dimension, number of
  layers, and the model name for Hugging Face.

<a id="danb.plm.EsmEncoder"></a>

## EsmEncoder Objects

```python
class EsmEncoder(nn.Module)
```

An encoder for ESM models.

This class provides an interface to ESM models for encoding protein
sequences. It handles tokenization and model inference, including for
sequences longer than the model's maximum length by using a sliding
window approach.

**Attributes**:

- `tokenizer` - The tokenizer for the ESM model.
- `model` - The ESM model.
- `max_len` - The maximum sequence length for the model.
- `overlap` - The overlap size for the sliding window.

<a id="danb.plm.EsmEncoder.__init__"></a>

#### \_\_init\_\_

```python
def __init__(model_name, dev)
```

Initializes the EsmEncoder.

**Arguments**:

- `model_name` - The name of the ESM model to use.
- `dev` - The device to run the model on.

<a id="danb.plm.EsmEncoder.forward"></a>

#### forward

```python
def forward(_seqs)
```

Encodes a batch of sequences.

**Arguments**:

- `_seqs` - A list of protein sequences to encode. Currently, only a
  batch size of 1 is supported.
  

**Returns**:

  A tensor containing the encoded representations of the sequences.

<a id="danb.plm.T5Encoder"></a>

## T5Encoder Objects

```python
class T5Encoder(nn.Module)
```

An encoder for T5 models.

This class provides an interface to T5 models for encoding protein
sequences. It handles tokenization and model inference, including for
sequences longer than the model's maximum length by using a sliding
window approach.

**Attributes**:

- `tokenizer` - The tokenizer for the T5 model.
- `model` - The T5 model.
- `max_len` - The maximum sequence length for the model.
- `overlap` - The overlap size for the sliding window.

<a id="danb.plm.T5Encoder.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name: str, dev) -> None
```

Initializes the T5Encoder.

**Arguments**:

- `name` - The name of the T5 model to use.
- `dev` - The device to run the model on.

<a id="danb.plm.T5Encoder.forward"></a>

#### forward

```python
def forward(_seqs)
```

Encodes a batch of sequences.

**Arguments**:

- `_seqs` - A list of protein sequences to encode. Currently, only a
  batch size of 1 is supported.
  

**Returns**:

  A tensor containing the encoded representations of the sequences.

<a id="danb.plm.get_model"></a>

#### get\_model

```python
def get_model(name: str, dev)
```

Get a pre-trained model by name.

**Arguments**:

- `name` - The name of the model to get.
- `dev` - The device to run the model on.
  

**Returns**:

  An instance of the specified model.
  

**Raises**:

- `ValueError` - If the model name is unknown.

<a id="danb.sequence"></a>

# danb.sequence

<a id="danb.sequence.read_or_download"></a>

#### read\_or\_download

```python
def read_or_download(pdbid, cache_dir)
```

Reads a FASTA file from cache or downloads it from RCSB PDB.

**Arguments**:

- `pdbid` - The PDB ID of the protein.
- `cache_dir` - The directory to cache the FASTA file.
  

**Returns**:

  A list of tuples, where each tuple contains the ID and sequence of a
  record in the FASTA file.

<a id="danb.sequence.cluster"></a>

#### cluster

```python
def cluster(fasta_file, cache_dir, seq_id=0.3)
```

Clusters sequences in a FASTA file using MMseqs2.

**Arguments**:

- `fasta_file` - The path to the FASTA file to cluster.
- `cache_dir` - The directory to store temporary files.
- `seq_id` - The minimum sequence identity for clustering.

<a id="danb.sequence.search"></a>

#### search

```python
def search(fasta1, fasta2, cache_dir, seq_id=0.3)
```

Searches for similar sequences between two FASTA files using MMseqs2.

**Arguments**:

- `fasta1` - The path to the query FASTA file.
- `fasta2` - The path to the target FASTA file.
- `cache_dir` - The directory to store temporary files.
- `seq_id` - The minimum sequence identity for searching.

