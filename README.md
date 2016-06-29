# YellowSpider

Extrae y almacena datos de la sección amarilla

### Instalación
```sh
git clone https://github.com/diegordzr/YellowSpider.git
cd YellowSpider
pip install -r requirements.txt
```
### Configuración

Por defecto el único pipeline almacena los datos en MongoDB
```python
ITEM_PIPELINES = ['yellow.pipelines.YellowPipeline']
```
parámetros de la base de datos
```python
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "test"
MONGODB_COLLECTION = "contacts"
```
### Uso
Obtener información de contactos en la categoria software:
```sh
scrapy crawl contacts -a category software
```
