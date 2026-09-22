from pathlib import Path
from typing import List, Any
from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import UnstructuredExcelLoader
from langchain_community.document_loaders import JSONLoader

def load_all_documents(data_dir: str) -> List[Any]:
    """
    Load all supported files from the data directory and convert to LangChain document structure
    Supported: PDF, TXT, CSV, EXCEL, Word, JSON
    """
    # Use project root data folder
    data_path = Path(data_dir).resolve()
    print(f"[DEBUG] Data path: {data_path}")
    documents = []

    #PDF files
    pdf_files = list(data_path.glob('**/*.pdf'))
    print(f"[DEBUG] Found {len(pdf_files)} PDF files: {[str(f.name) for f in pdf_files]}")
    for pdf_file in pdf_files:
        print(f"[DEBUG] Loading PDF: {pdf_file.name}")
        try:
            loader = PyPDFLoader(str(pdf_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} PDF docs from {pdf_file.name}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load PDF {pdf_file.name}: {e}")

    #Text files
    text_files = list(data_path.glob('**/*.txt'))
    print(f"[DEBUG] Found {len(text_files)} Text files: {[str(f.name) for f in text_files]}")
    for text_file in text_files:
        print(f"[DEBUG] Loading file: {text_file.name}")
        try:
            loader = TextLoader(str(text_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} Text docs from {text_file.name}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load Text file {text_file.name}: {e}")

    #word file
    word_files = list(data_path.glob('**/*.docx'))
    print(f"[DEBUG] Found {len(word_files)} Word files: {[str(f.name) for f in word_files]}")
    for word_file in word_files:
        print(f"[DEBUG] Loading word file: {word_file.name}")
        try:
            loader = Docx2txtLoader(file_path=str(word_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} docs from {word_file.name}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load file {word_file.name}: {e}")

    return documents