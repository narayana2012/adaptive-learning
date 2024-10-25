from datetime import datetime
import os
from pymongo import MongoClient


class DbConnection:

    def __init__(self):
        self.srv_uri = os.getenv("MONGO_DB_SRV")
        print(self.srv_uri)
        self.mongo_client = MongoClient(self.srv_uri)
        self.db = self.mongo_client["ai_tutor"]


    def find(self, collection_name, query):
        """
        Finds a document in a MongoDB collection.

        Args:
            collection_name (str): Collection name.
            query (dict): Query to find the document.

        Returns:
            dict: The document found.
        """
        return self.db[collection_name].find(query)
    

    def find_one(self, collection_name, query):
        """
        Finds a document in a MongoDB collection.

        Args:
            collection_name (str): Collection name.
            query (dict): Query to find the document.

        Returns:
            dict: The document found.
        """
        return self.db[collection_name].find_one(query)
    
    def insert_data(self,collection_name, document):
        """
        Inserts a document into a MongoDB collection.

        Args:
            collection_name (str): Collection name.
            document (dict): Document to be inserted.

        Returns:
            ObjectId: The ID of the inserted document.
        """
        inserted_id = self.db[collection_name].insert_one(document).inserted_id
        return inserted_id

    def update_record(self, collection, record, process_status, response_json=None, usage_tokens_and_costs=None,user_message= None, system_context=None):
        """
        Updates a record in a MongoDB collection.

        Args:
            collection (pymongo.collection.Collection): The MongoDB collection.
            record (dict): The record to be updated.
            process_status (str): The status to be set.
            response_json (dict, optional): JSON response to be added.

        Returns:
            str: The ID of the updated record.
        """
        print(f"Processing record with _id: {record['_id']}")
        self.db[collection].update_one(
            {"_id": record["_id"]},
            {
                "$set": {
                    "status": process_status,
                    "response_payload": response_json,
                    "usage_tokens_and_costs": usage_tokens_and_costs,
                    "updated_at": datetime.now(),
                    "user_message": user_message,
                    "system_context": system_context
                }
            }
        )
        print(f"Record with _id: {record['_id']} has been updated to {process_status}.")
        return record['_id']