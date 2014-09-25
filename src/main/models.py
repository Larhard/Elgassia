from django.db import models
import model_generics


class MainMenu(model_generics.MenuGeneric):
    pass


class PopupMenu(model_generics.MenuGeneric):
    pass


class StandardPage(model_generics.PageGeneric):
    pass