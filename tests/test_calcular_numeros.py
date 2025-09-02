import allure
from calcular_numeros import calcular_promedio

@allure.description("test donde se calcula el promedio")
@allure.feature("promedio")
@allure.epic("promedio")
def test_calcular_promedio():
    numeros = [1,2,3,4,5]
    resultado = calcular_promedio(numeros)
    assert resultado == 3
