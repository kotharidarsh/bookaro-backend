import logging
import logging.config
import yaml
# from app.core.config import get_settings
#
# settings = get_settings()

# creating logger object from reading logger_config yaml file
with open("logger_config.yaml", 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logger = logging.getLogger(__name__)
