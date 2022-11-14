from os import environ
from typing import Union


def get_env_var(variable_name: str, default: str = None) -> Union[str, None]:

  if not (variable := environ.get(variable_name)) and not default:
    raise KeyError(f'No Environment Variable: {variable_name}')

  return variable or default
