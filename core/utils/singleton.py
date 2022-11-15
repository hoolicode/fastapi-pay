from typing import Tuple, Dict


class Singleton(type):
  _instances = {}

  def __call__(cls, *args: Tuple, **kwargs: Dict) -> object:

    if cls not in cls._instances:
      cls._instances[cls] = super().__call__(*args, **kwargs)

    return cls._instances[cls]
