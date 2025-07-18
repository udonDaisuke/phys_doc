# pdf->md converter 
## 特徴
- pdfドキュメントのコンテンツ抽出（OCR未対応）
- configyamlによる、ヘッダーのレベル条件の指定
- チャプターごとにPDFを分割出力(H1ヘッダーが基準)が可能
- PDFファイルごとにプロジェクトフォルダを生成し、管理
- マークダウンの下処理（改行や空白記号などの修正。画像リンクの相対パス化）
- Gemini CLI等のCLIツールを使用した機能拡張を前提としている。

## Gemini CLIで処理すること@GEMINI.mdにて定義
- Pythonスクリプトの代理実行してくれる。ファイル一覧から対象ファイルを選択するだけ
- mdファイルの後処理
  - md後のmd中の数式の補完
  - 任意の言語への翻訳
- projectsフォルダ内を調査し、タスクの進捗を表示する。

# How to run
1. locate pdf file on root directory
1. run python module
```bash
# usual python environment
> python -m venv .venv 
> pip install requirements.txt

> . .venv/Scripts/activate # activaate venv

(.venv)
> python -m src.pdf2md <filename.pdf>

# uv environment
uv run -m src.pdf2md <filename.pdf>
```
---


# 作業メモ
やったこと
```bash
# 環境構築 uvを使っている　Pythonは３．１３
uv init
uv add pymupdf pymupdf4llm
uv add tqdm,pyyaml
uv pip freeze > requirements.txt
```
