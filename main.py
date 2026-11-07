import os

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from dados import carregar, salvar
from logica import restantes, lucro_real, total_recebido, vender_um

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

        self.lbl_msg = Label(size_hint_y=None, height=30)
        raiz.add_widget(self.lbl_msg)

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

        for i, p in enumerate(produtos):
            if p["tipo"] == "comida":
                tipo = "Comida"
            else:
                tipo = "Pronto"
            texto = (
                f"{p['nome']} ({tipo})\n"
                f"Restam {restantes(p)} | Lucro real: R$ {lucro_real(p):.2f}"
            )

            linha = BoxLayout(size_hint_y=None, height=70, spacing=5)
            info = Label(text=texto)
            botao = Button(text='Vendeu 1', size_hint_x=0.35)
            botao.indice = i
            botao.bind(on_press=self.clicou_vender)

            linha.add_widget(info)
            linha.add_widget(botao)
            self.lista.add_widget(linha)


    def clicou_vender(self, botao):
        produto = self.dados["produtos"][botao.indice]
        self.lbl_msg.text = vender_um(produto)
        salvar(self.dados, CAMINHO)
        self.atualizar()

if __name__ == "__main__":
    ControleApp().run()    