#
# Canopy product code
#
# (C) Copyright 2016 Enthought, Inc., Austin, TX
# All right reserved.
#
# This file is confidential and NOT open source.  Do not distribute.
#
import unittest

from pyface.api import OK
from pyface.qt.QtCore import Qt, QEvent
from pyface.qt.QtGui import QDialog, QKeyEvent
from pyface.ui.qt4.util.gui_test_assistant import GuiTestAssistant
from pyface.ui.qt4.util.modal_dialog_tester import ModalDialogTester

from calculatorQt import Application


class TestOkDefaultDialog(unittest.TestCase, GuiTestAssistant):
    """ Test the OkDefaultDialog widget.

    """
    def setUp(self):
        GuiTestAssistant.setUp(self)
        self.dialog = Application()

    def tearDown(self):
        del self.dialog
        GuiTestAssistant.tearDown(self)

    def test_ok_default(self):
        tester = ModalDialogTester(self.dialog.main)

        def press_enter(t):
            dialog = t.click_button(9)
            #enter_press = QKeyEvent(QEvent.KeyRelease, Qt.Key_Enter,
            #                        Qt.NoModifier)
            #dialog.keyPressEvent(enter_press)

            #enter_release = QKeyEvent(QEvent.KeyRelease, Qt.Key_Enter,
            #                          Qt.NoModifier)
            #dialog.keyReleaseEvent(enter_release)

        tester.open_and_run(press_enter)
        self.assertEqual(tester.result, OK)
