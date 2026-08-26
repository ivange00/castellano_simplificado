# %%
import streamlit as st

# %%
def translate(text):
    lower_text = text.lower()
    lower_text = lower_text.replace('v', 'b')
    lower_text = lower_text.replace('ch', 'ks')
    lower_text = lower_text.replace('ñ', 'ni')
    lower_text = lower_text.replace('nii', 'ni')
    lower_text = lower_text.replace('qu', 'k')
    lower_text = lower_text.replace('q', 'k')
    lower_text = lower_text.replace('w', 'u')
    lower_text = lower_text.replace('x', 'ks')
    lower_text = lower_text.replace('y', 'i')
    lower_text = lower_text.replace('ll', 'i')
    lower_text = lower_text.replace('ge', 'je')
    lower_text = lower_text.replace('gi', 'ji')
    lower_text = lower_text.replace('gue', 'ge')
    lower_text = lower_text.replace('gui', 'gi')
    lower_text = lower_text.replace('gü', 'gu')
    lower_text = lower_text.replace('h', '')
    lower_text = lower_text.replace('ce', 'ze')
    lower_text = lower_text.replace('ci', 'zi')
    lower_text = lower_text.replace('c', 'k')
    translated_text = lower_text
    return translated_text

# %%
st.title("Castellano simplificado")

with st.form("translator"):
    text = st.text_input("Texto a traducir:")
    submitted = st.form_submit_button("Traducir")

if submitted:
    st.subheader("Resultado")
    st.write(translate(text))
