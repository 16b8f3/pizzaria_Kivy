from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class Gerenciador_das_telas(ScreenManager):
    pass


class Menu(Screen):
    pass


class Pedido(Screen):
    def on_checkbox_Active(self, checkboxInstance, isActive):
        if isActive:
            self.ids.preco_total.text = "47.99"
        else:
            self.ids.preco_total.text = "0.00"

class Finalizar_pedido(Screen):
    def spinner_Clicado(self, value):
        self.ids.lbl_forma_de_pagamento.text = value


class pizzaria(App):
    def build(self):
        return Gerenciador_das_telas()


if __name__ == '__main__':
    pizzaria().run()

