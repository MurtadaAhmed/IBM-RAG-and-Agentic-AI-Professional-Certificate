# Food Recommendation System Using Chroma DB

## Description
This project implements a food recommendation system using Chroma DB, a vector database. It allows users to search for food items based on similarity and apply filters like cuisine type and calorie limits.

## Files
- `FoodDataSet.json`: Contains the raw food data, including details like name, description, ingredients, nutritional factors, and cuisine type.
- `shared_functions.py`: This file contains the core logic for interacting with Chroma DB. It includes functions to:
    - Load food data from a JSON file.
    - Create a Chroma DB collection for similarity search.
    - Populate the collection with food items, generating embeddings for their descriptions and other features.
    - Perform similarity searches based on a query.
    - Perform filtered similarity searches, allowing for additional criteria like cuisine type and maximum calories.
- `interactive_search.py`: This script provides an interactive command-line interface for users to perform food searches. It utilizes the functions from `shared_functions.py` to:
    - Initialize the Chroma DB collection.
    - Prompt the user for search queries and optional filters.
    - Display the search results in a user-friendly format.

## Setup
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Food-Recommendation-System-Using-Chroma-DB.git
    cd Food-Recommendation-System-Using-Chroma-DB
    ```
2.  **Install dependencies:**
    ```bash
    pip install chromadb sentence-transformers
    ```

## Usage
To run the interactive food recommendation system, execute the `interactive_search.py` script:

```bash
python interactive_search.py
```

The script will then prompt you to enter a food query. You can also specify optional filters for cuisine type and maximum calories.

**Example Interaction:**

```
Enter your food query (e.g., "sweet dessert", "spicy chicken dish"): sweet dessert
Enter cuisine type (optional, e.g., Italian, American):
Enter maximum calories (optional, e.g., 300): 350

Searching for "sweet dessert" with max calories 350...

Recommended Food Items:
------------------------
Food Name: Apple Pie
Description: A classic dessert made with a buttery, flaky crust filled with tender, spiced apples.
Cuisine: American
Calories: 320
Similarity Score: 0.85

Food Name: Tiramisu
Description: An Italian dessert made with layers of coffee-soaked ladyfingers and mascarpone cheese, dusted with cocoa powder.
Cuisine: Italian
Calories: 240
Similarity Score: 0.82

Food Name: Crème Brûlée
Description: A creamy custard dessert topped with a layer of hardened caramelized sugar.
Cuisine: French
Calories: 300
Similarity Score: 0.80

Food Name: Cheesecake
Description: A creamy dessert made with a base of cream cheese and a graham cracker crust, often topped with fruit.
Cuisine: American
Calories: 350
Similarity Score: 0.78

Food Name: Pavlova
Description: A meringue-based dessert topped with whipped cream and fresh fruits.
Cuisine: Australian
Calories: 150
Similarity Score: 0.75
```
