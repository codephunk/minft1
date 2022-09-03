import yaml
import io

from metadict import MetaDict

# Initialize configuration
with io.open("config.yml", 'r', encoding='utf8') as stream:
    cfg = MetaDict(yaml.safe_load(stream))

