from dataclasses import dataclass #SIMPLIFIES THE CREATION OF CLASSES THAT STORES DATA
from pathlib import Path

#THIS DECORATOR AUTOMATICALLY GENERATES SPECIAL METHODS FOR THE CLASS
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

#UPDATING ENTITY
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int