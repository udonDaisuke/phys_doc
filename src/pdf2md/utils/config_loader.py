
from pathlib import Path

import yaml

class ConfigLoader:
    """指定した設定ファイルを読み込み、設定値を取得するクラス"""
    def __init__(self, config_path):
        # ファイルの有無を判定
        if not Path(config_path).exists():
            raise FileNotFoundError(f"{config_path} not found.")
        # 設定ファイルの読み込み
        with open(config_path, "r", encoding="utf-8") as f:
            try:
                self._config = yaml.safe_load(f)
            except yaml.YAMLError as e:
                raise ValueError(f"YAML parsing error [{config_path}]\n >> {e}")

    def __getitem__(self, item):
        return self._config.get(item)