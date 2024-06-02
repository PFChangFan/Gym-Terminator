import streamlit as st
from datetime import date, timedelta
import re 
import pydeck as pdk
from googletrans import Translator
from streamlit_player import st_player


idiomas = {"es": "Español", "en": "English", "fr": "Français", "de": "Deutsch",
"pt": "Português", 'ja': "Japanese"}
translator = Translator()

idioma_seleccionado = st.selectbox("Elige tu idioma", list(idiomas.keys()), format_func=lambda x: idiomas[x])

title2 = "Sobre nosotros"
bio = "En el corazón de California, donde los músculos son tan famosos como las estrellas de cine, se alza un templo de acero y sudor: el gimnasio Terminator. Fundado por el mismísimo Arnold Schwarzenegger, este gimnasio es más exclusivo que la premiere de Terminator 2: Día del Juicio. Arnold creó el gimnasio con el objetivo de influir en cualquiera para seguir sus pasos; su cadena es tan famosa que cuenta con gimnasios en 55 ciudades por el mundo, como lo podrán ver en el mapa (realmente no existen XD). Pero, para poder expandir su negocio, decidió contratarme, a un profesional dios en la programación (es mentira, suspendí XDDDDDDD). De igual forma, esta página es para todo aquel que se siente inspirado a conseguir su físico y cumplir sus sueños en una realidad. Vamos a empezar."
title1 = "Welcome to Gym Terminator 😎"
subheader1 = "Vamos a crearte un perfil"
subheader2 = "Empecemos con su nombre y apellidos"
input1 = "Ingrese su nombre y apellidos:"
welcome = "Bienvenido"
birthdate = "Ingrese su día, mes y año de nacimiento"
minus15 = "Lo siento, no puedes entrar al gimnasio si eres menor de 15 años."
continue_age = "Continuemos"
gender = "Que tipo de terminator eres?"
weight_translate = "Seleccione su peso en libras"
height_translate = "Seleccione su altura en metros"
weight_metric = "Mi peso es de "
height_metric = "Mi estatura es de "
weight_unit = "lb"
weight_word = "Weight"
height_word = "Height"
choose_country = "Elige un país"
choose_prov = "Elige una provincia"
choose_mun = "Elige un municipio"
choose_city = "Ingresa la ciudad de donde vienes"
confirm_button = "Confirmar"
you_choose = "Has elegido"
prov = "provincia"
mun = "municipio"
city_origin = "y vienes de la ciudad de"
profile = "Cree su perfil soldado🤖"
email = "Introduce tu correo electrónico"
enter_password = "Introduce tu contraseña"
create_profile = "Crear Cuenta"
profile_created = "¡Cuenta creada con éxito!👌"
error_profile = "Error: El correo electrónico o la contraseña no cumplen con las condiciones requeridas."
conditions = "En el correo debe contener un @ y un dominio. Solo caracteres permitidos: letras, números, puntos, guiones y guiones bajos. Y para la contraseña mínimo 8 caracteres, al menos una letra mayúscula, una letra minúscula, un número y un carácter especial (@$!%*?&)."
goals1 = "Mejorar la condición física"
goals2 = "Perder peso"
goals3 = "Ganar masa muscular"
goals4 = "Mejorar la salud en general"
goals5 = "Terminator 🥵"
reasons = "¿Cuáles son sus motivos para ingresar en nuestro gym?"
day1 = "Día 1"
day2 = "Día 2"
day3 = "Día 3"
day4 = "Día 4"
day5 = "Día 5"
day6 = "Día 6"
day7 = "Día 6"
day1_ex = "Sentadillas, Press de banca y Deadlifts"
day2_ex = "Dominadas, Dips, Curl de bíceps"
day3_ex = "Press militar, Elevaciones laterales y Tríceps en pole"
day4_ex = "Zancadas, Prensa de piernas y Gemelos en máquina"
day5_ex = "Remo con barra, Pull-ups y Face pulls"
day6_ex = "Fondos en paralelas, Flexiones y Plancha"
day7_ex = "Descanso o cardio ligero"
select_day = "Selecciona el día de la semana:"
ex_day = "Ejercicios para el"
markdown_ex = "No se preocupe, con esta rutina podrá empezar a convertirse en el próximo Schwarzenegger. Esta rutina consiste en 7 días dedicados a partes específicas del cuerpo, lo cual es una buena forma de empezar a ganar músculo y fuerza."
markdown_ex2 = "Si desea ver con más detalle, aquí le dejamos videos del mismo Arnold donde puede ver su rutina."
final_text = "Gracias por ingresar en nuestro gym, y recuerde, hay que estar fuerte para el Día del Juicio 😎"

translated_title1 = translator.translate(title1, dest=idioma_seleccionado).text
translated_bio1 = translator.translate(bio, dest=idioma_seleccionado).text
translated_bio = translator.translate(bio, dest=idioma_seleccionado).text
translated_subheader1 = translator.translate(subheader1, dest=idioma_seleccionado).text
translated_subheader2 = translator.translate(subheader2, dest=idioma_seleccionado).text
input_label = translator.translate(input1, dest=idioma_seleccionado).text
welcome_message = translator.translate(welcome, dest=idioma_seleccionado).text
birthdate1 = translator.translate(birthdate, dest=idioma_seleccionado).text
minus15_1 = translator.translate(minus15, dest=idioma_seleccionado).text
continue_age1 = translator.translate(continue_age, dest=idioma_seleccionado).text
gender1 = translator.translate(gender, dest=idioma_seleccionado).text
weight1 = translator.translate(weight_translate, dest=idioma_seleccionado).text
height1 = translator.translate(height_translate, dest=idioma_seleccionado).text
weight_metric1 = translator.translate(weight_metric, dest=idioma_seleccionado).text
height_metric1 = translator.translate(height_metric, dest=idioma_seleccionado).text
weight_unit1 = translator.translate(weight_unit, dest=idioma_seleccionado).text
weight_word1 = translator.translate(weight_word, dest=idioma_seleccionado).text
height_word1 = translator.translate(height_word, dest=idioma_seleccionado).text
choose_country1 = translator.translate(choose_country, dest=idioma_seleccionado).text
choose_prov1 = translator.translate(choose_prov, dest=idioma_seleccionado).text
choose_mun1 = translator.translate(choose_mun, dest=idioma_seleccionado).text
choose_city1 = translator.translate(choose_city, dest=idioma_seleccionado).text
confirm_button1 = translator.translate(confirm_button, dest=idioma_seleccionado).text
you_choose1 = translator.translate(you_choose, dest=idioma_seleccionado).text
prov1 = translator.translate(prov, dest=idioma_seleccionado).text
mun1 = translator.translate(mun, dest=idioma_seleccionado).text
city_origin1 = translator.translate(city_origin, dest=idioma_seleccionado).text
profile1 = translator.translate(profile, dest=idioma_seleccionado).text
email1 = translator.translate(email, dest=idioma_seleccionado).text
enter_password1 = translator.translate(enter_password, dest=idioma_seleccionado).text
create_profile1 = translator.translate(create_profile, dest=idioma_seleccionado).text
profile_created1 = translator.translate(profile_created, dest=idioma_seleccionado).text
error_profile1 = translator.translate(error_profile, dest=idioma_seleccionado).text
conditions1 = translator.translate(conditions, dest=idioma_seleccionado).text
goals1_1 = translator.translate(goals1, dest=idioma_seleccionado).text
goals2_1 = translator.translate(goals2, dest=idioma_seleccionado).text
goals3_1 = translator.translate(goals3, dest=idioma_seleccionado).text
goals4_1 = translator.translate(goals4, dest=idioma_seleccionado).text
goalss5_1 = translator.translate(goals5, dest=idioma_seleccionado).text
reasons1 = translator.translate(reasons, dest=idioma_seleccionado).text
day1_ex1 = translator.translate(day1_ex, dest=idioma_seleccionado).text
day2_ex1 = translator.translate(day2_ex, dest=idioma_seleccionado).text
day3_ex1 = translator.translate(day3_ex, dest=idioma_seleccionado).text
day4_ex1 = translator.translate(day4_ex, dest=idioma_seleccionado).text
day5_ex1 = translator.translate(day5_ex, dest=idioma_seleccionado).text
day6_ex1 = translator.translate(day6_ex, dest=idioma_seleccionado).text
day7_ex1 = translator.translate(day7_ex, dest=idioma_seleccionado).text
day1_1 = translator.translate(day1_ex, dest=idioma_seleccionado).text
day2_1 = translator.translate(day2_ex, dest=idioma_seleccionado).text
day3_1 = translator.translate(day3_ex, dest=idioma_seleccionado).text
day4_1 = translator.translate(day4_ex, dest=idioma_seleccionado).text
day5_1 = translator.translate(day5_ex, dest=idioma_seleccionado).text
day6_1 = translator.translate(day6_ex, dest=idioma_seleccionado).text
day7_1 = translator.translate(day7, dest=idioma_seleccionado).text
select_day1 = translator.translate(select_day, dest=idioma_seleccionado).text
ex_day1 = translator.translate(ex_day, dest=idioma_seleccionado).text
markdown_ex1 = translator.translate(markdown_ex, dest=idioma_seleccionado).text
markdown_ex2_1 = translator.translate(markdown_ex2, dest=idioma_seleccionado).text
final_text1 = translator.translate(final_text, dest=idioma_seleccionado).text

st.image("46580e9c3f5e17dc973da2f383b2a18a.jpg")
st.title(translated_title1)
st.markdown("cringe")

st.markdown(translated_bio1)
data = [
    {"name": "Tokio", "latitude": 35.6895, "longitude": 139.6917},
    {"name": "Nueva York", "latitude": 40.7128, "longitude": -74.0060},
    {"name": "París", "latitude": 48.8566, "longitude": 2.3522},
    {"name": "Madrid", "latitude": 40.4168, "longitude": -3.7038},
    {"name": "Roma", "latitude": 41.8967, "longitude": 12.4822},
    {"name": "Berlín", "latitude": 52.5200, "longitude": 13.4050},
    {"name": "Miami", "latitude": 25.7617, "longitude": -80.1918},
    {"name": "Vienna", "latitude":48.2081, "longitude": 16.3713},
    {"name": "La Habana", "latitude": 23.1136, "longitude": -82.3666},
    {"name": "Lisboa", "latitude": 38.7223, "longitude": -9.1393},
    {"name": "Estocolmo", "latitude": 59.3293, "longitude": 18.0686},
    {"name": "Londres", "latitude": 51.5072, "longitude": -0.1276},
    {"name": "Hong Kong", "latitude": 22.3193, "longitude": 114.1694},
    {"name": "Los Ángeles", "latitude": 34.0549, "longitude": -118.2426},
    {"name": "San Francisco", "latitude": 37.7749, "longitude": -122.4194},
    {"name": "Singapur", "latitude": 1.3521, "longitude": 103.8198},
    {"name": "Seúl", "latitude": 37.5519, "longitude": 126.9918},
    {"name": "Chicago", "latitude": 41.8781, "longitude": -87.6298},
    {"name": "Shanghái", "latitude": 31.2304, "longitude": 121.4737},
    {"name": "Boston", "latitude": 42.3601, "longitude": -71.0589},
    {"name": "Washington D. C.", "latitude": 38.9072, "longitude": -77.0369},
    {"name": "Fráncfort", "latitude": 50.1109, "longitude": 8.6821},
    {"name": "Dubái", "latitude": 25.276987, "longitude": 55.296249},
    {"name": "Ámsterdam", "latitude": 52.3676, "longitude": 4.9041},
    {"name": "Zúrich", "latitude": 47.3769, "longitude": 8.5417},
    {"name": "Ciudad de México", "latitude": 19.4326, "longitude": -99.1332},
    {"name": "Río de Janeiro", "latitude": -22.9068, "longitude": -43.1729},
    {"name": "São Paulo", "latitude": -23.5505, "longitude": -46.6333},
    {"name": "Santiago de Chile", "latitude": -33.4489, "longitude": -70.6693},
    {"name": "Bogotá", "latitude": 4.7110, "longitude": -74.0721},
    {"name": "Buenos Aires", "latitude": -34.6037, "longitude": -58.3816},
    {"name": "Ciudad de Panamá", "latitude": 8.9824, "longitude": -79.5199},
    {"name": "Sídney", "latitude": -33.8688, "longitude": 151.2093},
    {"name": "Moscú", "latitude": 55.7558, "longitude": 37.6173},
    {"name": "Toronto", "latitude": 43.6532, "longitude": -79.3832},
    {"name": "Barcelona", "latitude": 41.3851, "longitude": 2.1734},
    {"name": "Dallas", "latitude": 32.7767, "longitude": -96.7970},
    {"name": "Osaka", "latitude": 34.6937, "longitude": 135.5023},
    {"name": "Portland", "latitude": 45.5152, "longitude": -122.6784},
    {"name": "Liverpool", "latitude": 53.4084, "longitude": -2.9916},
    {"name": "Sevilla", "latitude": 37.3891, "longitude": -5.9845},
    {"name": "Oporto", "latitude": 41.1579, "longitude": -8.6291},
    {"name": "Lyon", "latitude": 45.7640, "longitude": 4.8357},
    {"name": "Montreal", "latitude": 45.5017, "longitude": -73.5673},
    {"name": "Bombay", "latitude": 19.0760, "longitude": 72.8777},
    {"name": "Bangkok", "latitude": 13.7563, "longitude": 100.5018},
    {"name": "Johannesburgo", "latitude": -26.2041, "longitude": 28.0473},
    {"name": "Copenhague", "latitude": 55.6761, "longitude": 12.5683},
    {"name": "Medellín", "latitude": 6.2442, "longitude": -75.5812},
    {"name": "Kuala Lumpur", "latitude": 3.1390, "longitude": 101.6869},
    {"name": "Seattle", "latitude": 47.6062, "longitude": -122.3321},
    {"name": "Las Vegas", "latitude": 36.1699, "longitude": -115.1398},
    {"name": "San Diego", "latitude": 32.7157, "longitude": -117.1611},
    {"name": "New Orleans", "latitude": 29.9511, "longitude": -90.0715},
    {"name": "Orlando", "latitude": 28.5383, "longitude": -81.3792},
    {"name": "Thal", "latitude": 47.0779, "longitude": 15.3554}    
]
    
view_state = pdk.ViewState(latitude=0, longitude=0, zoom=1)

layer = pdk.Layer(
    "ScatterplotLayer",
    data,
    get_position="[longitude, latitude]",
    get_color="[200, 30, 0, 160]",
    get_radius=50000,
)

st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

st.subheader(translated_subheader1)
st.subheader(translated_subheader2)
nombre = st.text_input(input_label)
st.write(f"{welcome_message}: {nombre}")

año_minimo = 1900
fecha_nacimiento = st.date_input(birthdate1, min_value=date(año_minimo, 1, 1))
hoy = date.today()
edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

if edad < 15:
    st.error(minus15_1)
else:
    st.success(continue_age1)
    
sexo = st.radio(gender1,
                ["Terminator XX", "Terminator XY", "Terminator XD"]
                )
weight = st.slider(weight1, 0, 600, 25)
st.write(f"{weight_metric1} {weight} {weight_unit}")
height = st.slider(height1, 0, 300, 25)
st.write(f"{height_metric1} {height} cm")
col1, col2, col3 = st.columns(3)
col1.metric(weight_word1, weight, weight//2.2)
col2.metric(height_word1, height, height /100)

paises = [
    "Estados Unidos", "España", "Italia", "Japón", "Alemania", "Austria", "Cuba", "Portugal",
    "Suecia", "UK", "Singapore", "Corea del Norte", "China", "Emiratos Árabes Unidos", "Países Bajos", "Suiza", "México",
    "Brasil", "Chile", "Colombia", "Argentina", "Panamá", "Australia", "Rusia", "Canadá", "Francia", "India", "Tailandia", "Sudáfrica",
    "Dinamarca", "Malasia"
]

municipios_cuba = {
    "Pinar del Rio": ["Monte", "Ciudad"],
    "La Habana": ["Plaza de la Revolución", "Habana Vieja", "Centro Habana", "Diez de Octubre", "Cerro", "Arroyo Naranjo", "Boyeros", "Playa", "Marianao", "La Lisa", "Guanabacoa", "Regla", "Habana del Este", "San Miguel del Padrón", "Cotorro"],
    "Matanzas": ["Matanzas", "Varadero", "Cardenas", "Campo XD"],
    "Holguin": ["Holguin", "Selva", "Monte", "Campo"],
    "Santiago de Cuba": ["Contramaestre", "Mella", "San Luis", "Segundo Frente", "Songo-La Maya", "Santiago de Cuba", "Palma Soriano", "Tercer Frente", "Guamá"],
    "Villa Clara": ["Santa Clara", "Ranchuelo", "Encrucijada", "Santo Domingo", "Placetas", "Corralillo", "Manicaragua", "Camajuaní", "Remedios"],
    "Cienfuegos": ["Abreus", "Aguada de Pasajeros", "Cienfuegos", "Cumanayagua", "Cruces", "Lajas", "Palmira", "Rodas"],
    "Sancti Spíritus": ["Sancti Spíritus", "Trinidad", "Cabaiguán", "Yaguajay", "Jatibonico", "Taguasco", "Fomento", "La Sierpe"],
    "Ciego de Ávila": ["Ciego de Ávila", " Morón, Chambas", "Primero de Enero", "Ciro Redondo", "Florencia", "Majagua", "Baraguá", "Bolivia", "Venezuela"],
    "Camagüey": ["Carlos Manuel de Céspedes", "Florida", "Nuevitas", "Esmeralda", "Minas", "Sibanicú", "Guáimaro", "Najasa", "Jimaguayú", "Vertientes", "Santa Cruz del Sur", "Sierra de Cubitas", "Camagüey"],
    "Las Tunas":["Manatí", "Puerto Padre", "Jesús Menéndez", "Majibacoa", "Las Tunas", "Jobabo", "Colombia", "Amancio"],
    "Granma": ["Guisa", "Media Luna", "Buey Arriba", "Cauto Cristo", "Jiguani", "Yara", "Bartolome Maso", "Pilon", "Rio Cauto"],
    "Guantánamo": ["Baracoa", "Caimanera", "El Salvador", "Guantánamo", "Imías", "Maisí", "Manuel Tames", "Niceto Pérez", "San Antonio del Sur", "Yateras"]
}

pais_elegido = st.selectbox(choose_country1, paises)

if pais_elegido == "Cuba":
    provincia_elegida = st.selectbox(choose_prov1, list(municipios_cuba.keys()))
    municipio_elegido = st.selectbox(choose_mun1, municipios_cuba[provincia_elegida])

else:
    ciudad = st.text_input(city_origin1, "", key="ciudad_otro")
    
if st.button(confirm_button1):
    if pais_elegido == "Cuba":
        st.write(f"{you_choose1} {pais_elegido}, {prov1} {provincia_elegida}, {mun1} {municipio_elegido}.")
    else:
        st.write(f"{you_choose1} {pais_elegido} {city_origin1} {ciudad}.")

def validar_email(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

def validar_contrasenna(contrasenna):
    patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(patron, contrasenna) is not None

st.title(profile1)

email_usuario = st.text_input(email1)

contrasenna_usuario = st.text_input(enter_password1, type="password")

if st.button(create_profile1):
    
    if validar_email(email_usuario) and validar_contrasenna(contrasenna_usuario):
        st.success(profile_created1)
    else:
        st.error(error_profile1)

st.markdown(conditions)

motivos = [
    goals1_1,
    goals2_1,
    goals3_1,
    goals4_1,
    goalss5_1
]
choice = st.selectbox(reasons1, motivos)

st.markdown(markdown_ex1)

ejercicios = {
    day1_1: [day1_ex1],
    day2_1: [day2_ex1],
    day3_1: [day3_ex1],
    day4_1: [day4_ex1],
    day5_1: [day5_ex1],
    day6_1: [day6_ex1],
    day7_1: [day7_ex1]
}

dia = st.selectbox(select_day1, list(ejercicios.keys()))

st.write(ex_day1, dia)
for ejercicio in ejercicios[dia]:
    st.write('- ', ejercicio)
    
st.markdown(markdown_ex2_1)

video_url = "https://youtu.be/o9zCgPtsups"
video_url2 = "https://youtu.be/A8gFTV0Dz_o?si"
video_url3 = "https://youtu.be/pCFVZexvQKY?si"

st_player(video_url)
st_player(video_url2)
st_player(video_url3)

st.markdown(final_text1)

st.image("images.jpg")