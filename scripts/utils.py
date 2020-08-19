import re

def camel_to_snake(name):
    """
    Convert strings to snake case format
    """
    # https://stackoverflow.com/a/1176023
    name = name.replace(' ', '_').replace("'", '').replace(':', '_').replace('?','')
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('_+', r'_', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()