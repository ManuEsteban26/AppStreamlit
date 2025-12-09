import streamlit as st
import time
from PIL import Image
import requests
from io import BytesIO

# --- CONFIGURACIÓN INICIAL ---
st.set_page_config(
    page_title="NPS Zonamerica 2024 – Comunidad", 
    page_icon="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAAAKlBMVEVHcEwwrGgwrGgwrGgwrGgwrGgwrGgwrGgwrGgwrGgwrGgwrGgwrGgwrGjV3fMIAAAADXRSTlMATcoq3TlrrwhiivAW61nCVAAAAJ9JREFUKJHNkUsSxCAIREURxMT7X3ckxM9osp2a3hh8dtEQ5/5XwJ7hhfmiyvqZQGKaWSim4E575tPqPBhLk//yEkU9G8T7PgrdUSAfpTdQiRUZMhaWpLGRyR5z70LnOkLsTK46hTBg7hDrLVxpfVidPYkqtrXZVLWkiY4JAWwdk3nf8uSUDY7dlbDB0dRvbCwEH1iNrj8H6ZGp0iv5hT6F0gp3kbmSPQAAAABJRU5ErkJggg==", 
    layout="centered"
)

# --- FUNCIÓN GUARDAR EN SUPABASE (Solo para Comunidad) ---
def guardar_en_supabase(datos, tabla):
    """
    Guarda los datos de la encuesta en Supabase.
    """
    try:
        from supabase import create_client, Client
        
        url = "https://ekyfwvxmkagwaonrbafk.supabase.co"
        key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVreWZ3dnhta2Fnd2FvbnJiYWZrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ2NjE5MTIsImV4cCI6MjA4MDIzNzkxMn0.VD1QFtqxHAkfp1D_TQj4GUCD8YKzmu14oQMpiOkrDX0"
        supabase: Client = create_client(url, key)

        if tabla == "Cuestionario_Comunidad":
            # Mapear los datos al esquema de la tabla Cuestionario_Comunidad
            supabase_data = {
                # Datos generales
                "aceptacion_politica": datos.get("aceptacion_politica"),
                "empresa_actual": datos.get("empresa_actual"),
                
                # Pregunta 3: Fiabilidad
                "calificacion_fiabilidad_eficiente": datos.get("p3_1_eficiente"),
                "calificacion_fiabilidad_resuelve": datos.get("p3_2_resuelve"),
                
                # Pregunta 4: Capacidad de respuesta
                "calificacion_capacidad_respuesta_concluye": datos.get("p4_1_concluye"),
                "calificacion_capacidad_respuesta_atencion": datos.get("p4_2_atencion"),
                
                # Pregunta 5: Confianza
                "calificacion_confianza_humano": datos.get("p5_1_humano"),
                "calificacion_confianza_conocimiento": datos.get("p5_2_conocimiento"),
                
                # Pregunta 6: Empatía
                "calificacion_empatia_comprende": datos.get("p6_1_comprende"),
                "calificacion_empatia_ofrece": datos.get("p6_2_ofrece"),
                
                # Pregunta 7: Elementos Tangibles
                "calificacion_elementos_tangibles_intalaciones": datos.get("p7_1_instalaciones"),
                "calificacion_elementos_tangibles_equipamentos": datos.get("p7_2_equipamientos"),
                
                # Pregunta 8: Servicios Generales Contratados
                "calificacion_servicios_generales_calidad": datos.get("p8_calidad"),
                "calificacion_servicios_generales_alquiler": datos.get("p8_alquiler"),
                "calificacion_servicios_generales_promovidas": datos.get("p8_promovidas"),
                "calificacion_servicios_generales_aire": datos.get("p8_aire"),
                "calificacion_servicios_generales_internet": datos.get("p8_internet"),
                "calificacion_servicios_generales_mantenimiento": datos.get("p8_mantenimiento"),
                "calificacion_servicios_generales_telefono": datos.get("p8_telefono"),
                
                # Pregunta 9: Amenities
                "calificacion_amenities_restaurante": datos.get("p9_restaurante"),
                "calificacion_amenities_cafe": datos.get("p9_cafe"),
                "calificacion_amenities_cajero": datos.get("p9_cajero"),
                "calificacion_amenities_vending": datos.get("p9_vending"),
                "calificacion_amenities_area": datos.get("p9_area"),
                
                # Preguntas 10-11: Observaciones
                "observaciones_servicios_generales": datos.get("p10_obs_servicios"),
                "observaciones_amenities": datos.get("p11_obs_amenities"),
                
                # Pregunta 12-13: Cierre
                "experiencia_emocional": datos.get("p12_emocion"),
                "nps_score": datos.get("p13_nps")
            }
            
            with st.spinner("Guardando respuestas..."):
                result = supabase.table(tabla).insert(supabase_data).execute()
            
            if result.data:
                st.success("✅ ¡Datos guardados exitosamente!")
                st.balloons()
                time.sleep(2)
                return True
            else:
                st.warning("⚠️ No se pudo confirmar el guardado de los datos")
                return False
            
    except Exception as e:
        st.error(f"❌ Error al guardar: {e}")
        # Mostrar datos para depuración en caso de error
        with st.expander("Ver datos que se intentaron guardar"):
            st.json(datos)
        return False

# --- ENCUESTA 3: COMUNIDAD ---
def show_survey_comunidad():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.image("https://web.zonamerica.com/colombia/wp-content/themes/zaco/assets/img/logo.png", width=200)
    with col3:
        st.image("https://cdn.brandfetch.io/ida2XlnzHx/theme/dark/logo.svg?c=1bxid64Mup7aczewSAYMX&t=1680282084001", width=200)

    # Encabezado principal del formulario
    st.title("NPS Zonamerica 2024 – Encuesta Comunidad")

    # Mensaje introductorio
    st.markdown("""
    Este contenido lo creó el propietario del formulario. Los datos que envíes se enviarán al propietario del formulario.

    No somos responsables de las prácticas de privacidad o seguridad de sus clientes, incluidas las que adopte el propietario de este formulario. Nunca comparta su contraseña.

    Sus datos personales serán tratados conforme a los lineamientos establecidos en nuestra
    [Política de Protección de Datos Personales](https://web.zonamerica.com/colombia/wp-content/uploads/2022/11/JUR.PO_.01-Politica-de-Tratamiento-de-Datos-Personales-v1.pdf)

    **¡Gracias por su participación!**
    """)

    st.markdown("---")

    with st.form("form_comunidad"):
        # Pregunta 1: Política de datos
        st.markdown("<h4 style='font-size: 20px;'>1. Usted acepta la política de tratamiento de datos. (*)</h4>", unsafe_allow_html=True)
        aceptacion = st.radio("", ["Sí", "No"], horizontal=True, label_visibility="collapsed", key="com_aceptacion")

        # Pregunta 2: Empresa donde labora
        st.markdown("<h4 style='font-size: 20px;'>2. Escriba el nombre de la empresa donde labora actualmente dentro de Zonamerica. (*)</h4>", unsafe_allow_html=True)
        empresa_actual = st.text_input("Empresa actual", label_visibility="collapsed", key="com_empresa_actual")

        st.markdown("---")

        # Pregunta 3: Fiabilidad
        st.markdown("<h4 style='font-size: 20px;'>3. Fiabilidad</h4>", unsafe_allow_html=True)
        st.caption("En una escala del 1 al 5, siendo 1=muy insatisfecho y 5=muy satisfecho, califica: (*)")

        st.markdown("**3.1** En Zonamerica le brindan un servicio eficiente y eficaz.")
        fiabilidad_3_1 = st.selectbox("3.1", [1, 2, 3, 4, 5], index=2, key="com_fia_3_1", label_visibility="collapsed")

        st.markdown("**3.2** Zonamerica resuelve íntegramente sus necesidades como usuario/cliente.")
        fiabilidad_3_2 = st.selectbox("3.2", [1, 2, 3, 4, 5], index=2, key="com_fia_3_2", label_visibility="collapsed")

        # Pregunta 4: Capacidad de respuesta
        st.markdown("<h4 style='font-size: 20px;'>4. Capacidad de respuesta</h4>", unsafe_allow_html=True)
        st.caption("En una escala del 1 al 5, siendo 1=muy insatisfecho y 5=muy satisfecho, califica: (*)")

        st.markdown("**4.1** Zonamerica concluye sus requerimientos a tiempo.")
        capacidad_4_1 = st.selectbox("4.1", [1, 2, 3, 4, 5], index=2, key="com_cap_4_1", label_visibility="collapsed")

        st.markdown("**4.2** ¿La atención por parte de Zonamerica es oportuna y eficaz?")
        capacidad_4_2 = st.selectbox("4.2", [1, 2, 3, 4, 5], index=2, key="com_cap_4_2", label_visibility="collapsed")

        # Pregunta 5: Confianza
        st.markdown("<h4 style='font-size: 20px;'>5. Confianza</h4>", unsafe_allow_html=True)
        st.caption("En una escala del 1 al 5, siendo 1=muy insatisfecho y 5=muy satisfecho, califica: (*)")

        st.markdown("**5.1** El equipo humano de Zonamerica es amable, diligente e infunde confianza en usted.")
        confianza_5_1 = st.selectbox("5.1", [1, 2, 3, 4, 5], index=2, key="com_con_5_1", label_visibility="collapsed")

        st.markdown("**5.2** ¿El personal de Zonamerica es conocedor en las áreas de su desempeño?")
        confianza_5_2 = st.selectbox("5.2", [1, 2, 3, 4, 5], index=2, key="com_con_5_2", label_visibility="collapsed")

        # Pregunta 6: Empatía
        st.markdown("<h4 style='font-size: 20px;'>6. Empatía</h4>", unsafe_allow_html=True)
        st.caption("En una escala del 1 al 5, siendo 1=muy insatisfecho y 5=muy satisfecho, califica: (*)")

        st.markdown("**6.1** Zonamerica comprende y se preocupa por las necesidades específicas de su empresa.")
        empatia_6_1 = st.selectbox("6.1", [1, 2, 3, 4, 5], index=2, key="com_emp_6_1", label_visibility="collapsed")

        st.markdown("**6.2** Zonamerica ofrece opciones adecuadas para su tipo de negocio.")
        empatia_6_2 = st.selectbox("6.2", [1, 2, 3, 4, 5], index=2, key="com_emp_6_2", label_visibility="collapsed")

        # Pregunta 7: Elementos Tangibles
        st.markdown("<h4 style='font-size: 20px;'>7. Elementos Tangibles</h4>", unsafe_allow_html=True)
        st.caption("En una escala del 1 al 5, siendo 1=muy insatisfecho y 5=muy satisfecho, califica: (*)")

        st.markdown("**7.1** Las instalaciones físicas de Zonamerica son cómodas, visualmente atractivas y de aspecto impecable.")
        tangibles_7_1 = st.selectbox("7.1", [1, 2, 3, 4, 5], index=2, key="com_tan_7_1", label_visibility="collapsed")

        st.markdown("**7.2** Zonamerica cuenta con equipamientos modernos y eficientes.")
        tangibles_7_2 = st.selectbox("7.2", [1, 2, 3, 4, 5], index=2, key="com_tan_7_2", label_visibility="collapsed")

        st.markdown("---")

        # Pregunta 8: Servicios generales contratados
        st.markdown("<h4 style='font-size: 20px;'>8. Servicios generales contratados</h4>", unsafe_allow_html=True)
        st.caption("En una escala del 1 al 5, siendo 1=muy insatisfecho y 5=muy satisfecho, califica: (*)")
        col8_a, col8_b = st.columns(2)
        with col8_a:
            sg_calidad = st.selectbox("Calidad y estado de mantenimiento, limpieza de su edificio y áreas comunes", [1, 2, 3, 4, 5], index=2, key="com_sg_calidad")
            sg_alquiler = st.selectbox("Alquiler de espacios y equipos para actividades propias de cada usuario/cliente", [1, 2, 3, 4, 5], index=2, key="com_sg_alquiler")
            sg_promovidas = st.selectbox("Actividades promovidas por Zonamerica para el bienestar de la comunidad", [1, 2, 3, 4, 5], index=2, key="com_sg_promovidas")
            sg_aire = st.selectbox("Aire acondicionado", [1, 2, 3, 4, 5], index=2, key="com_sg_aire")
        with col8_b:
            sg_internet = st.selectbox("Internet", [1, 2, 3, 4, 5], index=2, key="com_sg_internet")
            sg_mantenimiento = st.selectbox("Mantenimiento y limpieza de la infraestructura de Zonamerica", [1, 2, 3, 4, 5], index=2, key="com_sg_mantenimiento")
            sg_telefono = st.selectbox("Telefonía", [1, 2, 3, 4, 5], index=2, key="com_sg_telefono")

        # Pregunta 9: Amenities
        st.markdown("<h4 style='font-size: 20px;'>9. Amenities</h4>", unsafe_allow_html=True)
        st.caption("En una escala del 1 al 5, siendo 1=muy insatisfecho y 5=muy satisfecho, califica: (*)")
        col9_a, col9_b = st.columns(2)
        with col9_a:
            am_restaurante = st.selectbox("Restaurante", [1, 2, 3, 4, 5], index=2, key="com_am_rest")
            am_cafe = st.selectbox("Café", [1, 2, 3, 4, 5], index=2, key="com_am_cafe")
            am_cajero = st.selectbox("Cajero", [1, 2, 3, 4, 5], index=2, key="com_am_cajero")
        with col9_b:
            am_vending = st.selectbox("Vending Machine", [1, 2, 3, 4, 5], index=2, key="com_am_vend")
            am_area = st.selectbox("Áreas de esparcimiento en general", [1, 2, 3, 4, 5], index=2, key="com_am_area")

        st.markdown("---")

        # Pregunta 10: Observaciones - Servicios Generales
        st.markdown("<h4 style='font-size: 20px;'>10. Observaciones - Servicios Generales (*)</h4>", unsafe_allow_html=True)
        st.caption("Si tiene alguna observación, recomendación, solicitud o pedido específico con respecto a Servicios Generales, nos gustaría mucho contar con su opinión. Gracias")
        obs_servicios = st.text_area("Observaciones servicios generales", key="com_obs_serv", label_visibility="collapsed")

        # Pregunta 11: Observaciones - Amenities
        st.markdown("<h4 style='font-size: 20px;'>11. Observaciones - Amenities (*)</h4>", unsafe_allow_html=True)
        st.caption("Si tiene alguna observación, recomendación, solicitud o pedido específico con respecto a Servicios de Bienestar o empresas de apoyo-AMENITIES-, nos gustaría mucho contar con su opinión. Gracias")
        obs_amenities = st.text_area("Observaciones amenities", key="com_obs_amen", label_visibility="collapsed")

        # Pregunta 12: Experiencia emocional
        st.markdown("<h4 style='font-size: 20px;'>12. ¿Cómo se siente acerca de su experiencia general con Zonamerica? (*)</h4>", unsafe_allow_html=True)
        emocion = st.radio(
            "Emoción",
            ["Feliz 😄", "Encantado 🤩", "Neutral 😐", "Decepcionado 😞", "Molesto 😠"],
            horizontal=True,
            key="com_emocion",
            label_visibility="collapsed"
        )

        # Pregunta 13: NPS
        st.markdown("<h4 style='font-size: 20px;'>13. De 1 a 10, ¿Qué tanto recomendaría a sus colegas o amigos Zonamerica? (*)</h4>", unsafe_allow_html=True)
        nps = st.selectbox("NPS", options=range(1, 11), index=8, key="com_nps", label_visibility="collapsed")

        submitted = st.form_submit_button("Enviar Encuesta Comunidad", type="primary", use_container_width=True)

        if submitted:
            if aceptacion == "No":
                st.error("⚠️ Debe aceptar la política de tratamiento de datos para continuar.")
            elif not empresa_actual:
                st.error("⚠️ Por favor complete el nombre de la empresa donde labora.")
            else:
                data_payload = {
                    "aceptacion_politica": aceptacion == "Sí",
                    "empresa_actual": empresa_actual,
                    "p3_1_eficiente": fiabilidad_3_1,
                    "p3_2_resuelve": fiabilidad_3_2,
                    "p4_1_concluye": capacidad_4_1,
                    "p4_2_atencion": capacidad_4_2,
                    "p5_1_humano": confianza_5_1,
                    "p5_2_conocimiento": confianza_5_2,
                    "p6_1_comprende": empatia_6_1,
                    "p6_2_ofrece": empatia_6_2,
                    "p7_1_instalaciones": tangibles_7_1,
                    "p7_2_equipamientos": tangibles_7_2,
                    "p8_calidad": sg_calidad,
                    "p8_alquiler": sg_alquiler,
                    "p8_promovidas": sg_promovidas,
                    "p8_aire": sg_aire,
                    "p8_internet": sg_internet,
                    "p8_mantenimiento": sg_mantenimiento,
                    "p8_telefono": sg_telefono,
                    "p9_restaurante": am_restaurante,
                    "p9_cafe": am_cafe,
                    "p9_cajero": am_cajero,
                    "p9_vending": am_vending,
                    "p9_area": am_area,
                    "p10_obs_servicios": obs_servicios,
                    "p11_obs_amenities": obs_amenities,
                    "p12_emocion": emocion,
                    "p13_nps": nps
                }
                guardar_en_supabase(data_payload, "Cuestionario_Comunidad")

if __name__ == '__main__':
    show_survey_comunidad()