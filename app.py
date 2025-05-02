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

st.subheader("así se usa un botón")
if st.button("oprima o miedo"):
  st.write("YAYYYY")
else:
  st.write("MERA LOCAAAAAAAAAAAA")

st.subheader("papapapapapap")
in_mod = st.selectbox(
  "pero eliga una", 
  ("princesa número uno", "princesa número dos", "princesa número tres"),
)
if in_mod == "princesa número uno":
  set_mod = "aplaudale aaa cenicientaaaaa"
elif in_mod == "princesa número dos":
  set_mod = "vamos denle un aplauso aaaa blancaaaanieveeeeees"
elif in_mod == "princesa número tres":
  set_mod = "será suya para rescatar la princesa fiooooonaaaaaa"
st.write("lord farquaad,", set_mod)
