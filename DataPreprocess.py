from langchain_community.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter,RecursiveCharacterTextSplitter

class Document():

    def __init__(self, file_dir):
        self.file_dir = file_dir
        self.type = file_dir.split(".")[-1]
        self.docs = self.load_text(self.file_dir)
    
    def load_text(self,file_dir):
        if self.type == "pdf":
            loader = UnstructuredFileLoader(file_dir, mode="elements")
        elif self.type == "txt":
            loader =  UnstructuredFileLoader(file_dir)

        print("Loading...")
        docs = loader.load()

        return docs
    
    def text_split(self):
        print("Spiltting...")
        if self.type == "pdf":
            docs = [doc.page_content for doc in self.docs]

        text = ""
        for doc in docs:
            text += doc
            text += "\n\n"

        text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n", ".", "!", "\"", " "],
            keep_separator = False,
            chunk_size = 196,
            chunk_overlap  = 0.2,
            length_function = len,
        )

        chunks = text_splitter.split_documents(self.docs)
        chunks = [chunk.page_content for chunk in chunks]
        return chunks