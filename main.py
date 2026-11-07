import os

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from dados import carregar
from logica import restantes, lucro_real, total_recebido

Window.size = (400,700) #tamanho da janela

PASTA = os.path.dirname(os.path.abspath(__file__))
CAMINHO = os.path.join(PASTA, "produtos.json")

class ControleApp(App):

    def build(self):
        self.dados = carregar(CAMINHO)

        raiz = BoxLayout(orientation="vertical", padding=10, spacing=10)

        titulo = Label(
            text="Controle de vendas",
            font_size=24,
            size_hint_y=None,
            height=60,
        )
        raiz.add_widget(titulo)

        self.lbl_totais = Label(size_hint_y=None, height=100, font_size=18)
        raiz.add_widget(self.lbl_totais)

        self.lista = GridLayout(cols=1, spacing=8, size_hint_y=None)
        self.lista.bind(minimum_height=self.lista.setter("height"))
        rolagem = ScrollView()
        rolagem.add_widget(self.lista)
        raiz.add_widget(rolagem)


        self.atualizar()
        return raiz


    def atualizar(self):
        produtos = self.dados["produtos"]

        recebido = 0
        lucro = 0
        for p in produtos:
            recebido = recebido + total_recebido(p)
            lucro = lucro + lucro_real(p)


        self.lbl_totais.text = (
            f"Ja recebido: R$ {recebido:.2f}\n"
            f"Lucro real: R$ {lucro:.2f}"
        )


        self.lista.clear_widgets()

        if not produtos:
            self.lista.add_widget(
                Label(text="Nenhum produto ainda.", size_hint_y=None, height=70)
            )

        for p in produtos:
            if p["tipo"] == "comida":
                tipo = "comida"
            else:
                tipo = "pronto"
            texto = (
                f"{p['nome']} ({tipo})\n"
                f"Restam {restantes(p)} | Lucro real: R$ {lucro_real(p):.2f}"
            )
            self.lista.add_widget(
                Label(text=texto, size_hint_y=None, height=70)
            )

if __name__ == "__main__":
    ControleApp().run()
