from controllers.menu import iniciar_menu_principal
from datetime import datetime


if __name__ == " main ":
    print(f"\n{datetime.now().strftime('%d/%m/%y, %H:%M:%S')}\n")
    iniciar_menu_principal()