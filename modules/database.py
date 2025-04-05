from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class Database:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGODB_URI'))
        self.db = self.client.tap_content
        self.content_collection = self.db.content
        
    def store_content(self, content):
        """Store generated content in the database"""
        try:
            # Add metadata
            content['created_at'] = datetime.utcnow()
            content['last_accessed'] = datetime.utcnow()
            
            # Insert content
            result = self.content_collection.insert_one(content)
            return str(result.inserted_id)
        except Exception as e:
            raise Exception(f"Error storing content: {str(e)}")
    
    def get_content(self, content_id):
        """Retrieve content by ID"""
        try:
            content = self.content_collection.find_one({'_id': content_id})
            if content:
                # Update last accessed timestamp
                self.content_collection.update_one(
                    {'_id': content_id},
                    {'$set': {'last_accessed': datetime.utcnow()}}
                )
                return content
            return None
        except Exception as e:
            raise Exception(f"Error retrieving content: {str(e)}")
    
    def get_content_by_subject(self, subject):
        """Retrieve all content for a specific subject"""
        try:
            return list(self.content_collection.find({'type': subject}))
        except Exception as e:
            raise Exception(f"Error retrieving content by subject: {str(e)}")
    
    def get_content_by_topic(self, subject, topic):
        """Retrieve content for a specific subject and topic"""
        try:
            return list(self.content_collection.find({
                'type': subject,
                'topic': topic
            }))
        except Exception as e:
            raise Exception(f"Error retrieving content by topic: {str(e)}")
    
    def update_content(self, content_id, updates):
        """Update existing content"""
        try:
            result = self.content_collection.update_one(
                {'_id': content_id},
                {'$set': updates}
            )
            return result.modified_count > 0
        except Exception as e:
            raise Exception(f"Error updating content: {str(e)}")
    
    def delete_content(self, content_id):
        """Delete content by ID"""
        try:
            result = self.content_collection.delete_one({'_id': content_id})
            return result.deleted_count > 0
        except Exception as e:
            raise Exception(f"Error deleting content: {str(e)}")
    
    def get_popular_content(self, limit=10):
        """Retrieve most accessed content"""
        try:
            return list(self.content_collection.find().sort(
                'last_accessed', -1
            ).limit(limit))
        except Exception as e:
            raise Exception(f"Error retrieving popular content: {str(e)}") 