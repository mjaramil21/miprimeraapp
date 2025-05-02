import streamlit as st
from PIL import Image

st.title("Hola Mundo!!")

st.header("Wow guys puse texto en una página web")
st. write("ahora que")
image = Image.open('IMG_1936.jpg')

st.image(image, caption='miren a mi gata')


texto = st.text_input('bueno pero', 'y se sabe el chiste del bus')
st.write('pero', texto)

st.subheader("dos fokin columnas wow")

col1, col2 = st.columns(2)

with col1:
  st.subheader("primera fokin columna")
  st.write("vea esooooo")
  resp = st.checkbox('sioque')
  if resp: 
    st.write("SIZAAAA")

with col2:
  st.subheader("segunda fokin columna")
  modo = st.radio("aún más cool que antes", ('opción 1', 'opción 2', 'opción 3'))
  if modo == 'opción 1':
    st.write('oprimiste la opción 1 mera loca')
  if modo == 'opción 2':
    st.write('oprimiste la opción 2 mera loca')
  if modo == 'opción 3':
    st.write('oprimiste la opción 3 mera loca')

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
