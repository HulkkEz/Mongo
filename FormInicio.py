from ._anvil_designer import FormInicioTemplate
from anvil import *

class FormInicio(FormInicioTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    cp = ColumnPanel(background="#f5f5f5", spacing="large")
    self.add_component(cp)

    titulo = Label(
      text="🎵 Tienda Musical",
      font_size=24,
      bold=True,
      align="center"
    )

    subtitulo = Label(
      text="Sistema CRUD con MongoDB Atlas",
      align="center",
      foreground="#555"
    )

    btn = Button(
      text="Ver productos",
      role="primary",
      width=200
    )
    btn.set_event_handler("click", self.ir_productos)

    cp.add_component(titulo)
    cp.add_component(subtitulo)
    cp.add_component(Spacer(height=20))
    cp.add_component(btn)

  def ir_productos(self, **event_args):
    open_form("FormProductos")
