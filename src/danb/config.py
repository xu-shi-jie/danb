import yaml

class Config:
    """A class to manage configuration from YAML files.

    This class allows for reading, updating, and saving configuration settings
    from and to YAML files. Configuration values are stored as attributes of
    the class instance.
    """

    def __init__(self, yaml_file: str):
        """Initializes the Config object from a YAML file.

        Args:
            yaml_file: The path to the YAML file to load configuration from.
        """
        with open(yaml_file, "r") as f:
            config = yaml.safe_load(f)

        for k, v in config.items():
            setattr(self, k, v)

    def update(self, new_yaml_file: str):
        """Updates the configuration from a new YAML file.

        Existing configuration values are overwritten by values from the new
        file. New configuration values are added.

        Args:
            new_yaml_file: The path to the YAML file to update the
                configuration from.
        """
        with open(new_yaml_file, "r") as f:
            config = yaml.safe_load(f)

        for k, v in config.items():
            setattr(self, k, v)

    def save(self, yaml_file: str):
        """Saves the current configuration to a YAML file.

        Args:
            yaml_file: The path to the YAML file to save the configuration to.
        """
        with open(yaml_file, "w") as f:
            yaml.dump(self.__dict__, f)