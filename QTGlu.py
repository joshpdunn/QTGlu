# QTGlu.py
# Joshua Dunn
# Created 17 Aug 2022
# Last update 17 Aug 2022
# This is the main backend for the QTGlu Application

# __MODULES__

# import math
# MODULE FOR GETTING PROJECT DIRECTORY
import os
# MODULE FOR ACCESSING ARGUMENTS
import sys
# MODULES FOR PyQT
from PySide6.QtWidgets import (
    QMainWindow,
    QStatusBar,
    QWidget,
    QTabWidget,
    QGroupBox,
    Line,
    QCheckBox,
    QLabel,
    QPushButton,
    QTextEdit,
    QGroupBox,
    QTextBrowser,
    QApplication,)
from PySide6 import  QTCore, QTGui
# TOOL FOR USING UI FILE INSTEAD OF NEEDING TO CONVERT TO PY FILE MANUALLY
from PySide6.QtUiTools import QUiLoader
# ACCESS Qt METHOD NAMES IN A MORE PYTHONIC, PEP8 STYLE
from __feature__ import snake_case, true_property
# END IMPORTS

# GLOABAL VARIABLES
loader = QUILoader()
basedir = os.path.dirname(__file__)


# CLASSES - EACH WINDOW HAS A CLASS. EACH CLASS HAS FUNCTIONS FOR HANDLING INTERACTIONS WITH ITS INTERFACE
class MainUI(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load( os.path.join(basedir, "QTGluMain.ui"), None )
        self.ui.show()
    def gen_released(self):
        slot_dict = { 1 : self.ui.central.ts_tab.ts_group.slot01.current_text(),
                      2 : self.ui.central.ts_tab.ts_group.slot02.current_text(),
                      3 : self.ui.central.ts_tab.ts_group.slot03.current_text(),
                      4 : self.ui.central.ts_tab.ts_group.slot04.current_text(),
                      5 : self.ui.central.ts_tab.ts_group.slot05.current_text(),
                      6 : self.ui.central.ts_tab.ts_group.slot06.current_text(),
                      7 : self.ui.central.ts_tab.ts_group.slot07.current_text(),
                      8 : self.ui.central.ts_tab.ts_group.slot08.current_text(),
                      9 : self.ui.central.ts_tab.ts_group.slot09.current_text(),
                      10: self.ui.central.ts_tab.ts_group.slot10.current_text(),
                      11: self.ui.central.ts_tab.ts_group.slot11.current_text(),
                      12: self.ui.central.ts_tab.ts_group.slot12.current_text() }
        param_tup = ( self.ui.central.tabs.settings_tab.param_group.glu_int.to_plain_text(), # 0
                      self.ui.central.tabs.settings_tab.param_group.gap_int.to_plain_text(), # 1
                      self.ui.central.tabs.settings_tab.param_group.glu_fr.to_plain_text(), # 2
                      self.ui.central.tabs.settings_tab.param_group.gap_fr.to_plain_text(), # 3
                      self.ui.central.tabs.settings_tab.cal_group.slot_01_x.to_plain_text(), # 4
                      self.ui.central.tabs.settings_tab.cal_group.slot_01_y.to_plain_text(), # 5
                      self.ui.central.tabs.settings_tab.cal_group.slot_01_z.to_plain_text(), # 6
                      self.ui.central.tabs.settings_tab.cal_group.slot_02_x.to_plain_text(), # 7
                      self.ui.central.tabs.settings_tab.cal_group.slot_02_y.to_plain_text(), # 8
                      self.ui.central.tabs.settings_tab.cal_group.slot_02_z.to_plain_text(), # 9
                      self.ui.central.tabs.settings_tab.cal_group.slot_03_x.to_plain_text(), # 10
                      self.ui.central.tabs.settings_tab.cal_group.slot_03_y.to_plain_text(), # 11
                      self.ui.central.tabs.settings_tab.cal_group.slot_03_z.to_plain_text(), # 12
                      self.ui.central.tabs.settings_tab.cal_group.slot_04_x.to_plain_text(), # 13
                      self.ui.central.tabs.settings_tab.cal_group.slot_04_y.to_plain_text(), # 14
                      self.ui.central.tabs.settings_tab.cal_group.slot_04_z.to_plain_text(), # 15
                      self.ui.central.tabs.settings_tab.cal_group.slot_05_x.to_plain_text(), # 16
                      self.ui.central.tabs.settings_tab.cal_group.slot_05_y.to_plain_text(), # 17
                      self.ui.central.tabs.settings_tab.cal_group.slot_05_z.to_plain_text(), # 18
                      self.ui.central.tabs.settings_tab.cal_group.slot_06_x.to_plain_text(), # 19
                      self.ui.central.tabs.settings_tab.cal_group.slot_06_y.to_plain_text(), # 20
                      self.ui.central.tabs.settings_tab.cal_group.slot_06_z.to_plain_text(), # 21
                      self.ui.central.tabs.settings_tab.cal_group.slot_07_x.to_plain_text(), # 22
                      self.ui.central.tabs.settings_tab.cal_group.slot_07_y.to_plain_text(), # 23
                      self.ui.central.tabs.settings_tab.cal_group.slot_07_z.to_plain_text(), # 24
                      self.ui.central.tabs.settings_tab.cal_group.slot_08_x.to_plain_text(), # 25
                      self.ui.central.tabs.settings_tab.cal_group.slot_08_y.to_plain_text(), # 26
                      self.ui.central.tabs.settings_tab.cal_group.slot_08_z.to_plain_text(), # 27
                      self.ui.central.tabs.settings_tab.cal_group.slot_09_x.to_plain_text(), # 28
                      self.ui.central.tabs.settings_tab.cal_group.slot_09_y.to_plain_text(), # 29
                      self.ui.central.tabs.settings_tab.cal_group.slot_09_z.to_plain_text(), # 30
                      self.ui.central.tabs.settings_tab.cal_group.slot_10_x.to_plain_text(), # 31
                      self.ui.central.tabs.settings_tab.cal_group.slot_10_y.to_plain_text(), # 32
                      self.ui.central.tabs.settings_tab.cal_group.slot_10_z.to_plain_text(), # 33
                      self.ui.central.tabs.settings_tab.cal_group.slot_11_x.to_plain_text(), # 34
                      self.ui.central.tabs.settings_tab.cal_group.slot_11_y.to_plain_text(), # 35
                      self.ui.central.tabs.settings_tab.cal_group.slot_11_z.to_plain_text(), # 36
                      self.ui.central.tabs.settings_tab.cal_group.slot_12_x.to_plain_text(), # 37
                      self.ui.central.tabs.settings_tab.cal_group.slot_12_y.to_plain_text(), # 38
                      self.ui.central.tabs.settings_tab.cal_group.slot_12_z.to_plain_text(), # 39
                      self.ui.central.tabs.settings_tab.z_cal_group.z_cal_x.to_plain_text(), # 40
                      self.ui.central.tabs.settings_tab.z_cal_group.z_cal_y.to_plain_text(), # 41
                      self.ui.central.tabs.settings_tab.z_cal_group.z_cal_z.to_plain_text(), # 42
                      self.ui.central.tabs.a_tab.a_group.new_cart_val.to_plain_text(), # 43
                      self.ui.central.tabs.a_tab.a_group.a_man.to_plain_text(), # 44
                      self.ui.central.tabs.a_tab.a_group.int_prep_a.to_plain_text(), # 45
                      self.ui.central.tabs.a_tab.a_group.wait_prep_a.to_plain_text(), # 46
                      self.ui.central.tabs.a_tab.a_group.prep_a_count.to_plain_text(), # 47
                      self.ui.central.tabs.a_tab.a_group.prep_factor.to_plain_text(), # 48
                      self.ui.central.tabs.a_tab.a_group.glu_factor.to_plain_text(), # 49
                      self.ui.central.tabs.param_group.z_lift.to_plain_text(), # 50
                      self.ui.central.tabs.param_group.margin.to_plain_text(), # 51
                      self.ui.central.tabs.param_group.a_push.to_plain_text() ) # 52
        gap_fr_0 = self.ui.central.tabs.settings_tab.param_group.gap_fr_0.to_plain_text()
        a_sel_tup = ( self.ui.central.a_tab.a_group.new_cart.is_checked(), 
                      self.ui.central.a_tab.a_group.load_proj_a.is_checked(),
                      self.ui.central.a_tab.a_group.set_a_man.is_checked() )
        sep_a_push = self.ui.central.tabs.settings_tab.param_group.sep_a_move.is_checked()
        invalid_tup = validate_selections(slot_list, param_tup, gap_fr_0, a_sel_tup)
        # ERRORS LIST EMPTY
        if invalid_tup(0) == []:
            gcode_tup = generate_gcode(slot_dict, param_tup, gap_fr_0, a_sel_tup, sep_a_push)
            self.ui.central.z_gcode_group.z_gcode_view.set_plain_text(gcode_tup[0])
            self.ui.central.glu_gcode_group.glu_gcode_view.set_plain_text(gcode_tup[1])
        # ERRORS IN LIST
        else:
            self.err_win = ErrorWindow()
            self.err_win.err_display.set_plain_text(f"Errors:\n    {valid_tup[0]}\n\n"
                                                    f"Parameters that are not numbers:\n    {valid_tup[1]}\n\n"
                                                    f"Negative Parameters:\n    {valid_tup[2]}\n\n" )
            self.err_win.show()

        
class ErrorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.set_window_title("QTGlu Errors")
        self.err_display = QTextBrowser("")
        self.setFixed(QSize(500, 600))


# FUNCTIONS
def validate_selections(slot_dict, param_tup, gap_fr_0, a_sel_tup):
    '''Check for obvious invalid entries before generating g-code'''
    errors = {}
    empty_prev = False
    for slot_val in slot_dict.values():
        if (slot_val != "Empty") and empty_prev:
            errors.add( "Skipped slot(s)")
            break
        elif slot_val == "Empty":
            empty_prev = True
    non_float_params, negative_params = {}, {}
    for param in param_tup:
        try:
            float_param = float( param )
            if float_param < 0:
                errors.add( "Negative parameter(s)" )
                negative_params.add(param)
        except:
            errors.add( "Missing or Non-number parameter(s)" )
            non_float_params.add(param)
    if gap_fr_0 not in { "G", "F" }:
        errors.add( "Invalid gap feedrate prefix" )
    if a_sel_tup.count(True) < 1:
        errors.add( "No initial a-coordinate source selected" )
    elif a_sel_tup.count(True) > 1:
        errors.add( "Too many initial a-coordinate sources selected" )
    return ( errors, non_float_params, negative_params )

def prep_seq(param_tup, a_sel_tup):

def gen_odd_slot(slot_num, slot_dict[slot_num], param_tup, gap_fr_0, sep_a_push):

def gen_even_slot(slot_num, slot_dict[slot_num], param_tup, gap_fr_0, sep_a_push):

def generate_gcode(slot_dict, param_tup, gap_fr_0, a_sel_tup, sep_a_push):
    z_gcode = ( "G21\n"
                "G28.2X0Y0Z0A0\n"
               f"G0G53X{param_tup(40)}Y{param_tup(41)}\n"
               f"G0G53Z{param_tup(42)}\n" )
    glu_gcode = "G21\n"
    glu_gcode += prep_seq(param_tup, a_sel_tup)
    for slot_num in range(1,13):
        if slot_dict[slot_num] != "Empty":
            if slot_num % 2 == 1:
                glu_gcode += gen_odd_slot(slot_num, slot_dict[slot_num], param_tup, gap_fr_0, sep_a_push)
            else:
                glu_gcode += gen_even_slot(slot_num, slot_dict[slot_num], param_tup, gap_fr_0, sep_a_push)
    glu_gcode += "G28.2 A0 Z0\nG28.2 X0 Y0\n"
    return (z_gcode, glu_gcode)

# MAIN PROGRAM
app = QtWidgets.QApplication(sys.argv)
ui = MainUI()
app.exec()



sys.exit(app.exec())
