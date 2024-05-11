import pytest
from WeightHelper import WeightHelper

def test_calculate_bmi():
    assert WeightHelper.calculate_bmi(1.75, 70) == 22.857142857142858

def test_calculate_bmi_accepted():
    height = 1000
    weight = 10000
    bmi = WeightHelper.calculate_bmi(height, weight)
    assert bmi == 0.01 

def test_calculate_bmi_accepted():
    height = -1000
    weight = -10000
    bmi = WeightHelper.calculate_bmi(height, weight)
    assert bmi == -0.01  

def test_get_category_accepted():
    category = WeightHelper.get_category(100000 - 180, float('inf') - 80)
    assert category == "Obese"

def test_get_category_accepted():
    category = WeightHelper.get_category(180, 80)
    assert category == "Normal weight"

def test_get_category_accepted():
    category = WeightHelper.get_category(180, 50)
    assert category == "Underweight"

