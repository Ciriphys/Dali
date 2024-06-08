defaultFontFamily = None

HelveticaFF = { 'fontname' : 'Helvetica' }

__all__ = ['defaultFontFamily', 'HelveticaFF', 'SetFontFamily']

def SetFontFamily(fontFamily = HelveticaFF):
    defaultFontFamily = fontFamily
