# La Perla del Born — Eventos Corporativos

Web de presentación de eventos privados para La Perla del Born, Barcelona.

## Publicar en GitHub Pages

1. Sube todos los archivos a `poemasl/eventos-corporativos` en GitHub
2. Ve a **Settings → Pages**
3. En *Source* selecciona `Deploy from a branch`
4. Elige la rama `main` y carpeta `/ (root)`
5. Guarda. En 2-3 minutos la URL `https://poemasl.github.io/eventos-corporativos/` estará activa

## Conectar dominio propio (eventos.laperladelborn.com)

En cdmon, ve a la gestión DNS de `laperladelborn.com` y añade:

| Tipo  | Nombre    | Valor                          |
|-------|-----------|--------------------------------|
| CNAME | eventos   | poemasl.github.io              |

Luego en GitHub Pages → Custom domain: escribe `eventos.laperladelborn.com` y activa HTTPS.

## Estructura

```
eventos-corporativos/
├── index.html          ← Página principal
├── assets/
│   ├── css/style.css   ← Estilos
│   └── js/main.js      ← Textos i18n + interacciones
└── icons/              ← Imágenes y logos
```
