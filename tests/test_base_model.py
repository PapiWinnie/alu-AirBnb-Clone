import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid
import time


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up test instances."""
        self.model = BaseModel()
        self.model.name = "Test"
        self.model.number = 42

    def test_id(self):
        """Test if id is a valid UUID."""
        self.assertTrue(uuid.UUID(self.model.id))

    def test_created_at(self):
        """Test if created_at is a datetime object."""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """Test if updated_at is a datetime object."""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        """Test save method updates updated_at."""
        old_updated_at = self.model.updated_at
        time.sleep(0.001) 
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test conversion of instance to dictionary."""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["name"], "Test")
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def test_init_from_dict(self):
        """Test re-creation of instance from dictionary."""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.name, new_model.name)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)
        self.assertFalse(self.model is new_model)  # Different objects
