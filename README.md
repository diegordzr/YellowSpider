# YellowSpider

Extrae y almacena datos de la sección amarilla

### Instalación
```sh
git clone https://github.com/diegordzr/YellowSpider.git
cd YellowSpider
pip install -r requirements.txt
```
### Configuración

configure el piplenine para configurar el destino de los datos
Para almacenar los datos en MongoDB use el sig pipline
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
