import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txt_result.clean()
        self._view.update_page()
        anno = self._view._txtAnno.value
        try:
            intAnno = int(anno)
        except ValueError:
            self._view.create_alert("Anno inserito non valido")
        self._model.getGrafo(intAnno)
        #print(self._model.getNumNodes())
        dizRisultato, compConnesse = self._model.getConnessa()
        dizOrdinato = sorted(dizRisultato.items())
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {compConnesse} componenti connesse"))
        for i in dizOrdinato:
            self._view._txt_result.controls.append(ft.Text(f"{i[0]} -- {i[1]}"))
        self._view.update_page()

    def handleStatiRaggiungibili(self,e):
        stato = self._view._dropStato.value
        self._view._txt_result.clean()
        self._view.update_page()
        anno = self._view._txtAnno.value
        try:
            intAnno = int(anno)
        except ValueError:
            self._view.create_alert("Anno inserito non valido")
        self._model.getGrafo(intAnno)
        lista_raggiungibili = self._model.getCompConnessa(stato)
        self._view._txt_result.controls.append(ft.Text(f"Lo stato {stato} pùo raggiungere i seguenti stati:"))
        lista_raggiungibili.sort()
        for i in lista_raggiungibili:
            self._view._txt_result.controls.append(ft.Text(f"{i}"))
        self._view.update_page()


