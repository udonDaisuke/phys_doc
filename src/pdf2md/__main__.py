from pathlib import Path

from src.pdf2md.utils.config_loader import ConfigLoader
from src.pdf2md.utils.path_utils import ensure_dir
from src.pdf2md.core.pdf_to_md_processing import PDF2MDProcessing 

def main(file_name: str):
    # Load configuration
    config_path= Path(__file__).parent/"config.yaml"
    config = ConfigLoader(config_path)

    input_pdf_dir = Path(config["input_pdf_directory"]).absolute()
    projects_dir = Path(config["project_directory"]).absolute()
    print(input_pdf_dir, projects_dir)
    ensure_dir(projects_dir/Path(str(file_name)).stem/config["output_directory_basename"]/"images")

    input_pdf_file = input_pdf_dir/file_name
    print(input_pdf_file)
    md = PDF2MDProcessing(config).process(input_pdf_file)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python -m src.pdf2md <pdf_file_name>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    main(file_name)