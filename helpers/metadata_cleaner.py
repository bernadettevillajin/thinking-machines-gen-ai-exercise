from langchain.schema import Document
from langchain_community.vectorstores.utils import filter_complex_metadata

def clean(metadata):
  return filter_complex_metadata(metadata) if isinstance(metadata, Document) else {}