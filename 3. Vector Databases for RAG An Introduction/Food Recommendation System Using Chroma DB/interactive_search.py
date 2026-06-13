from shared_functions import *

def show_help_menu():
    print("\n--- HELP MENU ---")
    print("Search Examples:")
    print("  'chocolate dessert' -> Find chocolate desserts")
    print("  'Italian food'      -> Find Italian cuisine")
    print("  'low calorie'       -> Find lower-calorie options")
    print("\nCommands:")
    print("  'help' -> Show this menu")
    print("  'quit' -> Exit the system")

def suggest_related_searches(results):
    if not results:
        return
    cuisines = list(set([r['cuisine_type'] for r in results]))
    for cuisine in cuisines[:3]:
        print(f"  • Try '{cuisine} dishes' for more {cuisine} options")
    avg_calories = sum([r['food_calories_per_serving'] for r in results]) / len(results)
    if avg_calories > 350:
        print("  • Try 'low calorie' for lighter options")
    else:
        print("  • Try 'hearty meal' for more substantial dishes")


def handle_food_search(collection, query):
    results = perform_similarity_search(collection, query, 5)
    if not results:
        print("Try different keywords like 'Italian', 'sweet', or 'chicken'.")
        return
    print(f"\n Found {len(results)} recommendations:")
    for i, result in enumerate(results, 1):
        percentage_score = result['similarity_score'] * 100
        print(f"\n{i}. {result['food_name']}")
        print(f"   Match Score: {percentage_score:.1f}%")
        print(f"   Cuisine: {result['cuisine_type']}")
        print(f"   Calories: {result['food_calories_per_serving']} per serving")
        print(f"   Description: {result['food_description']}")
    suggest_related_searches(results)

def main():
    try:
        file_path = "FoodDataSet.json"
        food_items = load_food_data(file_path)
        collection = create_similarity_search_collection(
            "interactive_food_search",
            {'description': 'A collection for interactive food search'}
        )
        populate_similarity_collection(collection, food_items)

        print("Commands: Type any food to search, 'help' for examples, or 'quit' to exit.")

        while True:
            user_input = input("\n Search for food: ").strip()

            if not user_input:
                continue
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            elif user_input.lower() in ['help', 'h']:
                show_help_menu()
            else:
                handle_food_search(collection, user_input)

    except KeyboardInterrupt:
        print("System interrupted. Goodbye!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()