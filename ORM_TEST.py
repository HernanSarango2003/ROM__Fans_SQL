import datetime
from library import models
from library.models import Libro, Autor, Editorial
from django.db.models import Min, Max, Avg, Count, Sum
from django.db.models.functions import Left
from django.db.models import F, Q
from library.models import Editorial, Libro, Autor, AutorCapitulo  # Ajusta el nombre de tu aplicación en 'myapp'

# 1. Crear la editorial
editorial = Editorial.objects.create(nombre='Editorial 2')

# 2. Crear el libro "El Diablo"
libro = Libro.objects.create(
    isbn='7234567890123',
    titulo='El Diablo',
    paginas=98,
    fecha_publicacion='2021-01-01',
    imagen='http://imagen.com',
    desc_corta='Un clásico',
    estatus='A',
    categoria='suspenso',
    editorial=editorial
)

# 3. Crear 6 autores con bulk_create
autores = Autor.objects.bulk_create([
    Autor(nombre="Autor 17"),
    Autor(nombre="Autor 18"),
    Autor(nombre="Autor 19"),
    Autor(nombre="Autor 20"),
    Autor(nombre="Autor 21"),
    Autor(nombre="Autor 22")
])

# 4. Crear las relaciones en AutorCapitulo para asociar cada autor con el libro "El Diablo"
AutorCapitulo.objects.bulk_create([
    AutorCapitulo(autor=autor, libro=libro, capitulo=f"Capítulo {i+1}")
    for i, autor in enumerate(autores)
])


# 2. Encuentra todos los autores con nombres que contengan la letra "o" y que hayan escrito un libro en la categoría "Referencia"
autores_con_o = Autor.objects.filter(nombre__icontains="o", libros__categoria="Referencia")

# 3. Busca libros publicados entre los años 2020 y 2024, con más de 250 páginas y una categoría diferente de "Referencia"
libros_recientes = Libro.objects.filter(
    fecha_publicacion__year__range=(2020, 2024),
    paginas__gt=250
).exclude(categoria="Referencia")

# 4. Dado el libro “La Biblia”, muestra todos sus autores
libro_biblia = Libro.objects.get(titulo="La Biblia")
autores_biblia = libro_biblia.autores.all()

# 5. Incrementa el número de páginas en 50 para todos los libros que tengan más de 100 páginas y cuyo autor sea “Antoni”
Libro.objects.filter(
    paginas__gt=100,
    autores__nombre__icontains="Antoni"
).update(paginas=models.F('paginas') + 50)
