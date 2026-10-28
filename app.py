import streamlit as st

CERO_ABSOLUTO_C = -273.15

st.set_page_config(
    page_title="Conversor de temperatura",
    page_icon="🌡️",
    layout="centered",
)


def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte grados Celsius a grados Fahrenheit, redondeado a 2 decimales."""
    return round(celsius * 9 / 5 + 32, 2)


st.title("🌡️ Conversor de temperatura")
st.caption("Convierte grados Celsius a Fahrenheit al instante.")
st.divider()

with st.container(border=True):
    entrada, salida = st.columns(2, gap="large")

    with entrada:
        st.subheader("🧊 Celsius")
        celsius = st.number_input(
            "Grados Celsius (°C)",
            min_value=CERO_ABSOLUTO_C,
            value=0.0,
            step=0.5,
            format="%.2f",
        )

    fahrenheit = celsius_a_fahrenheit(celsius)

    with salida:
        st.subheader("🔥 Fahrenheit")
        st.metric(
            label=f"{celsius:.2f} °C equivalen a",
            value=f"{fahrenheit:.2f} °F",
        )

if celsius <= 0:
    st.info("❄️ Temperatura bajo o en el punto de congelación del agua.")
elif celsius < 25:
    st.success("🌤️ Temperatura fresca o agradable.")
elif celsius < 40:
    st.warning("☀️ Temperatura cálida.")
else:
    st.error("🔥 Temperatura muy alta.")

with st.expander("📐 Ver fórmula"):
    st.latex(r"^\circ F = ^\circ C \times \frac{9}{5} + 32")
