import streamlit as st

from web_functions import predict

def app(df, x,y):

	st.title("Halaman Prediksi")

	col1, col2, col3 = st.columns(3)

	with col1:
			tekanandarah = st.text_input ("Input Nilai Tekanan Darah")
	with col1:
			gravitas = st.text_input ("Input Nilai Gravitas")
	with col1:
			albumin = st.text_input ("Input Nilai Albumin")
	with col1:
			sugar = st.text_input ("Input Nilai sugar")
	with col1:
			seldarahmerah = st.text_input ("Input Nilai Sel Darah Merah")
	with col1:
			pussel = st.text_input ("Input Nilai pussel")
	with col1:
			puscell = st.text_input ("Input Nilai puscell")
	with col2:
			bakteri = st.text_input ("Input Nilai Bakteri")
	with col2:
			gds = st.text_input ("Input Nilai Gds")
	with col2:
			ureum = st.text_input ("Input Nilai Ureum")
	with col2:
			kreatinin = st.text_input ("Input Nilai Kreatinin")
	with col2:
			natrium = st.text_input ("Input Nilai Natrium")
	with col2:
			kalium = st.text_input ("Input Nilai Kalium")
	with col2:
			hemoglobin = st.text_input ("Input Nilai Hemoglobin")
	with col3:
			MCV = st.text_input ("Input Nilai Mcv")
	with col3:
			seldarahputih = st.text_input ("Input Nilai Sel Darah Putih")
	with col3:
			seldarahmerah_1 = st.text_input ("Input Nilai Sel Darah Merah 1")
	with col3:
			hipertensi = st.text_input ("Input Nilai Hipertensi")
	with col3:
			diabetes = st.text_input ("Input Nilai Diabetes")
	with col3:
			cad = st.text_input ("Input Nilai Cad")
	with col3:
			nafsumakan = st.text_input ("Input Nilai Nafsu Makan")
	with col3:
			edema = st.text_input ("Input Nilai Edema")
	with col3:
			anemia = st.text_input ("Input Nilai Anemia")


	features = [tekanandarah,gravitas,albumin,sugar,seldarahmerah,pussel,puscell,bakteri,gds,ureum,kreatinin,natrium,kalium,hemoglobin,MCV,seldarahputih,seldarahmerah_1,hipertensi,diabetes,cad,nafsumakan,edema,anemia]

	#button 
	if st.button("Prediksi"):
		prediction, score = predict(x,y,features)
		score = score
		st.info("Prediksi Sukses...")

		if (prediction == 1):
			st.warning("Orang Tersebut Rentan Terkena Penyakit Ginjal")

		else:
			st.success("Orang Tersebut Realtif Aman Dari Penyakit Ginjal")

		st.write("Model Yang Digunakan Memiliki Tingkat Akurasi", (score*100),"%")