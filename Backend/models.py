from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql.sqltypes import Boolean

Base = declarative_base()

class User(declarative_base()):
    """The Account class corresponds to the "accounts" database table.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)

class Recipe(declarative_base()):
    """Associated with recipes.
    """
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)
    instructions = Column(String)
    cook_time = Column(Integer)
    difficulty = Column(String)
    ingredients = relationship("Ingredient", back_populates = "recipes")

class Preference(declarative_base()):
    """Associated with preferences.
    """
    __tablename__ = 'preferences'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_allergy = Column(Boolean)

class Preference_recipe(declarative_base()):
    """The class associated with recipes and preferences relationships.
    """
    __tablename__ = 'preferences_recipes'
    id = Column(Integer, primary_key=True)
    id_preference = relationship("Preference", back_populates = "preferences_recipes")
    id_recipe = relationship("Recipe", back_populates = "preferences_recipes")

class Preference_user(declarative_base()):
    """The Account class corresponds to the "accounts" database table.
    """
    __tablename__ = 'preferences_users'
    id = Column(Integer, primary_key=True)
    id_preference = relationship("Preference", back_populates = "preferences_users")
    id_user = relationship("User", back_populates = "preferences_users")

class Ingredient(declarative_base()):
    """The Ingredients class helps with the different ingredients contained in each recipe
    """
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(String)
    is_sub = Column(Boolean)