import streamlit as st
from PIL import Image

st.title("¡Bienvenidxs a mi primera app!")

st.header("Mi Hola Mundo de Streamlit")
st. write("vamos a ver que mas podemos hacer...")
image = Image.open('IMAGEN APP.jpg')

st.image(image, caption='Se me abrió el tercer ojo haciendo esto')


texto = st.text_input('Hagamos este espacio productivo', 'Cuéntame 3 cosas que te hagan muy feliz')
st.write('las 3 cosas que me hacen feliz son:', texto)

st.subheader("¡Ya tenemos 2 columnas!")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Pregunta:")
  st.write("¿Si tuvieras que escoger entre no tener que dormir o comer nunca más en tu vida (no lo necesitas) ¿Qué escogerías?")
  resp = st.checkbox('Comer')
  resp_2 = st.checkbox('Dormir')
  if resp: 
    st.write("¿Estás bien?")
  if resp_2: 
    st.write("Eres un diseñador ó programador que necesita más tiempo para sus proyectos ¿cierto?")

with col2:
  st.subheader("¡Ahora otra pregunta!")
  modo = st.radio("Si tuvieras un último deseo a un genio de la lámpara ¿Qué le pedirías?", ('Paz Mundial', 'Dinero Ilimitado', 'Liberar al Genio'))
  if modo == 'Paz Mundial':
    st.write('Que respuesta tan de reina de belleza de tu parte')
  if modo == 'Dinero Ilimitado':
    st.write('Pudiste haber sido más creativo')
  if modo == 'Liberar al Genio':
    st.write('¡Esa es la única respuesta correcta!')

st.subheader("Oprime el botón para ser perfecto")
if st.button("Perfección a un botón de distancia"):
  st.write("Si no cambió nada es por que ya eres perfecto tal y como eres :) ")
else:
  st.write("¿Lo vas a presionar?")

st.subheader("Bueno ya no seamos tan filosóficos e inspiradores")
in_mod = st.selectbox(
  "Dime tu color favorito", 
  ("Rojo", "azul", "negro"),
)
if in_mod == "Rojo":
  set_mod = "También es mi color favorito"
elif in_mod == "azul":
  set_mod = "azul como el mar azul"
elif in_mod == "negro":
  set_mod = "eso es un poquito emo de tu parte pero esta bien"
st.write("Lo que pienso de tu elección:", set_mod)
