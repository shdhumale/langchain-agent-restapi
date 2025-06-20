
import requests

class LangChainAgent:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_all_objects(self):
        return requests.get(f"{self.base_url}/objects").json()

    def get_objects_by_ids(self, ids):
        return requests.get(f"{self.base_url}/objects", params={"id": ids}).json()

    def get_single_object(self, object_id):
        return requests.get(f"{self.base_url}/objects/{object_id}").json()

    def add_object(self, data):
        return requests.post(f"{self.base_url}/objects", json=data).json()

    def update_object(self, object_id, data):
        return requests.put(f"{self.base_url}/objects/{object_id}", json=data).json()

    def partially_update_object(self, object_id, data):
        return requests.patch(f"{self.base_url}/objects/{object_id}", json=data).json()

    def delete_object(self, object_id):
        return requests.delete(f"{self.base_url}/objects/{object_id}").json()
    
agent = LangChainAgent("https://api.restful-api.dev")

# Get all objects
print("agent.get_all_objects() -------------",agent.get_all_objects())

# Get objects by IDs
print("(agent.get_objects_by_ids([3, 5, 10]))--------------",(agent.get_objects_by_ids([3, 5, 10])))

# Get single object
print("agent.get_single_object(7)---------------", agent.get_single_object(7))

# Add object
print("agent.add_object----------")
created = agent.add_object({"name": "New Object", "data": "Some data"});
print("Created object:", created)
print("Created object:", created['id'])

# Update object
print("agent.update_object-----------",agent.update_object(created['id'], {"name": "Updated Object", "data": "Updated data"}))

# Partially update object
print("agent.partially_update_object ------------------",agent.partially_update_object(created['id'], {"data": "Partially updated data"}))

# Delete object
print("agent.delete_object------------------",agent.delete_object(created['id']))