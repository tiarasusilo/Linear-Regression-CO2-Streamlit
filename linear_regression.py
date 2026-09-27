# Core Pkgs
import streamlit as st
import sklearn
import joblib, os
import numpy as np

# Loading Models
def load_prediction_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), "rb"))
    return loaded_model

def main():
    """Regresi Linier Sederhana"""

    st.title("Prediksi Emisi CO₂ Kendaraan")

    html_templ = """
    <div style="background-color:#640D14;padding:10px;">
    <h3 style="color:white">Prediksi Emisi CO₂ Kendaraan Menggunakan Regresi Linier</h3>
    </div>
    """

    st.markdown(html_templ, unsafe_allow_html=True)

    activity = ["Prediksi Emisi CO₂", "Apa itu Regresi?"]
    choice = st.sidebar.selectbox("Menu", activity)

    # CO2 Prediction CHOICE
    if choice == 'Prediksi Emisi CO₂':

        st.subheader("Prediksi Emisi CO₂ Kendaraan")

        engine_size = st.number_input(
            "Masukkan ukuran mesin kendaraan (L)",
            min_value=1.0,
            max_value=6.7,
            value=None,
            step=0.1
        )

        if st.button("Proses"):

            regressor = load_prediction_model(
                "linear_regression_co2.pkl"
            )

            engine_size_reshaped = np.array(engine_size).reshape(-1, 1)

            predicted_co2 = regressor.predict(engine_size_reshaped)

            st.info(
                "Prediksi emisi CO₂ untuk kendaraan dengan ukuran mesin {} L diprediksi sebesar {}"
                .format(engine_size, predicted_co2[0][0].round(2))
            )

    elif choice == 'Apa itu Regresi?':

        st.subheader("Apa itu Regresi?")
        st.write("Regresi linier adalah metode yang digunakan untuk mengetahui hubungan antara dua variabel dan melakukan prediksi.")
        st.write("Pada aplikasi ini, regresi linier digunakan untuk memprediksi emisi CO₂ berdasarkan ukuran mesin kendaraan.")

if __name__ == '__main__':
    main()