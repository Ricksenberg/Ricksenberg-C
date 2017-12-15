#!/usr/bin/env python
# -*- coding: utf-8 -*-
import webbrowser
# Abrir una nueva pestaña en el navegador por defecto
webbrowser.open_new_tab("http://www.recursospython.com/")
# Abrir una nueva ventana en Chrome
try:
    webbrowser.get("chrome").open_new("http://www.recursospython.com/")
except webbrowser.Error:
    print "No se ha encontrado Chrome."