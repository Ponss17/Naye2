# Documentación técnica: Valorant

Esta API expone dos endpoints de Valorant apoyándose en HenrikDev y en utilidades comunes de caché y sesión HTTP.

## Endpoints

- `/valorant/rango`
  - Fuente: `GET https://api.henrikdev.xyz/valorant/v2/mmr/{REGION}/{NOMBRE}/{TAG}?api_key=...`
  - Devuelve rango actual (traducido a ES), puntos y delta de MMR respecto a la última partida.
  - Incluye el último agente jugado consultando el endpoint de partidas.

- `/valorant/ultima-ranked`
  - Fuente: `GET https://api.henrikdev.xyz/valorant/v3/matches/{REGION}/{NOMBRE}/{TAG}?api_key=...`
  - Devuelve mapa, agente, KDA (kills/deaths/assists), si ganó/perdió y el delta de MMR de la última partida.

## Configuración

Editar `valorant/config.py`:

```python
NOMBRE = "Ponssloveless"
TAG    = "8882"
REGION = "na"  # na, eu, kr, latam, ap
API_KEY = os.environ.get("API_KEY", "")
```

• Requiere `API_KEY` de HenrikDev en entorno.

## Caché y sesión HTTP

- Caché TTL: `common.cache.SimpleTTLCache` con TTL configurable vía `VALORANT_CACHE_TTL` (por defecto 15 segundos).
- Sesión HTTP: `common.http.get_session()` añade reintentos con backoff y `keep-alive`.
- Claves de caché:
  - `rango:{REGION}:{NOMBRE}:{TAG}`
  - `ultima:{REGION}:{NOMBRE}:{TAG}`

## Manejo de errores

- Errores de red y HTTP se capturan y devuelven como `502` con mensajes legibles.
- Errores inesperados devuelven `500` con un texto sencillo.

## Personalización y notas

- Traducciones de rango: `valorant/rangos_es.py`.
- Mensajes se formatean en español y se pueden ajustar en `valorant/endpoints.py`.
- Si cambias jugador/region, no necesitas modificar código de endpoints; sólo `valorant/config.py`.