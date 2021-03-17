import os
import numpy as np
import unittest
from context import deepti
# print(deepti.equi)

class TestEquiHeader(unittest.TestCase):
    def setUp(self) :
        # kwargs={'nsteps':100000, prt_freq, dump_freq, temp, pres, tau_t, tau_p, conf_file}
        self.maxDiff = None

    def test_equi_header_npt(self):
        equi_settings = dict(nsteps=1000000, thermo_freq=10, dump_freq=100000, 
            temp=400, pres=200000, tau_t=0.2, 
            tau_p=2.0, mass_map=[118.71], equi_conf='conf.lmp')

        ret1 = """clear
# --------------------- VARIABLES-------------------------
variable        NSTEPS          equal 1000000
variable        THERMO_FREQ     equal 10
variable        DUMP_FREQ       equal 100000
variable        NREPEAT         equal ${NSTEPS}/${DUMP_FREQ}
variable        TEMP            equal 400.000000
variable        PRES            equal 200000.000000
variable        TAU_T           equal 0.200000
variable        TAU_P           equal 2.000000
# ---------------------- INITIALIZAITION ------------------
units           metal
boundary        p p p
atom_style      atomic
# --------------------- ATOM DEFINITION ------------------
box             tilt large
read_data       conf.lmp
change_box      all triclinic
mass            1 118.710000
"""
        ret2 = deepti.equi.gen_equi_header(equi_settings=equi_settings)
        self.assertEqual(ret1, ret2)

    def test_equi_header_nvt(self):
        equi_settings = dict(nsteps=1000000, thermo_freq=10, dump_freq=100000, 
            temp=400, pres=None, tau_t=0.2, 
            tau_p=2.0, mass_map=[118.71], equi_conf='conf.lmp')
        ret1 = """clear
# --------------------- VARIABLES-------------------------
variable        NSTEPS          equal 1000000
variable        THERMO_FREQ     equal 10
variable        DUMP_FREQ       equal 100000
variable        NREPEAT         equal ${NSTEPS}/${DUMP_FREQ}
variable        TEMP            equal 400.000000
variable        TAU_T           equal 0.200000
variable        TAU_P           equal 2.000000
# ---------------------- INITIALIZAITION ------------------
units           metal
boundary        p p p
atom_style      atomic
# --------------------- ATOM DEFINITION ------------------
box             tilt large
read_data       conf.lmp
change_box      all triclinic
mass            1 118.710000
"""
        ret2 = deepti.equi.gen_equi_header(equi_settings=equi_settings)
        self.assertEqual(ret1, ret2)


    def test_equi_header_npt_multi_element(self):
        equi_settings = dict(nsteps=1000000, thermo_freq=10, dump_freq=100000, 
            temp=400, pres=None, tau_t=0.2, 
            tau_p=2.0, mass_map=[118.71, 196.97], equi_conf='conf.lmp')
        ret1 = """clear
# --------------------- VARIABLES-------------------------
variable        NSTEPS          equal 1000000
variable        THERMO_FREQ     equal 10
variable        DUMP_FREQ       equal 100000
variable        NREPEAT         equal ${NSTEPS}/${DUMP_FREQ}
variable        TEMP            equal 400.000000
variable        TAU_T           equal 0.200000
variable        TAU_P           equal 2.000000
# ---------------------- INITIALIZAITION ------------------
units           metal
boundary        p p p
atom_style      atomic
# --------------------- ATOM DEFINITION ------------------
box             tilt large
read_data       conf.lmp
change_box      all triclinic
mass            1 118.710000
mass            2 196.970000
"""
        ret2 = deepti.equi.gen_equi_header(equi_settings=equi_settings)
        self.assertEqual(ret1, ret2)

if __name__ == '__main__':
    unittest.main()