import os
import logging

import toml

CONF = {}

def read_config_file():
    """Find and read config file (.2-n_solitaire.toml) if exists.

    Config file will be looked for in these directories in this order:
    - current working directory
    - home directory
    - directory specified by twoN_SOLITAIRE_CONF_DIR environment
      variable
    Return the config file contents if found, empty directory otherwise.
    """
    env_var = 'twoN_SOLITAIRE_CONF_DIR'

    locations = [
        (os.curdir, 'current directory'),
        (os.path.expanduser('~'), 'home directory'),
        (os.environ.get(env_var), f'{env_var!r} environment variable'),
    ]

    logging.debug('Looking for config file.')
    for loc, loc_desc in locations:
        try:
            logging.debug('Trying %s', loc_desc)
            cf_path = os.path.join(loc, '.2-n_solitaire.toml')
            cf_content = toml.load(cf_path)
            logging.info('Reading config file %r', cf_path)
            return cf_content
        except IOError as err:
            logging.debug('Could not read %r: %s', cf_path, err.strerror)
        except TypeError as err:
            logging.debug('Not found.')
        except toml.TomlDecodeError:
            logging.warn('Config file %s has a wrong format. Ingoring it.')

    logging.info('Config file not found. Default values will be used.')
    return {}

def init_config():
    """Initialize config with data from a config file if available.

    Otherwise default values will be used.
    """
    conf_file = read_config_file()

    global CONF
    CONF['max_card_value'] = conf_file.get('max_card_value', 2048)
