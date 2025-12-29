# Información de Envío del Challenge

## ✅ Checklist Pre-Envío

Antes de enviar tu solución, verifica que:

- [x] **6 archivos Python** implementados en `src/`:
  - [x] `q1_time.py`
  - [x] `q1_memory.py`
  - [x] `q2_time.py`
  - [x] `q2_memory.py`
  - [x] `q3_time.py`
  - [x] `q3_memory.py`

- [x] **Jupyter Notebook** completo con:
  - [x] Explicación de soluciones
  - [x] Ejecución de todas las funciones
  - [x] Mediciones de tiempo
  - [x] Profiling de memoria
  - [x] Comparaciones de resultados
  - [x] Análisis de mejoras

- [x] **requirements.txt** actualizado con todas las dependencias

- [x] **README.md** con instrucciones

- [x] **Documentación** clara de supuestos y decisiones

## 📤 Proceso de Envío

### 1. Preparar Repositorio Git

```bash
cd challenge_data_ops_eng

# Inicializar git (si no está inicializado)
git init

# Crear rama develop
git checkout -b develop

# Agregar archivos (NO incluir el archivo JSON de datos)
git add .
git add src/*.py
git add src/challenge.ipynb
git add requirements.txt
git add *.md

# Verificar que NO se incluya el archivo de datos
git status

# Si el archivo JSON aparece, agregarlo al .gitignore
echo "farmers-protest-tweets-2021-2-4.json" >> .gitignore
git add .gitignore

# Commit
git commit -m "feat: Implement complete data engineering challenge solution

- Q1: Top 10 dates with most tweets (time & memory optimized)
- Q2: Top 10 most used emojis (time & memory optimized)
- Q3: Top 10 most mentioned users (time & memory optimized)
- Complete Jupyter notebook with analysis and profiling
- Comprehensive documentation

🤖 Generated with Claude Code (https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

# Merge a main
git checkout -b main
git merge develop

# Verificar el estado final
git log --oneline
```

### 2. Subir a GitHub

```bash
# Crear repositorio en GitHub
# Luego conectar y subir

git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
git push -u origin main
git push origin develop
```

### 3. Enviar Solución

Hacer POST request a la API con tus datos:

```bash
curl -X POST https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/data-engineer \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Tu Nombre Completo",
    "mail": "tu.email@example.com",
    "github_url": "https://github.com/tu_usuario/tu_repo.git"
  }'
```

O usando Python:

```python
import requests

data = {
    "name": "Tu Nombre Completo",
    "mail": "tu.email@example.com",
    "github_url": "https://github.com/tu_usuario/tu_repo.git"
}

response = requests.post(
    "https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/data-engineer",
    json=data
)

print(response.status_code)
print(response.text)
```

## 📋 Contenido del Repositorio

Tu repositorio debe tener esta estructura:

```
tu-repo/
├── .gitignore                    # Ignorar archivos grandes
├── README.md                     # Instrucciones originales del challenge
├── EXECUTION_GUIDE.md            # Guía de ejecución
├── SOLUTION_SUMMARY.md           # Resumen de la solución
├── requirements.txt              # Dependencias
└── src/
    ├── q1_time.py               # Implementaciones
    ├── q1_memory.py
    ├── q2_time.py
    ├── q2_memory.py
    ├── q3_time.py
    ├── q3_memory.py
    ├── challenge.ipynb          # Análisis completo
    └── test_functions.py        # Script de verificación
```

## ⚠️ Notas Importantes

### NO Incluir en el Repositorio
- ❌ El archivo JSON de datos (es muy grande, 389MB)
- ❌ Carpetas `__pycache__/`
- ❌ `.ipynb_checkpoints/`
- ❌ Archivos `.pyc`
- ❌ Entornos virtuales (`venv/`, `env/`)

### Incluir .gitignore

Crear archivo `.gitignore`:

```gitignore
# Data files
*.json
farmers-protest-tweets-2021-2-4.json

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Jupyter
.ipynb_checkpoints
*.ipynb_checkpoints/

# Environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
```

## 🎯 Puntos Clave para Evaluación

Según el README del challenge, serán evaluados:

1. **Orden y Claridad**: Código bien organizado y explicativo
2. **Modularidad**: Funciones separadas en archivos individuales
3. **Eficiencia**: Optimizaciones de tiempo y memoria
4. **Creatividad**: Soluciones innovadoras
5. **Documentación**: Supuestos, explicaciones, mejoras
6. **Git**: Uso correcto de branches, commits, pull requests
7. **Manejo de Errores**: Casos borde considerados

## ✅ Validación Final

Antes de enviar, ejecuta:

```bash
cd src
python test_functions.py
```

Esto verificará que:
- Todas las funciones se importen correctamente
- Retornen el formato correcto
- Las versiones time y memory den resultados idénticos
- No haya errores de ejecución

## 📞 Dudas

Si tienes dudas sobre el challenge, revisa:
- El README.md original
- La documentación de Twitter API v1
- Los archivos de documentación incluidos

## 🚀 ¡Buena Suerte!

Has completado una solución sólida y bien documentada. Asegúrate de revisar todo antes de enviar.
