import chromadb

client = chromadb.PersistentClient(path="./chroma/db")

collection = client.get_or_create_collection("agrios")

collection.add(
    documents=[
        "Brown spot disease affects paddy leaves."
    ],
    ids=["doc1"]
)

results = collection.query(
    query_texts=["My paddy leaves have brown spots"],
    n_results=1
)

print(results["documents"])