from qt.core import Qt, QFontMetrics, QLineEdit

class PathLineEdit(QLineEdit):
    '''
    Read-only line edit for paths that are usually wider than the field. The
    beginning of the path is replaced by an ellipsis so that the end of the
    path - the interesting part - stays readable, and more of it reappears as
    the field gets wider. The full path is shown while the field has focus, so
    that it can be selected and copied, and is always what text() returns.
    '''

    def __init__(self, text: str = "", parent=None):
        QLineEdit.__init__(self, parent)
        self.setReadOnly(True)
        self.full_text = text
        self.setToolTip(text)
        self.update_shown_text()


    def setText(self, text: str):
        self.full_text = text
        self.setToolTip(text)
        if self.hasFocus():
            QLineEdit.setText(self, text)
        else:
            self.update_shown_text()


    def text(self) -> str:
        return self.full_text


    def focusInEvent(self, event):
        QLineEdit.setText(self, self.full_text)
        QLineEdit.focusInEvent(self, event)


    def focusOutEvent(self, event):
        QLineEdit.focusOutEvent(self, event)
        self.update_shown_text()


    def resizeEvent(self, event):
        QLineEdit.resizeEvent(self, event)
        self.update_shown_text()


    def update_shown_text(self):
        if self.hasFocus():
            return
        # Qt keeps a small horizontal margin inside the frame that is not
        # available for text.
        available = max(self.contentsRect().width() - 6, 0)
        elided = QFontMetrics(self.font()).elidedText(self.full_text,
                                                      Qt.TextElideMode.ElideLeft,
                                                      available)
        QLineEdit.setText(self, elided)
