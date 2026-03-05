#  Análisis Visual de Datos de Producción en una Fábrica

**Alumna:** Yulenny Bonilla
**Matricula:** 2023-0769
**Materia:** Inteligencia Artificial
**Práctica:** Primera Práctica General — 15 puntos  

##  Descripción
Análisis visual de datos de producción de una fábrica de componentes electrónicos, utilizando Python, Pandas y Matplotlib para detectar patrones y posibles causas de defectos.

##  Tecnologías usadas
- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- NumPy

##  Estructura del proyecto
practica_produccion/
├── data/produccion.csv      # Dataset de producción
├── graficos/                # Gráficos generados
├── analisis.py              # Código principal
├── requirements.txt         # Dependencias
└── README.md

##  Cómo ejecutar
pip install -r requirements.txt
python analisis.py

##  Gráficos generados
1. Histograma de cantidad producida
2. Histograma de defectos
3. Boxplot de defectos por turno
4. Boxplot de cantidad producida por turno
5. Scatter plot temperatura vs defectos
6. Scatter plot cantidad vs defectos
7. Heatmap de correlaciones