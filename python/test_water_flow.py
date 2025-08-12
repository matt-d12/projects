"""
File Name: test_water_flow.py
Author: Matt D.
Course: CSE 111 | BYU-Idaho
Purpose: To test out the water_flow program
"""
import pytest
from pytest import approx
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction

#Test water_column_height function from other file, test numbers from assignment page
#Arguments passed in are tower_height, tank_height | return expected water column height
def test_water_column_height():
    assert water_column_height(0, 0) == approx(0, abs=0)
    assert water_column_height(0, 10) == approx(7.5, abs=0.1)
    assert water_column_height(25, 0) == approx(25, abs=0)
    assert water_column_height(48.3, 12.8) == approx(57.9, abs=0.01)

#Test pressure_gain_from_water_height function from other file, test numbers from assignment page
#Argument passed in is water_column_height | returns expected pressure
def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0) == approx(0, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50) == approx(489.450, abs=0.001)

#Test pressure_loss_from_pipe function from other file, test numbers from assignment page
#Arguments passed in are pipe_diameter, pipe_length, friction_factor, fluid_velocity | returns expected pressure loss
def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0, 1.75) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 0) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65) == approx(-100.462, abs=0.001)    
    assert pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)

#Test pressure_loss_from_fittings function from other file, test numbers from assignment page
#Arguments passed in are fluid_velocity, quantity_fittings | returns expected pressure loss
def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(0, 3) == approx(0, abs=0.1)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0, abs=0.1)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.1)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.1)
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.1)

#Test reynolds_number function from other file, test numbers from assignment page
#Arguments passed in are hydraulic_diameter, fluid_velocity | returns reynolds number
def test_reynolds_number():
    assert reynolds_number(0.048692, 0) == approx(0, abs=1)
    assert reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
    assert reynolds_number(0.048692, 1.75) == approx(84922, abs=1)
    assert reynolds_number(0.28687, 1.65) == approx(471729, abs=1)
    assert reynolds_number(0.28687, 1.75) == approx(500318, abs=1)

#Test pressure_loss_from_pipe-reduction function from other file, test numbers from assignment page
#Arguments passed in are larger_diameter,fluid_velocity, reynolds_number, smaller_diameter | returns expected pressure loss
def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])