from qdrant_client import QdrantClient

client = QdrantClient(host="localhost", port=6333)

# Lấy danh sách tất cả các collection
collections = client.get_collections().collections

for c in collections:
    name = c.name
    client.delete_collection(name)
    print(f"✅ Deleted collection: {name}")

print("🎯 All collections deleted successfully!")
