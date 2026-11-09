from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

        self._lista_biblioteche = []
        self._lista_generi = []
        self._lista_libri = []

        self.get_biblioteche()
        self.get_generi()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        if len(self._lista_libri) == 0:
            self._lista_libri = self._libro_dao.read_libri()
        else:
            pass
        result_genere = set()
        result_biblioteca = set()
        for b in self._lista_biblioteche:
            if b.nome == biblioteca:
                get_id = b.id
        for libro in self._lista_libri:
            if genere == "Nessun filtro" and biblioteca == "Nessun filtro":
                return self._lista_libri

            if genere != "Nessun filtro" and libro.genere == genere:
                result_genere.add(f"{libro.id} | {libro.titolo} | Autore: {libro.autore} | Genere: {libro.genere} | Anno: {libro.anno_pubblicazione}")
            if biblioteca != "Nessun filtro" and libro.id_biblioteca == get_id:
                    result_biblioteca.add(f"{libro.id} | {libro.titolo} | Autore: {libro.autore} | Genere: {libro.genere} | Anno: {libro.anno_pubblicazione}")
        if biblioteca == "Nessun filtro":
            if genere != "Nessun filtro":
                return list(result_genere)
        elif genere == "Nessun filtro":
            return list(result_biblioteca)
        result_intersect = list(result_genere & result_biblioteca)
        return result_intersect

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        if len(self._lista_generi) == 0:
            self._lista_generi = self._libro_dao.read_generi()
        else:
            pass
        return self._lista_generi

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        if len(self._lista_biblioteche) == 0:
            self._lista_biblioteche = self._biblioteca_dao.read_biblioteche()
        else:
            pass
        return self._lista_biblioteche
