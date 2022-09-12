# QTGlu.py
    ---
## Layout

1. Modules
    01. math
    02. sys
    03. os
    04. from PySide6.QtWidgets ...
    05. from PySide6 ...
    06. from PySide6.QtUiTools ...
    07. from __feature__ ...

2. Global Variables
    01. loader = QUILoader()
    02. basedir = os.path.dirname(__file__)

3. Classes
    01. MainUI(QTCore.QObject)
        001. __init__(self)
        002. gen_released(self)
            * slot_dict
            * param_tup
            * gap_fr_0
            * a_sel_tup
            * sep_a_push
            * invalid_tup = validate_selections(...)
            * if invalid_tup(0) == []
                * gcode_tup = generate_gcode(...)
            * else
                * ErrorWindow
    02. ErrorWindow(QWidget)



