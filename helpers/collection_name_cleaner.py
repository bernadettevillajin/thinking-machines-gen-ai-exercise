import re
from datetime import datetime

def clean(name):
  name = f"{name.split('.')[0].replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
  allowed_chars = re.sub(r'[^a-zA-Z0-9-_]', '', name)
  return allowed_chars[:63]