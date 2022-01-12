# TRIGGERS O SIGNAL ACTUALIZAR EL STOK DE UN LIBRO SI SE DEVUELVE
def update_libro_stok(sender, instance, **kwargs):
    instance.libro.stok = instance.libro.stok + 1
    instance.libro.save()