from ..utils.config_loader import ConfigLoader
from ..core.custom_hdr_info import custom_hdr_info
from ..core.markdown_contents_preprocessor import MarkdownContentsPreprocessor 
from ..modules.contents_extractor import extraction_from_pdf 
from pathlib import Path

class PDF2MDProcessing:

    def __init__(self, config: ConfigLoader):
        self.config = config
        self.header_rules = self.config["header_rules"]
        self.project_directory = self.config["project_directory"]
        

    def process(self, file_path):
        output_directory = (Path(self.project_directory)/(Path(file_path).stem)/self.config["output_directory_basename"]).absolute()
        image_directory = (Path(self.project_directory)/(Path(file_path).stem)/"images").absolute()

        hdr_func = custom_hdr_info(self.header_rules)
        contents = extraction_from_pdf(file_path, hdr_func, image_directory)
        md = MarkdownContentsPreprocessor(contents)
        md.separate_chapters()
        md.write(output_directory, separate_chapters=True)
