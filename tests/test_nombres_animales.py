import allure
from animales import obtener_nombres_animales

@allure.description("test donde se devuelve una lista de animales")
@allure.feature("aniamles")
@allure.epic("listas de nombres")
def test_obtener_nombres():
    nombres = obtener_nombres_animales()
    assert isinstance(nombres, list)
