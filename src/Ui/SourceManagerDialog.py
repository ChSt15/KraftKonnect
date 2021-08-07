from dataclasses import asdict, astuple
from sqlite3 import IntegrityError
from typing import Any

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QListWidget, QTableWidget, QPushButton, QLabel, \
    QSplitter, QDialogButtonBox
from PyQt5.QtCore import Qt, QModelIndex, QObject, QVariant

from src.DataManagement.DTO.Source import Source
from src.DataManagement.IO.DataIO import DataIO
from src.DataManagement.IO.SourceIO import SourceIO


class SourceManagerDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Source Manager')
        self.source_io = SourceIO()
        self.data_io = DataIO()
        self.set_up_ui()
        self.model = None
        self.selected_source = None
        self.set_up_source_table_view()

    def apply(self) -> None:
        name = self.name_input.text()
        description = self.description_text.toPlainText()
        code = self.code_path.text()
        source = Source(self.selected_source.id, name, description, code)
        try:
            self.source_io.update(source)
            self.reload_sources()
            self.clean_widgets()
        except IntegrityError:
            # TODO Name not unique
            print('TODO Add warning here!')

    def clean_widgets(self):
        self.name_input.setText("")
        self.description_text.setText("")
        self.code_path.setText("")

    def discard(self) -> None:
        self.close()

    def ok(self) -> None:
        self.apply()
        self.close()

    def delete(self) -> None:
        if self.selected_source is not None:
            id = self.selected_source.id
            self.source_io.delete(id)
            self.data_io.delete_all(id)
            self.selected_source = None
            self.reload_sources()

    def reload_sources(self):
        self.delete_btn.setEnabled(False)
        self.set_up_source_table_view()

    def set_up_ui(self):
        uic.loadUi('res/layout/source_manager_dialog.Ui', self)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.ok)
        self.buttonBox.button(QDialogButtonBox.Discard).clicked.connect(self.discard)
        self.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.apply)

    def set_up_source_table_view(self):
        self.model = SourceManagerDialog.TableModel([source for source in self.source_io.get_all()])
        self.source_table_view.setModel(self.model)
        self.source_table_view.clicked.connect(self.edit_source)

    def edit_source(self, index: QModelIndex) -> None:
        row = index.row()
        self.selected_source = self.model.get_data_by_row(row)
        self.name_input.setText(self.selected_source.name)
        self.description_text.setText(self.selected_source.description)
        self.code_path.setText(self.selected_source.script)
        self.delete_btn.setEnabled(True)
        self.delete_btn.clicked.connect(self.delete)

    class TableModel(QtCore.QAbstractTableModel):
        def __init__(self, data):
            super(SourceManagerDialog.TableModel, self).__init__()
            self.data_list = data

        def rowCount(self, parent: QModelIndex = ...) -> int:
            return len(self.data_list)

        def columnCount(self, parent: QModelIndex = ...) -> int:
            return len(self.data_list[0].__annotations__)

        def data(self, index: QModelIndex, role: int = ...) -> Any:
            if role == Qt.DisplayRole:
                row = index.row()
                column = index.column()
                source = self.data_list[row]
                data = astuple(source)[column]
                return data
            else: return QVariant()

        def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
            if role == Qt.DisplayRole and orientation == Qt.Horizontal:
                return list(self.data_list[0].__annotations__)[section]

        def get_data_by_row(self, row: int) -> Source:
            return self.data_list[row]
