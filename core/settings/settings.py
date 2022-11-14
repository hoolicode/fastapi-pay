from pathlib import Path
from ..utils import get_env_var, add_prefix

BASE_DIR = Path(__file__).resolve().parent.parent

# Server
API_URL = get_env_var('API_URL')
API_TOKEN = add_prefix(get_env_var('API_TOKEN'), 'Token')
