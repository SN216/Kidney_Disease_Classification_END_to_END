from dataclasses import dataclass #SIMPLIFIES THE CREATION OF CLASSES THAT STORES DATA
from pathlib import Path

#THIS DECORATOR AUTOMATICALLY GENERATES SPECIAL METHODS FOR THE CLASS
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path