import chromadb
from chromadb.utils import embedding_functions
import json
from typing import List, Dict, Any

client = chromadb.Client()
sentence_transformers_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

def load_food_data(file_path: str) -> List[Dict]:
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            food_data = json.load(file)

        for i, item in enumerate(food_data):
            item['food_id'] = str(item.get('food_id', i + 1))
            item['food_ingredients'] = item.get('food_ingredients', [])
            item['food_description'] = item.get('food_description', '')
            item['cuisine_type'] = item.get('cuisine_type', 'Unknown')
            item['food_calories_per_serving'] = item.get('food_calories_per_serving', 0)

            taste_features = []
            if 'food_features' in item and isinstance(item['food_features'], dict):
                for key, value in item['food_features'].items():
                    if value:
                        taste_features.append(str(value))
            item['taste_profile'] = ', '.join(taste_features)
        print(f"Successfully loaded {len(food_data)} food items.")
        return food_data

    except Exception as e:
        print(f"Error: {e}")

def create_similarity_search_collection(collection_name: str, collection_metadata: dict):
    try:
        client.delete_collection(collection_name)
    except:
        pass

    return client.create_collection(
        name=collection_name,
        embedding_function=sentence_transformers_ef,
        metadata={**collection_metadata, "hnsw:space": "cosine"}
    )

def populate_similarity_collection(collection, food_items: List[Dict]):
    documents = []
    metadatas = []
    ids = []
    used_ids = set()

    for i, food in enumerate(food_items):
        text = f"Name: {food['food_name']}. Description: {food.get('food_description', '')}. "
        text += f"Ingredients: {', '.join(food.get('food_ingredients', []))}. Cuisine: {food.get('cuisine_type', 'Unknown')}. "

        if food.get('taste_profile'):
            text += f"Taste: {food['taste_profile']}. "

        if 'food_nutritional_factors' in food and isinstance(food['food_nutritional_factors'], dict):
            nutrition = ', '.join([f"{k}: {v}" for k, v in food['food_nutritional_factors'].items()])
            text += f"Nutrition: {nutrition}."

        unique_id = str(food.get('food_id', i))
        counter = 1
        while unique_id in used_ids:
            unique_id = f"{food.get('food_id', i)}_{counter}"
            counter += 1
        used_ids.add(unique_id)

        documents.append(text)
        ids.append(unique_id)

        metadatas.append({
            "name": food["food_name"],
            "cuisine_type": food.get("cuisine_type", "Unknown"),
            "calories": food.get("food_calories_per_serving", 0),
            "description": food.get("food_description", "")
        })

    collection.add(documents=documents, metadatas=metadatas, ids=ids)
    print(f"Added {len(food_items)} food items to vector database.")

def perform_similarity_search(collection, query: str, n_results: int = 5) -> List[Dict]:
    try:
        results = collection.query(query_texts=[query], n_results=n_results)

        if not results or not results['ids'] or len(results['ids'][0]) == 0:
            return []

        formatted_results = []
        for i in range(len(results['ids'][0])):
            result = {
                'food_id': results['ids'][0][i],
                'food_name': results['metadatas'][0][i]['name'],
                'food_description': results['metadatas'][0][i]['description'],
                'cuisine_type': results['metadatas'][0][i]['cuisine_type'],
                'food_calories_per_serving': results['metadatas'][0][i]['calories'],
                'similarity_score': 1 - results['distances'][0][i],
                'distance': results['distances'][0][i]
            }
            formatted_results.append(result)
        return formatted_results

    except Exception as e:
        print(f"error: {e}")

def perform_filtered_similarity_search(collection, query: str, cuisine_filter=None, max_calories: int=None, n_results: int=5):
    filters = []
    if cuisine_filter:
        filters.append({"cuisine_type": cuisine_filter})
    if max_calories:
        filters.append({"calories": {"$lte": max_calories}})

    where_clause = None
    if len(filters) == 1:
        where_clause = filters[0]
    elif len(filters) > 1:
        where_clause = {"$and": filters}

    try:
        results = collection.query(
            query_texts=[query],
            n_results=n_results,
            where=where_clause
        )
        if not results or not results['ids'] or len(results['ids'][0]) == 0:
            return []

        formatted_results = []

        for i in range(len(results['ids'][0])):
            result = {
                'food_id': results['ids'][0][i],
                'food_name': results['metadatas'][0][i]['name'],
                'food_description': results['metadatas'][0][i]['description'],
                'cuisine_type': results['metadatas'][0][i]['cuisine_type'],
                'food_calories_per_serving': results['metadatas'][0][i]['calories'],
                'similarity_score': 1 - results['distances'][0][i]
            }
            formatted_results.append(result)
        return formatted_results

    except Exception as e:
        print(f"error: {e}")

