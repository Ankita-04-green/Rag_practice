from src.data_loader import load_all_documents
# from src.embedding import EmbeddingPipeline
# from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

if __name__ == "__main__":
    # docs = load_all_documents("./data")
    # print("Total documents loaded are: ",len(docs))
    # store = FaissVectorStore("faiss_store")
    # store.build_from_documents(docs)
    # store.load()
    # print(len(store.query("What is machine learning?", top_k=5)))
    rag_search = RAGSearch()
    query = input("\nENTER YOUR QUERY: ")
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("\nSummary: ", summary)