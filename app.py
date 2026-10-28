import streamlit as st

st.set_page_config(page_title="Conversor de temperatura", page_icon="🌡️")


def celsius_a_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def celsius_a_kelvin(celsius: float) -> float:
    return celsius + 273.15


def fahrenheit_a_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_a_kelvin(fahrenheit: float) -> float:
    return fahrenheit_a_celsius(fahrenheit) + 273.15


def kelvin_a_celsius(kelvin: float) -> float:
    return kelvin - 273.15


def kelvin_a_fahrenheit(kelvin: float) -> float:
    return celsius_a_fahrenheit(kelvin_a_celsius(kelvin))


# nombre en el menú: (unidad origen, unidad destino, función, valor mínimo, fórmula)
CONVERSIONES = {
    "Celsius → Fahrenheit": ("°C", "°F", celsius_a_fahrenheit, -273.15, "°F = °C × 9/5 + 32"),
    "Celsius → Kelvin": ("°C", "K", celsius_a_kelvin, -273.15, "K = °C + 273.15"),
    "Fahrenheit → Celsius": ("°F", "°C", fahrenheit_a_celsius, -459.67, "°C = (°F − 32) × 5/9"),
    "Fahrenheit → Kelvin": ("°F", "K", fahrenheit_a_kelvin, -459.67, "K = (°F − 32) × 5/9 + 273.15"),
    "Kelvin → Celsius": ("K", "°C", kelvin_a_celsius, 0.0, "°C = K − 273.15"),
    "Kelvin → Fahrenheit": ("K", "°F", kelvin_a_fahrenheit, 0.0, "°F = (K − 273.15) × 9/5 + 32"),
}

st.title("Conversor de temperatura")

opcion = st.sidebar.radio("Conversión", list(CONVERSIONES))
origen, destino, convertir, minimo, formula = CONVERSIONES[opcion]

valor = st.number_input(
    f"Grados ({origen})",
    min_value=minimo,
    value=max(0.0, minimo),
    step=0.5,
    format="%.2f",
)

resultado = round(convertir(valor), 2)

st.metric(label=f"{valor:.2f} {origen} equivalen a", value=f"{resultado:.2f} {destino}")
st.caption(f"Fórmula: {formula}")
