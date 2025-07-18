import pymupdf4llm

def extraction_from_pdf(file_path,hdr_function,image_path,dpi=200):
    """PDFファイルからMarkdown形式の内容を抽出する関数"""
    return pymupdf4llm.to_markdown(
        file_path,
        embed_images=False,
        write_images=True,
        image_path=image_path,
        image_format="png",
        dpi=dpi,
        show_progress=True,
        use_glyphs=True,
        hdr_info=hdr_function
    )
