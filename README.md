# POKEMON API
## _Aprende más del mundo Pokemon_

![](https://th.bing.com/th/id/OIP.i1yxhWJGoP3lvMuha37_9AHaHk?rs=1&pid=ImgDetMain)

Los Pokémon son una clase de criaturas inspiradas en animales reales, insectos, objetos, plantas o criaturas mitológicas. Cada uno de ellos tiene uno o varios tipos (fuego, agua, hielo, entre otros) y según su tipo son capaces de realizar diferentes habilidades.

![Diagrama](https://github.com/cristianmontoyao/pokemonapi/blob/main/Diagrama.png)

Api escrita en Python, utilizando FastAPI y otras librerías de apoyo

## END POINTS 

- Obtener el tipo de Pokemón según su nombre
- Obtener un Pokemon al azar de un tipo epecífico.
- Obtener un Pokemón con el nombre más largo de cierto tipo
- Obtener un Pokemón al azar que contenga en su nombre alguna de las letras "i", "a" o "m", de acuerdo al clima actual de una ciudad dada en coordenadas (latitud y longitud), basado en la siguiente tabla de equivalencia:

| Temperatura | Tipo más fuerte |
| ------ | ------ |
| >= 30°C | Fuego|
| >= 20°C y < 30°C | Tierra |
| >= 10°C y < 20°C | Normal |
| >= 0°C y < 10°C | Agua |
| < 0°C | Hielo |

## Controles de seguridad por diseño

 ### Segmentación/Infraestructura
 - Aislar a nivel de conectividad los servicios de autenticación, de los de la API
 - Exponer las API por medio de API management/API gateway
 - Aplicar reglas de consumo según cliente
 - Generar trazabilidad de los consumos realizados
 - Contar con bases de datos independientes para IAM y para negocio
 ### Autenticación
- Identificar a los consumidores
- Segmentar los recursos que pueden consumir
- No almacenar contraseñas
- No exponer información sensible
- No divulgar detalles en autenticaciones fallidas
 ### Cifrado
- Cifrar las comunicaciones en tránsito con protocolos equivalentes o superiores a TLS1.2
- Utilizar certificados digitales firmados por CA externa
- Cifrar la información sensible en reposo
- Utilizar algoritmos criptográficos avalados por la industria como seguros
 ### Desarrollo
- Validar los campos de entrada
- Utilizar códigos de respuesta genérico
- Implementar mecanismo externo para el almacenamiento de parámetros
- Implementar mecanismo externo para el almacenamiento de secretos
- Agrupar recursos de las API
- Utilizar versiones



## SUPUESTOS
- Dado el entorno de despliegue, se utilizan variables de entorno para el almacenamiento de claves y constantes
- Al ser la información Pokemon de dominio público, no es necesario aplicar cifrado de de información en reposo; sin embargo, en implementaciones de nube es buena práctica.
- Las habilidades pokemón puedrían varian con el entrenamiento; sin embargo es considerada estática, por lo cual se realiza carga inicial de toda la información, monitoreando que la base de datos interna contenga la misma.

## IMPLEMENTACIÓN
- Se utiliza esquema de microservicios, dado que permiten ajuste según las necesidades sin afectar a los consumidores.
- Se dividen las responsabilidades en 4 tipos: 
  - Orquestador: Receptor de solicitudes y lógica principal de la API.
  - Embajador pokemon: Conexión con API externa para la consulta de información Pokemón.
  - Embajador clima: Conexión con API de clima externa, para la consulta de clima en tiempo real.
  - IAM: Responsable de la autenticación y autorización de los consumidores.
- Se propone esquema de despliegue en contenedores, permitiendo ajustar la capacidad de acuerdo con la demanda.

## IAM
- Es necesario que los consumidores se registren antes de poder hacer uso de la API.
- En el registro el consumidor define el usuario y contraseña a utilizar, además proporciona el correo electrónico para actividades de recuperación de clave (no implementado).
- La contraseña no es almacenada en base de datos, por lo cual se utiliza algoritmo criptográfico Argon2 para almacenar su hash.  Dadas las características del algoritmo, se puede almacenar el hash en vez de la contraseña.
- La contraseña parametrizada por los consumidores debe ser compleja y contar con carcaterísticas como longitud superior 14 caracteres, estar conformada por letras mayúsculas y minúsculas, símbolos y números (no implementado).
- Dado el tipo de información en la API, la contraseña puede vencer en tiempos superiores a 30 días (no implementado).
- La base de datos del IAM es independiente a la de las APIs de negocio.
- Se implementa trazabilidad en el registro y autenticación de consumidores.
- El usuario es autenticado en 2 oportunidades:
  - la primera proporcionando el usuario y contraseña definida en el registro. A estos campos se pueden sumar estrategias de múltiple factor de autenticación (no implementado).
  - Si la autenticación es correcta se devuelve al consumidor una cadena en formato JSON web token (JWT), el cual es generado mediante algoritmo HS256.  Se utiliza dicho algoritmo dado que quien genera el token es el mismo que lo valida.
- La llave utilizada para firma debe estar almacenada en recurso externo tipo key management service o key vault; sin embargo dada la implementación se almacena en variables de entorno.
- El token tiene vigencia parametrizable, la cual dependerá de la dinámica de la API.
- No se almacenan datos sensibles en el token devuelto, se utiliza un identificar tipo UUID sin sentido para el consumidor
- El UUID permite enlazar la trazabilidad internamente.
- El consumo de las API Pokemon está sujeto a la autenticación.
- Se genera trazabilidad de uso

## INSTALACIÓN

Clonar repositorio
```sh
git clone https://github.com/cristianmontoyao/pokemonapi.git
```
Acceder a la carpeta descargada
```sh
cd pokemonapi
```

Modificar las variables de entorno en el archivo docker-compose.yaml

```sh
docker-compose.yaml
```

Construir las imágenes
```sh
docker-compose build
```

Desplegar los contenedores
```sh
docker-compose up
```

## CONSUMOS

Puede hacer uso de la documentación proporcionada por FastAPI o probar mediante el uso de Curl adjunto:

### Autenticación:
```sh
http://localhost:8001/docs
```

### PokemonsAPI
```sh
http://localhost:8000/docs
```
##### Registrar usuario
```sh
curl -X 'POST' \
  'http://localhost:8001/auth/v1/registeruser' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "user",
  "password": "paswwword123",
  "mail": "correo@correo.com"
}'
```

##### Autenticar usuario
```sh
curl -X 'POST' \
  'http://localhost:8001/auth/v1/authenticate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "user",
  "password": "paswwword123"
}'
 ```
##### Obtener el tipo de Pokemón según su nombre
```sh
curl -X 'POST' \
  'http://localhost:8000/pokemons/v1/pokemon/gettypebyname' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiIyYWJmMDA1MS01NWY2LTQ2NTMtYjNiNi1mYTI2OTFiMmY4MTMiLCJleHAiOjE3MTU5OTMwMjR9.vKivfZT1o2ar3WyMqDxvqwgZyjTYqYRIDo-hY4pniFs",
  "pokemon_name": "wartortle"
}'
 ```
### Obtener un Pokemon al azar de un tipo epecífico.
```sh
curl -X 'POST' \
  'http://localhost:8000/pokemons/v1/pokemon/getrandombytype' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiIyYWJmMDA1MS01NWY2LTQ2NTMtYjNiNi1mYTI2OTFiMmY4MTMiLCJleHAiOjE3MTU5OTMwMjR9.vKivfZT1o2ar3WyMqDxvqwgZyjTYqYRIDo-hY4pniFs",
  "type_name": "water"
}'
```
### Obtener un Pokemón con el nombre más largo de cierto tipo
```sh
curl -X 'POST' \
  'http://localhost:8000/pokemons/v1/pokemon/getnamebytype' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiIyYWJmMDA1MS01NWY2LTQ2NTMtYjNiNi1mYTI2OTFiMmY4MTMiLCJleHAiOjE3MTU5OTMwMjR9.vKivfZT1o2ar3WyMqDxvqwgZyjTYqYRIDo-hY4pniFs",
  "type_name": "water"
}'
```
### Obtener un Pokemón al azar que contenga en su nombre alguna de las letras "i", "a" o "m", de acuerdo al clima actual de una ciudad dada en coordenadas (latitud y longitud)
```sh
curl -X 'POST' \
  'http://localhost:8000/pokemons/v1/pokemon/getrandombycityweather' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiIyYWJmMDA1MS01NWY2LTQ2NTMtYjNiNi1mYTI2OTFiMmY4MTMiLCJleHAiOjE3MTU5OTMwMjR9.vKivfZT1o2ar3WyMqDxvqwgZyjTYqYRIDo-hY4pniFs",
"latitude":4.5055,
"longitude": -45.23
}'
```