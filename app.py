import streamlit as st

CERO_ABSOLUTO_C = -273.15

st.set_page_config(page_title="Conversor de temperatura", page_icon="🌡️")


def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte grados Celsius a grados Fahrenheit, redondeado a 2 decimales."""
    return round(celsius * 9 / 5 + 32, 2)


st.title("Conversor de temperatura")

celsius = st.number_input(
    "Grados Celsius (°C)",
    min_value=CERO_ABSOLUTO_C,
    value=0.0,
    step=0.5,
    format="%.2f",
)

fahrenheit = celsius_a_fahrenheit(celsius)

st.metric(label=f"{celsius:.2f} °C equivalen a", value=f"{fahrenheit:.2f} °F")
st.caption("Fórmula: °F = °C × 9/5 + 32")

