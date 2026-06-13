import chromadb
from chromadb.utils import embedding_functions

ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

def perform_similarity_search(collection):
    try:
        print("Performing similarity search")
        query_term = ["red", "fresh"]

        results = collection.query(
            query_texts=query_term,
            n_results=3

        )

        if not results or not results['ids'] or len(results['ids'][0]) == 0:
            print(f"No documents found similar to {query_term}")
            return

        for query_index in range(len(query_term)):
            current_query = query_term[query_index]
            print(f'\nTop 3 similar documents to "{current_query}":')
            for i in range (min(3, len(results['ids'][query_index]))):
                doc_id = results['ids'][query_index][i]
                score = results['distances'][query_index][i]
                text = results['documents'][query_index][i]

                print(f'ID: {doc_id}, Text: "{text}", Distance Score: {score:.4f}')

    except Exception as e:
        print(f"Error {e}")


def main():
    try:
        print("Creating chroma db client")
        client = chromadb.Client()
        collection_name = "my_grocery_collection"


        print("Creating collection using Cosine Distance")
        collection = client.create_collection(
            name =collection_name,
            embedding_function=ef,
            metadata= {
                "description": "A collection for storing grocery data",
                "hnsw:space": "cosine"
            }

        )
        print(f"Collection created successfully: {collection.name}")

        texts = [
            'fresh red apples',
            'organic bananas',
            'ripe mangoes',
            'whole wheat bread',
            'farm-fresh eggs',
            'natural yogurt',
            'frozen vegetables',
            'grass-fed beef',
            'free-range chicken',
            'fresh salmon fillet',
            'aromatic coffee beans',
            'pure honey',
            'golden apple',
            'red fruit'
        ]

        ids = [f"food_{index + 1}" for index, _ in enumerate(texts)]

        print("Adding document, metadata, and ID to the database")
        collection.add(
            documents=texts,
            metadatas=[{"source": "grocery_store", "category": "food"} for _ in texts],
            ids=ids
        )
        print("Documents added successfully")

        all_items = collection.get()
        print("Collection contents:")
        print(f"Number of documents loaded: {len(all_items['documents'])}")

        perform_similarity_search(collection)


    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
