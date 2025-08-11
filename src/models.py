from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    date_of_suscription: Mapped[str] = mapped_column(
        String(50), nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Favorite(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        db.ForeignKey('user.id'), nullable=False, unique=True)
    planet_id: Mapped[int] = mapped_column(
        db.ForeignKey('planet.id'), unique=True)
    chraracter_id: Mapped[int] = mapped_column(
        db.ForeignKey('character.id'), unique=True)
    starship_id: Mapped[int] = mapped_column(
        db.ForeignKey('starship.id'), unique=True)

    user = db.relationship('User', back_populates='favorites')
    planet = db.relationship('Planet', back_populates='favorites')
    character = db.relationship('Character', back_populates='favorites')
    starchip = db.relationship('Starship', back_populates='favorites')

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "character_id": self.character_id,
        }


class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    climate: Mapped[str] = mapped_column(String(50), nullable=True)
    terrain: Mapped[str] = mapped_column(String(50), nullable=True)
    diameter: Mapped[int] = mapped_column(nullable=True)
    population: Mapped[int] = mapped_column(nullable=True)
    gravity: Mapped[str] = mapped_column(String(50), nullable=True)
    orbital_period: Mapped[int] = mapped_column(nullable=True)
    surface_water: Mapped[int] = mapped_column(nullable=True)
    created: Mapped[str] = mapped_column(String(50), nullable=False)
    edited: Mapped[str] = mapped_column(String(50), nullable=False)

    favorites = db.relationship('Favorite', back_populates='planet')

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "diameter": self.diameter,
            "population": self.population,
            "gravity": self.gravity,
            "orbital_period": self.orbital_period,
            "surface_water": self.surface_water,
            "created": self.created,
            "edited": self.edited,
        }


class Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    gender: Mapped[str] = mapped_column(String(50), nullable=True)
    skin_color: Mapped[str] = mapped_column(String(50), nullable=True)
    hair_color: Mapped[str] = mapped_column(String(50), nullable=True)
    eye_color: Mapped[str] = mapped_column(String(50), nullable=True)
    mass: Mapped[str] = mapped_column(String(50), nullable=True)
    homeworld: Mapped[str] = mapped_column(String(100), nullable=True)
    birth_year: Mapped[str] = mapped_column(String(50), nullable=True)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    created: Mapped[str] = mapped_column(String(50), nullable=False)
    edited: Mapped[str] = mapped_column(String(50), nullable=False)

    favorites = db.relationship('Favorite', back_populates='character')

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "skin_color": self.skin_color,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "mass": self.mass,
            "homeworld": self.homeworld,
            "birth_year": self.birth_year,
            "description": self.description,
            "created": self.created,
            "edited": self.edited,
        }


class Starship(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    model: Mapped[str] = mapped_column(String(50), nullable=True)
    manufacturer: Mapped[str] = mapped_column(String(50), nullable=True)
    starship_class: Mapped[str] = mapped_column(String(50), nullable=True)
    passengers: Mapped[int] = mapped_column(nullable=True)
    cargo_capacity: Mapped[int] = mapped_column(nullable=True)
    consumables: Mapped[str] = mapped_column(String(50), nullable=True)
    cost_in_credits: Mapped[int] = mapped_column(nullable=True)
    hyperdrive_rating: Mapped[float] = mapped_column(nullable=True)
    MGLT: Mapped[int] = mapped_column(nullable=True)
    created: Mapped[str] = mapped_column(String(50), nullable=False)
    edited: Mapped[str] = mapped_column(String(50), nullable=False)

    favorites = db.relationship('Favorite', back_populates='starship')

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "starship_class": self.starship_class,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "cost_in_credits": self.cost_in_credits,
            "hyperdrive_rating": self.hyperdrive_rating,
            "MGLT": self.MGLT,
            "created": self.created,
            "edited": self.edited,
        }
