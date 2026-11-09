import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_biblioteca(self):
        for b in self._model._lista_biblioteche:
            self._view.dd_biblioteche.options.append(ft.dropdown.Option(b.nome))

    def popola_genere(self):
        for g in self._model._lista_generi:
            self._view.dd_generi.options.append(ft.dropdown.Option(g))

    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self, e):
        biblioteca = self._view.dd_biblioteche.value
        genere = self._view.dd_generi.value
        if biblioteca is None or genere is None:
            print('Errore')
            return
        result = self._model.get_libri_filtrati(biblioteca, genere)
        self._view.lista_libri_selezionati.controls.clear()
        for libro in result:
            self._view.lista_libri_selezionati.controls.append(ft.Text(f"{libro}"))
        self._view.update()