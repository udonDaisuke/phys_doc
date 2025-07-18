import re
from pathlib import Path

from tqdm import tqdm


class MarkdownContentsPreprocessor:
    def __init__(self, contents=None):
        self.contents = contents
        self.contents_separated = None

    def _clean_markdown_content(self, content):
        """Markdown contentをクリーンアップするメソッド"""
        # PDF変換時などに含まれがちな制御文字（表示に支障が出るもの）を除去する
        content = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', content)

        # 改行コードをUnixスタイル（\n）に統一する
        # WindowsのCRLF（\r\n）やMacのCR（\r）-> \n
        content = content.replace('\r\n', '\n').replace('\r', '\n')

        # 連続する空行を1つの空行に置き換えて、余計なスペースを減らす
        content = re.sub(r'\n\n+', '\n\n', content)

        # 絶対パス画像リンクを相対パスに書き換える（altテキストは空でOK）
        content = re.sub(
            r'!\[\]\((?:[A-Z]:)?[^)\\]+images[\\/](.+?)\)',
            r'![](../images/\1)',
            content
            )

        return content

    def separate_chapters(self, chapter_hdr_level=1):
        """Markdown内容を指定したヘッダーレベルごとにチャプターとして分割するメソッド"""
        print("Checking contents to separate chapters ...")
        contents_separated = {} # contentsが分割された際に情報を格納する辞書
        all_lines = self.contents.splitlines()
        current_chapter_title = "Default_title"
        current_chapter_lines = [] # 現在のチャプターの行を保持するリスト

        for line in all_lines:
            # ヘッダー行を検出: 前のチャプターの内容の保存と、新チャプターの情報登録
            if line.startswith("#" * chapter_hdr_level + " "):
                #現在のチャプターが登録済みの場合（前のチャプターが終わったことを意味する）
                if current_chapter_lines:
                    # 現在のチャプター（前のチャプター）の内容を辞書に追加
                    contents_separated[current_chapter_title] = "\n".join(current_chapter_lines)

                # 現在のチャプターを更新
                current_chapter_title = line.strip()
                current_chapter_lines = [line]
            # 非ヘッダー行
            else:
                current_chapter_lines.append(line)

        # 最後のチャプターの内容を保存        
        if current_chapter_title and current_chapter_lines:
            contents_separated[current_chapter_title] = "\n".join(current_chapter_lines)

        self.contents_separated = contents_separated
        print(f"Separated into {len(self.contents_separated)} chapters.")
        return self.contents_separated

    def write(self, output_dir, separate_chapters=False, show_progress=True):
        """Markdown内容を指定されたディレクトリに書き込むメソッド"""

        OUTPUT_DIR = Path(output_dir)
        bar_format="{bar} [{percentage:3.0f}%] "

        # チャプターごとにファイルを分割する場合
        if separate_chapters:
            if self.contents_separated is None:
                raise TypeError("contents_separated is None. Please call separate_chapters() first.")
            
            print(f"Writing {len(self.contents_separated)} separated files...")
            for key, value in tqdm(self.contents_separated.items(), bar_format=bar_format, ncols=50):
                print(f"Processing {key} ...")
                # ファイル名のサニタイズ
                # 空白や特殊文字を除去
                sanitized_key = key.strip()
                # Windowsのファイル名に使えない文字を除去
                sanitized_key = re.sub(r'[<>:"/\\|?*#•]', '', sanitized_key)
                # 連続する空白を1つに置き換え、前後の空白をトリム
                sanitized_key = re.sub(r'\s+', ' ', sanitized_key).strip()
                # 文字数を制限
                if len(sanitized_key) > 100:
                    sanitized_key = sanitized_key[:100]
                if not sanitized_key:
                    sanitized_key = "untitled"
                file_path = OUTPUT_DIR / f"{sanitized_key}.md"

                # 特定の文字列記号の除去
                cleaned_value = self._clean_markdown_content(value)

                # ファイル出力
                try:
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(cleaned_value) 
                except OSError as e:
                    print(f"Could not write file {file_path}: {e}")

            if not OSError :
                print(f"Finished writing files.")


        # 全体を1つのファイルに書き込む場合
        else:
            all_md_path = OUTPUT_DIR / "All.md"
            print(f"Processing {all_md_path}...")
            with open(all_md_path, 'w', encoding='utf-8') as file:
                if isinstance(self.contents, str):
                    cleaned_content = self._clean_markdown_content(self.contents)
                    file.write(cleaned_content)
                elif isinstance(self.contents, list):
                    for i in tqdm(range(len(self.contents)), bar_format=bar_format,ncols=50):
                        cleaned_content = self._clean_markdown_content(self.contents[i])
                        file.write(cleaned_content)
                        
