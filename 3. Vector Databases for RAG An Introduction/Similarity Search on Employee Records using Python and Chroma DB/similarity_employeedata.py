import chromadb
from chromadb.utils import embedding_functions

ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

def perform_advanced_search(collection):
    try:

        query = ["Python developer with web development experience"]
        results = collection.query(
            query_texts=query,
            n_results=3
        )
        print(f"The result is generated for the query: {query}")

        print("1. Extracting the results for the query:")
        for i in range(len(results['ids'][0])):
            doc_id=results['ids'][0][i]
            metadata= results['metadatas'][0][i]
            distance=results['distances'][0][i]
            print(f"  {i + 1}. {metadata['name']} ({doc_id}) - Distance: {distance:.4f}")
            print(f"     Role: {metadata['role']} | Skills: {metadata['skills']}")

        print("2. Filter with 10 years experience")
        senior_results = collection.get(
            where={"experience": {"$gt": 10}}
        )
        print(f"Found {len(senior_results['ids'])} senior employees:")
        for i in range(len(senior_results['ids'])):
            metadata = senior_results['metadatas'][i]
            print(f"  - {metadata['name']}: {metadata['role']} ({metadata['experience']})")
                  
        print("3. Hybrid search. query with senior python developer full-stack and 8+ experience and location")

        hybrid_results = collection.query(
            query_texts=["senior Python developer full-stack"],
            n_results=5,
            where={
                "$and":[
                    {"experience": {"$gte": 8}},
                    {"location": {"$in": ["San Francisco", "New York", "Seattle"]}}
                ]
            }
        )

        if not hybrid_results['ids'][0]:
            print("No employees matched all criteria.")
            return

        print(f"Found {len(hybrid_results['ids'][0])} matching employees:")
        for i in range(len(hybrid_results['ids'][0])):
            doc_id = hybrid_results['ids'][0][i]
            metadata = hybrid_results['metadatas'][0][i]
            distance = hybrid_results['distances'][0][i]
            print(f"  {i + 1}. {metadata['name']} ({doc_id}) - Distance: {distance:.4f}")
            print(f"     Location: {metadata['location']} | Experience: {metadata['experience']} years")


    except Exception as e:
        print(f"error: {e}")

def main():
    try:

        print("Initializing chroma db client")
        client = chromadb.Client()
        collection_name = "employee_collection"
        collection = client.create_collection(
            name=collection_name,
            embedding_function=ef,
            metadata={
                "description": "A collection for storing employee data",
                "hnsw:space": "cosine"
            }
        )
        print(f"Collection created: {collection.name}")

        employees = [
            {"id": "employee_1", "name": "John Doe", "experience": 5, "department": "Engineering",
             "role": "Software Engineer", "skills": "Python, JavaScript, React, Node.js, databases",
             "location": "New York", "employment_type": "Full-time"},
            {"id": "employee_2", "name": "Jane Smith", "experience": 8, "department": "Marketing",
             "role": "Marketing Manager", "skills": "Digital marketing, SEO, content strategy, analytics, social media",
             "location": "Los Angeles", "employment_type": "Full-time"},
            {"id": "employee_3", "name": "Alice Johnson", "experience": 3, "department": "HR", "role": "HR Coordinator",
             "skills": "Recruitment, employee relations, HR policies, training programs", "location": "Chicago",
             "employment_type": "Full-time"},
            {"id": "employee_4", "name": "Michael Brown", "experience": 12, "department": "Engineering",
             "role": "Senior Software Engineer",
             "skills": "Java, Spring Boot, microservices, cloud architecture, DevOps", "location": "San Francisco",
             "employment_type": "Full-time"},
            {"id": "employee_5", "name": "Emily Wilson", "experience": 2, "department": "Marketing",
             "role": "Marketing Assistant",
             "skills": "Content creation, email marketing, market research, social media management",
             "location": "Austin", "employment_type": "Part-time"},
            {"id": "employee_6", "name": "David Lee", "experience": 15, "department": "Engineering",
             "role": "Engineering Manager",
             "skills": "Team leadership, project management, software architecture, mentoring", "location": "Seattle",
             "employment_type": "Full-time"},
            {"id": "employee_7", "name": "Sarah Clark", "experience": 8, "department": "HR", "role": "HR Manager",
             "skills": "Performance management, compensation planning, policy development, conflict resolution",
             "location": "Boston", "employment_type": "Full-time"},
            {"id": "employee_8", "name": "Chris Evans", "experience": 20, "department": "Engineering",
             "role": "Senior Architect",
             "skills": "System design, distributed systems, cloud platforms, technical strategy",
             "location": "New York", "employment_type": "Full-time"},
            {"id": "employee_9", "name": "Jessica Taylor", "experience": 4, "department": "Marketing",
             "role": "Marketing Specialist",
             "skills": "Brand management, advertising campaigns, customer analytics, creative strategy",
             "location": "Miami", "employment_type": "Full-time"},
            {"id": "employee_10", "name": "Alex Rodriguez", "experience": 18, "department": "Engineering",
             "role": "Lead Software Engineer",
             "skills": "Full-stack development, React, Python, machine learning, data science", "location": "Denver",
             "employment_type": "Full-time"},
            {"id": "employee_11", "name": "Hannah White", "experience": 6, "department": "HR",
             "role": "HR Business Partner",
             "skills": "Strategic HR, organizational development, change management, employee engagement",
             "location": "Portland", "employment_type": "Full-time"},
            {"id": "employee_12", "name": "Kevin Martinez", "experience": 10, "department": "Engineering",
             "role": "DevOps Engineer", "skills": "Docker, Kubernetes, AWS, CI/CD pipelines, infrastructure automation",
             "location": "Phoenix", "employment_type": "Full-time"},
            {"id": "employee_13", "name": "Rachel Brown", "experience": 7, "department": "Marketing",
             "role": "Marketing Director",
             "skills": "Strategic marketing, team leadership, budget management, campaign optimization",
             "location": "Atlanta", "employment_type": "Full-time"},
            {"id": "employee_14", "name": "Matthew Garcia", "experience": 3, "department": "Engineering",
             "role": "Junior Software Engineer",
             "skills": "JavaScript, HTML/CSS, basic backend development, learning frameworks", "location": "Dallas",
             "employment_type": "Full-time"},
            {"id": "employee_15", "name": "Olivia Moore", "experience": 12, "department": "Engineering",
             "role": "Principal Engineer",
             "skills": "Technical leadership, system architecture, performance optimization, mentoring",
             "location": "San Francisco", "employment_type": "Full-time"}
        ]

        employee_documents = []

        for emp in employees:
            doc = f"{emp['role']} with {emp['experience']} years of experience in {emp['department']}. Skills: {emp['skills']}. Located in {emp['location']}. Employment type: {emp['employment_type']}."
            employee_documents.append(doc)

        print(f"employee documents generated. length: {len(employee_documents)}")

        metadatas = []
        for emp in employees:
            metadatas.append({
                "name": emp["name"],
                "department": emp["department"],
                "role": emp["role"],
                "experience": emp["experience"],
                "location": emp["location"],
                "employment_type": emp["employment_type"],
                "skills": emp["skills"]
            })
        print(f"employee metadatas generated. length: {len(metadatas)}")

        print("Embedding data and adding to collection")
        collection.add(
            ids=[emp['id'] for emp in employees],
            documents=employee_documents,
            metadatas=metadatas
        )
        print("Documents added successfully")

        all_items = collection.get()
        print(f"Successfully loaded the document. Document length: {len(all_items['documents'])}")

    except Exception as e:
        print(f"Error: {e}")

    perform_advanced_search(collection)

if __name__ == "__main__":
    main()