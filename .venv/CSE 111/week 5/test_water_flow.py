from pytest import approx
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, reynolds_number, pressure_loss_from_pipe_reduction, pressure_loss_from_fittings, kPa_to_psi

# Test for water_column_height function
def test_water_column_height():
    assert water_column_height(0, 0) == 0
    assert water_column_height(0, 10) == approx(7.5, abs=0.001)
    assert water_column_height(25, 0) == 25
    assert water_column_height(48.3, 12.8) == approx(57.9, abs=0.001)

# Test for pressure_gain_from_water_height function
def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0) == approx(0, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50) == approx(489.450, abs=0.001)

# Test for pressure_loss_from_pipe function
def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75) == 0
    assert pressure_loss_from_pipe(0.048692, 200, 0, 1.75) == 0
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 0) == 0
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)

# Tests for pressure_loss_from_fittings function
def test_pressure_loss_from_fittings():
    assert pytest.approx(pressure_loss_from_fittings(0, 3), abs=0.001) == 0
    assert pytest.approx(pressure_loss_from_fittings(1.65, 0), abs=0.001) == 0
    assert pytest.approx(pressure_loss_from_fittings(1.65, 2), abs=0.001) == -0.109
    assert pytest.approx(pressure_loss_from_fittings(1.75, 2), abs=0.001) == -0.122
    assert pytest.approx(pressure_loss_from_fittings(1.75, 5), abs=0.001) == -0.306

# Tests reynolds number
def test_reynolds_number():
    assert pytest.approx(reynolds_number(0.048692, 0), abs=1) == 0
    assert pytest.approx(reynolds_number(0.048692, 1.65), abs=1) == 80069
    assert pytest.approx(reynolds_number(0.048692, 1.75), abs=1) == 84922
    assert pytest.approx(reynolds_number(0.28687, 1.65), abs=1) == 471729
    assert pytest.approx(reynolds_number(0.28687, 1.75), abs=1) == 500318

# Tests for pressure_loss_from_pipe_reduction function
def test_pressure_loss_from_pipe_reduction():
    assert pytest.approx(pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692), abs=0.001) == 0
    assert pytest.approx(pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692), abs=0.001) == -163.744
    assert pytest.approx(pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692), abs=0.001) == -184.182
    
# Tests for kPA_to_psi
def test_kPa_to_psi():
    # Test a known value of kPa
    assert abs(kPa_to_psi(100) - 14.5038) < 0.0001  # 100 kPa should convert to 14.5038 psi

    # Test the conversion for 0 kPa
    assert kPa_to_psi(0) == 0

    # Test a higher value of kPa
    assert abs(kPa_to_psi(200) - 29.0076) < 0.0001  # 200 kPa should convert to 29.0076 psi

    # Test a very small value
    assert abs(kPa_to_psi(1) - 0.145038) < 0.0001  # 1 kPa should convert to 0.145038 psi


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

