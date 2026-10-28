import streamlit as st

CERO_ABSOLUTO_C = -273.15

st.set_page_config(page_title="Conversor de temperatura", page_icon="🌡️")


def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte grados Celsius a grados Fahrenheit, redondeado a 2 decimales."""
    return round(celsius * 9 / 5 + 32, 2)


def celsius_a_kelvin(celsius: float) -> float:
    """Convierte grados Celsius a Kelvin, redondeado a 2 decimales."""
    return round(celsius + 273.15, 2)


st.title("Conversor de temperatura")

celsius = st.number_input(
    "Grados Celsius (°C)",
    min_value=CERO_ABSOLUTO_C,
    value=0.0,
    step=0.5,
    format="%.2f",
)

fahrenheit = celsius_a_fahrenheit(celsius)
kelvin = celsius_a_kelvin(celsius)

col1, col2 = st.columns(2)
col1.metric(label=f"{celsius:.2f} °C equivalen a", value=f"{fahrenheit:.2f} °F")
col2.metric(label=f"{celsius:.2f} °C equivalen a", value=f"{kelvin:.2f} K")
st.caption("Fórmulas: °F = °C × 9/5 + 32  |  K = °C + 273.15")

