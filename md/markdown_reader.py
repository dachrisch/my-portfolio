from os.path import join


class MarkdownReader:
    def __init__(self, directory: str):
        self.directory = directory

    def read(self, filename: str) -> str:
        with open(join(self.directory, filename) + '.md') as md_file:
            return md_file.read()


md = MarkdownReader('md')
