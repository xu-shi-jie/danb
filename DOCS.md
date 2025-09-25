# Table of Contents

* [\_\_init\_\_](#__init__)
* [config](#config)
  * [Config](#config.Config)
    * [\_\_init\_\_](#config.Config.__init__)
    * [update](#config.Config.update)
    * [save](#config.Config.save)
* [cli](#cli)
  * [cli](#cli.cli)
* [structure](#structure)
  * [read\_protein\_file](#structure.read_protein_file)
* [downloader](#downloader)
  * [is\_uniprot\_id](#downloader.is_uniprot_id)
  * [make\_url](#downloader.make_url)
  * [download\_file](#downloader.download_file)
  * [main](#downloader.main)
* [plm](#plm)
  * [EsmModelInfo](#plm.EsmModelInfo)
  * [EsmEncoder](#plm.EsmEncoder)
    * [\_\_init\_\_](#plm.EsmEncoder.__init__)
    * [forward](#plm.EsmEncoder.forward)
  * [T5Encoder](#plm.T5Encoder)
    * [\_\_init\_\_](#plm.T5Encoder.__init__)
    * [forward](#plm.T5Encoder.forward)
  * [get\_model](#plm.get_model)
* [sequence](#sequence)
  * [read\_or\_download](#sequence.read_or_download)
  * [cluster](#sequence.cluster)
  * [search](#sequence.search)

<a id="__init__"></a>

# \_\_init\_\_

danb: Python utilities and tools for bioinformatics data processing.

<a id="config"></a>

# config

<a id="config.Config"></a>

## Config Objects

```python
class Config()
```

A class to manage configuration from YAML files.

This class allows for reading, updating, and saving configuration settings
from and to YAML files. Configuration values are stored as attributes of
the class instance.

<a id="config.Config.__init__"></a>

#### \_\_init\_\_

```python
def __init__(yaml_file: str)
```

Initializes the Config object from a YAML file.

**Arguments**:

- `yaml_file` - The path to the YAML file to load configuration from.

<a id="config.Config.update"></a>

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

<a id="config.Config.save"></a>

#### save

```python
def save(yaml_file: str)
```

Saves the current configuration to a YAML file.

**Arguments**:

- `yaml_file` - The path to the YAML file to save the configuration to.

<a id="cli"></a>

# cli

Command-line interface for danb.

<a id="cli.cli"></a>

#### cli

```python
def cli()
```

Entry point for the danb command-line tool.

<a id="structure"></a>

# structure

<a id="structure.read_protein_file"></a>

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

<a id="downloader"></a>

# downloader

Downloader module for bioinformatics data files.

<a id="downloader.is_uniprot_id"></a>

#### is\_uniprot\_id

```python
def is_uniprot_id(protein_id: str) -> bool
```

Check if the given ID is a UniProt ID.

**Arguments**:

- `protein_id` - The protein identifier to check.
  

**Returns**:

  True if the ID appears to be a UniProt ID, False otherwise.

<a id="downloader.make_url"></a>

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

<a id="downloader.download_file"></a>

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

<a id="downloader.main"></a>

#### main

```python
def main() -> int
```

Main entry point for the danb command-line tool.

<a id="plm"></a>

# plm

<a id="plm.EsmModelInfo"></a>

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

<a id="plm.EsmEncoder"></a>

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

<a id="plm.EsmEncoder.__init__"></a>

#### \_\_init\_\_

```python
def __init__(model_name, dev)
```

Initializes the EsmEncoder.

**Arguments**:

- `model_name` - The name of the ESM model to use.
- `dev` - The device to run the model on.

<a id="plm.EsmEncoder.forward"></a>

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

<a id="plm.T5Encoder"></a>

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

<a id="plm.T5Encoder.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name: str, dev) -> None
```

Initializes the T5Encoder.

**Arguments**:

- `name` - The name of the T5 model to use.
- `dev` - The device to run the model on.

<a id="plm.T5Encoder.forward"></a>

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

<a id="plm.get_model"></a>

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

<a id="sequence"></a>

# sequence

<a id="sequence.read_or_download"></a>

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

<a id="sequence.cluster"></a>

#### cluster

```python
def cluster(fasta_file, cache_dir, seq_id=0.3)
```

Clusters sequences in a FASTA file using MMseqs2.

**Arguments**:

- `fasta_file` - The path to the FASTA file to cluster.
- `cache_dir` - The directory to store temporary files.
- `seq_id` - The minimum sequence identity for clustering.

<a id="sequence.search"></a>

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

