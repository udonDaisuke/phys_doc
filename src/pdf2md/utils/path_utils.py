from pathlib import Path

def ensure_dir(path: Path):
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)


# class DirInfo:
#     """ディレクトリの情報を取得するクラス"""

#     def __init__(self, path: Path):
#         self.path = path
#         self.name = path.name
#         self.parent = path.parent
#         self.is_dir = path.is_dir()
#         self.is_file = path.is_file()
#         self.exists = path.exists()

#     def files(self,type=None):
#         """指定されたタイプのファイルを取得するメソッド"""
#         if self.is_dir:
#             if type:
#                 return list(self.path.glob(f"*.{type}"))
#             else:
#                 return list(self.path.glob("*"))
#         return []
    
#     def folders(self):
#         """ディレクトリ内のサブディレクトリを取得するメソッド"""
#         if self.is_dir:
#             return [DirectoryInfo(p) for p in self.path.iterdir() if p.is_dir()]
#         return []
    
