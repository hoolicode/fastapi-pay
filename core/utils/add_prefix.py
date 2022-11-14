

def add_prefix(string: str, prefix: str) -> str:

  if not string.startswith(prefix):
    string = f'{prefix} {string}'

  return string
