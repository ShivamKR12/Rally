import pytest
from ursina import Ursina, Entity, Vec3
from car import Car
from ai import AICar
from server import Server

@pytest.fixture
def app():
    return Ursina()

@pytest.fixture
def car():
    return Car()

@pytest.fixture
def ai_car(car):
    return AICar(car, [], None, None, None, None, None, None)

def test_car_initialization(car):
    assert car.position == Vec3(0, 0, 4)
    assert car.rotation == Vec3(0, 0, 0)
    assert car.topspeed == 30
    assert car.acceleration == 0.35

def test_car_movement(car):
    initial_position = car.position
    car.update()
    assert car.position != initial_position

def test_ai_car_initialization(ai_car):
    assert ai_car.position == Vec3(0, 0, 0)
    assert ai_car.rotation == Vec3(0, 0, 0)

def test_ai_car_movement(ai_car):
    initial_position = ai_car.position
    ai_car.update()
    assert ai_car.position != initial_position

def test_server_initialization():
    server = Server("localhost", 12345)
    assert server.ip == "localhost"
    assert server.port == 12345

def test_server_event_handling():
    server = Server("localhost", 12345)
    server.update_server()
    assert server.server_update == True
