import streamlit as st
import time
from PIL import Image
import requests
from io import BytesIO

# --- CONFIGURACIÓN INICIAL ---
st.set_page_config(
    page_title="NPS Zonamerica 2024 – Obra Gris", 
    page_icon="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAAAKlBMVEVHcEwwrGgwrGgwrGgwrGgwrGgwrGgwrGgwrGgwrGgwrGgwrGgwrGgwrGjV3fMIAAAADXRSTlMATcoq3TlrrwhiivAW61nCVAAAAJ9JREFUKJHNkUsSxCAIREURxMT7X3ckxM9osp2a3hh8dtEQ5/5XwJ7hhfmiyvqZQGKaWSim4E575tPqPBhLk//yEkU9G8T7PgrdUSAfpTdQiRUZMhaWpLGRyR5z70LnOkLsTK46hTBg7hDrLVxpfVidPYkqtrXZVLWkiY4JAWwdk3nf8uSUDY7dlbDB0dRvbCwEH1iNrj8H6ZGp0iv5hT6F0gp3kbmSPQAAAABJRU5ErkJggg==", 
    layout="centered"
)

# --- FUNCIÓN GUARDAR EN SUPABASE (Solo para Obra Gris) ---
def guardar_en_supabase(datos, tabla):
    """
    Guarda los datos de la encuesta en Supabase.
    """
    try:
        from supabase import create_client, Client
        
        url = "https://ekyfwvxmkagwaonrbafk.supabase.co"
        key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVreWZ3dnhta2Fnd2FvbnJiYWZrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ2NjE5MTIsImV4cCI6MjA4MDIzNzkxMn0.VD1QFtqxHAkfp1D_TQj4GUCD8YKzmu14oQMpiOkrDX0"
        supabase: Client = create_client(url, key)

        if tabla == "Cuestionario_Obra_Gris":
            # Mapear los datos al esquema de la tabla Cuestionario_Obra_Gris
            supabase_data = {
                # Datos generales
                "aceptacion_politica": datos.get("aceptacion_politica"),
                "razon_social": datos.get("razon_social"),
                "nombre_completo": datos.get("nombre_completo"),
                
                # Pregunta 4: Comunicación y Soporte
                "calificacion_comunicacion_soporte_comunicacion": datos.get("p4_1_comunicacion"),
                "calificacion_comunicacion_soporte_satisfecho": datos.get("p4_2_soporte"),
                
                # Pregunta 5: Fiabilidad
                "calificacion_fiabilidad_resuelve": datos.get("p5_1_resolucion"),
                "calificacion_fiabilidad_capacidad": datos.get("p5_2_capacidad"),
                
                # Pregunta 6: Capacidad de respuesta
                "calificacion_capacidad_respuesta_satisfecho": datos.get("p6_1_satisfecho"),
                "calificacion_capacidad_respuesta_capacidad": datos.get("p6_2_capacidad"),
                
                # Pregunta 7: Confianza
                "calificacion_confianza_integridad": datos.get("p7_1_integridad"),
                "calificacion_confianza_humano": datos.get("p7_2_humano"),
                
                # Pregunta 8: Empatía
                "calificacion_empatia_comprende": datos.get("p8_1_comprende"),
                "calificacion_empatia_demuestra": datos.get("p8_2_demuestra"),
                
                # Pregunta 9: Elementos Tangibles
                "calificacion_elementos_tangibles_oficinas": datos.get("p9_1_oficinas"),
                "calificacion_elementos_tangibles_calidad": datos.get("p9_2_calidad"),
                
                # Pregunta 10: Área TIC
                "calificacion_area_tecnologia_tiempo": datos.get("p10_tic_tiempo"),
                "calificacion_area_tecnologia_calidad": datos.get("p10_tic_calidad"),
                "calificacion_area_tecnologia_atencion": datos.get("p10_tic_atencion"),
                
                # Pregunta 11: Operaciones y Mantenimiento
                "calificacion_area_operaciones_tiempo": datos.get("p11_oper_tiempo"),
                "calificacion_area_operaciones_calidad": datos.get("p11_oper_calidad"),
                "calificacion_area_operaciones_atencion": datos.get("p11_oper_atencion"),
                
                # Pregunta 12: Comercial, Bienestar y ATC
                "calificacion_area_comercial_tiempo": datos.get("p12_comercial_tiempo"),
                "calificacion_area_comercial_calidad": datos.get("p12_comercial_calidad"),
                "calificacion_area_comercial_atencion": datos.get("p12_comercial_atencion"),
                
                # Pregunta 13: Administrativa y Financiera
                "calificacion_area_administrativa_tiempo": datos.get("p13_admin_tiempo"),
                "calificacion_area_administrativa_calidad": datos.get("p13_admin_calidad"),
                "calificacion_area_administrativa_atencion": datos.get("p13_admin_atencion"),
                
                # Pregunta 14: GCI y Control de Inventarios
                "calificacion_area_gci_tiempo": datos.get("p14_gci_tiempo"),
                "calificacion_area_gci_calidad": datos.get("p14_gci_calidad"),
                "calificacion_area_gci_atencion": datos.get("p14_gci_atencion"),
                
                # Pregunta 15: Servicios Contratados
                "calificacion_servicios_contratados_liempieza": datos.get("p15_limpieza"),
                "calificacion_servicios_contratados_aire": datos.get("p15_aire"),
                "calificacion_servicios_contratados_telefonia": datos.get("p15_telefonia"),
                "calificacion_servicios_contratados_internet": datos.get("p15_internet"),
                "calificacion_servicios_contratados_impresiones": datos.get("p15_impresiones"),
                "calificacion_servicios_contratados_vigilancia": datos.get("p15_vigilancia"),
                
                # Pregunta 16: Servicios Generales Zonamerica
                "satisfaccion_servicios_zonamerica_proceso": datos.get("p16_proceso"),
                "satisfaccion_servicios_zonamerica_seguridad": datos.get("p16_seguridad"),
                "satisfaccion_servicios_zonamerica_areas": datos.get("p16_areas"),
                "satisfaccion_servicios_zonamerica_alquiler": datos.get("p16_alquiler"),
                "satisfaccion_servicios_zonamerica_actividades": datos.get("p16_actividades"),
                "satisfaccion_servicios_zonamerica_mantenimiento": datos.get("p16_mantenimiento"),
                
                # Pregunta 17: Necesidades del personal
                "satisfaccion_necesidades_personal_restaurante": datos.get("p17_restaurante"),
                "satisfaccion_necesidades_personal_cafe": datos.get("p17_cafe"),
                "satisfaccion_necesidades_personal_cajero": datos.get("p17_cajero"),
                "satisfaccion_necesidades_personalvending": datos.get("p17_vending"),
                "satisfaccion_necesidades_personal_areas": datos.get("p17_esparcimiento"),
                
                # Pregunta 18: Satisfacción general
                "satisfaccion_general": str(datos.get("p18_satisfaccion_general")),
                
                # Preguntas 19-22: Observaciones
                "sugerencias_servicios_2025": datos.get("p19_servicios_2025"),
                "observaciones_servicios_generales": datos.get("p20_obs_servicios_generales"),
                "observaciones_servicios_contratados": datos.get("p21_obs_servicios_contratados"),
                "observaciones_amenities": datos.get("p22_obs_amenities"),
                
                # Pregunta 23-24: Cierre
                "experiencia_emocional": datos.get("p23_emocion"),
                "nps_score": datos.get("p24_nps")
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

# --- ENCUESTA 2: OBRA GRIS ---
def show_survey_obra_gris():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.image("https://web.zonamerica.com/colombia/wp-content/themes/zaco/assets/img/logo.png", width=200)
    with col3:
        st.image("https://cdn.brandfetch.io/ida2XlnzHx/theme/dark/logo.svg?c=1bxid64Mup7aczewSAYMX&t=1680282084001", width=200)

    # Encabezado principal del formulario
    st.title("NPS Zonamerica 2024 – Obra Gris")

    # Mensaje introductorio
    st.markdown("""
    Este contenido lo creó el propietario del formulario. Los datos que envíes se enviarán al propietario del formulario.

    No somos responsables de las prácticas de privacidad o seguridad de sus clientes, incluidas las que adopte el propietario de este formulario. Nunca comparta su contraseña.

    Sus datos personales serán tratados conforme a los lineamientos establecidos en nuestra
    [Política de Protección de Datos Personales](https://web.zonamerica.com/colombia/wp-content/uploads/2022/11/JUR.PO_.01-Politica-de-Tratamiento-de-Datos-Personales-v1.pdf)

    **¡Gracias por su participación!**
    """)

    st.markdown("---")

    with st.form("form_obra_gris"):
        # Pregunta 1: Política de datos
        st.markdown("<h4 style='font-size: 20px;'>1. Usted acepta la política de tratamiento de datos. (*)</h4>", unsafe_allow_html=True)
        aceptacion = st.radio("", ["Sí", "No"], horizontal=True, label_visibility="collapsed", key="og_aceptacion")

        # Pregunta 2: Razón social
        st.markdown("<h4 style='font-size: 20px;'>2. Escriba la razón social de su Organización/Empresa. (*)</h4>", unsafe_allow_html=True)
        razon_social = st.text_input("Razón Social", label_visibility="collapsed", key="og_razon_social")

        # Pregunta 3: Nombre
        st.markdown("<h4 style='font-size: 20px;'>3. Escriba su nombre y apellidos. (*)</h4>", unsafe_allow_html=True)
        nombre_completo = st.text_input("Nombre completo", label_visibility="collapsed", key="og_nombre_completo")

        st.markdown("---")

        # Pregunta 4: Comunicación y Soporte
        st.markdown("<h4 style='font-size: 20px;'>4. Comunicación y Soporte</h4>", unsafe_allow_html=True)
        st.caption("En una escala del 1 al 5, siendo 1=muy insatisfecho y 5=muy satisfecho, califica: (*)")

        st.markdown("**4.1** ¿Cómo evalúas la comunicación proporcionada por la administración de la Zonamerica?")
        comunicacion_4_1 = st.selectbox("4.1", [1, 2, 3, 4, 5], index=2, key="og_com_4_1", label_visibility="collapsed")

        st.markdown("**4.2** ¿Estás satisfecho con el nivel de soporte ofrecido por la zona franca?")
        comunicacion_4_2 = st.selectbox("4.2", [1, 2, 3, 4, 5], index=2, key="og_com_4_2", label_visibility="collapsed")

        # Pregunta 5: Fiabilidad
        st.markdown("<h4 style='font-size: 20px;'>5. Fiabilidad</h4>", unsafe_allow_html=True)
        st.caption("En una escala del 1 al 5, siendo 1=muy insatisfecho y 5=muy satisfecho, califica: (*)")

        st.markdown("**5.1** Zonamerica resuelve íntegramente sus necesidades como usuario/cliente.")
        fiabilidad_5_1 = st.selectbox("5.1", [1, 2, 3, 4, 5], index=2, key="og_fia_5_1", label_visibility="collapsed")

        st.markdown("**5.2** La capacidad de Zonamerica para cumplir con los acuerdos establecidos ha influido en la toma de decisiones estratégicas de tu empresa.")
        fiabilidad_5_2 = st.selectbox("5.2", [1, 2, 3, 4, 5], index=2, key="og_fia_5_2", label_visibility="collapsed")

        # Pregunta 6: Capacidad de respuesta
        st.markdown("<h4 style='font-size: 20px;'>6. Capacidad de respuesta</h4>", unsafe_allow_html=True)
        st.caption("En una escala del 1 al 5, siendo 1=muy insatisfecho y 5=muy satisfecho, califica: (*)")

        st.markdown("**6.1** ¿Te sientes satisfecho/a con la velocidad y eficacia de la respuesta a tus solicitudes y necesidades por parte de la administración de Zonamerica?")
        capacidad_6_1 = st.selectbox("6.1", [1, 2, 3, 4, 5], index=2, key="og_cap_6_1", label_visibility="collapsed")

        st.markdown("**6.2** ¿La capacidad de respuesta ágil de Zonamerica ha influido en la eficiencia operativa de tu empresa?")
        capacidad_6_2 = st.selectbox("6.2", [1, 2, 3, 4, 5], index=2, key="og_cap_6_2", label_visibility="collapsed")

        # Pregunta 7: Confianza
        st.markdown("<h4 style='font-size: 20px;'>7. Confianza</h4>", unsafe_allow_html=True)
        st.caption("En una escala del 1 al 5, siendo 1=muy insatisfecho y 5=muy satisfecho, califica: (*)")

        st.markdown("**7.1** ¿La integridad y ética empresarial de Zonamerica han contribuido a consolidar la confianza de tu empresa en su relación?")
        confianza_7_1 = st.selectbox("7.1", [1, 2, 3, 4, 5], index=2, key="og_con_7_1", label_visibility="collapsed")

        st.markdown("**7.2** ¿El equipo humano de Zonamerica, es amable y diligente e infunde confianza en usted?")
        confianza_7_2 = st.selectbox("7.2", [1, 2, 3, 4, 5], index=2, key="og_con_7_2", label_visibility="collapsed")

        # Pregunta 8: Empatía
        st.markdown("<h4 style='font-size: 20px;'>8. Empatía</h4>", unsafe_allow_html=True)
        st.caption("En una escala del 1 al 5, siendo 1=muy insatisfecho y 5=muy satisfecho, califica: (*)")

        st.markdown("**8.1** Zonamerica comprende y se preocupa por las necesidades específicas de tu empresa.")
        empatia_8_1 = st.selectbox("8.1", [1, 2, 3, 4, 5], index=2, key="og_emp_8_1", label_visibility="collapsed")

        st.markdown("**8.2** Zonamerica demuestra sensibilidad hacia las circunstancias individuales de las empresas establecidas en ella.")
        empatia_8_2 = st.selectbox("8.2", [1, 2, 3, 4, 5], index=2, key="og_emp_8_2", label_visibility="collapsed")

        # Pregunta 9: Elementos Tangibles
        st.markdown("<h4 style='font-size: 20px;'>9. Elementos Tangibles</h4>", unsafe_allow_html=True)
        st.caption("En una escala del 1 al 5, siendo 1=muy insatisfecho y 5=muy satisfecho, califica: (*)")

        st.markdown("**9.1** Las oficinas y espacios de trabajo, cumplen con tus expectativas y necesidades empresariales.")
        tangibles_9_1 = st.selectbox("9.1", [1, 2, 3, 4, 5], index=2, key="og_tan_9_1", label_visibility="collapsed")

        st.markdown("**9.2** La calidad de las instalaciones y servicios de Zonamerica ha impactado positivamente en la imagen y operación de tu empresa.")
        tangibles_9_2 = st.selectbox("9.2", [1, 2, 3, 4, 5], index=2, key="og_tan_9_2", label_visibility="collapsed")

        st.markdown("---")

        # Pregunta 10: Área de Tecnología/TIC'S
        st.markdown("<h4 style='font-size: 20px;'>10. Área de Tecnología/TIC'S</h4>", unsafe_allow_html=True)
        st.caption("En una escala del 1 al 5, siendo 1=muy insatisfecho y 5=muy satisfecho, califica: (*)")
        col10_1, col10_2, col10_3 = st.columns(3)
        with col10_1:
            tic_tiempo = st.selectbox("Tiempo de espera", [1, 2, 3, 4, 5], index=2, key="og_tic_tiempo")
        with col10_2:
            tic_calidad = st.selectbox("Calidad de servicio", [1, 2, 3, 4, 5], index=2, key="og_tic_calidad")
        with col10_3:
            tic_atencion = st.selectbox("Atención del personal", [1, 2, 3, 4, 5], index=2, key="og_tic_atencion")

        # Pregunta 11: Área de Operaciones y Equipos de Mantenimiento
        st.markdown("<h4 style='font-size: 20px;'>11. Área de Operaciones y Equipos de Mantenimiento</h4>", unsafe_allow_html=True)
        st.caption("En una escala del 1 al 5, siendo 1=muy insatisfecho y 5=muy satisfecho, califica: (*)")
        col11_1, col11_2, col11_3 = st.columns(3)
        with col11_1:
            oper_tiempo = st.selectbox("Tiempo de espera", [1, 2, 3, 4, 5], index=2, key="og_oper_tiempo")
        with col11_2:
            oper_calidad = st.selectbox("Calidad de servicio", [1, 2, 3, 4, 5], index=2, key="og_oper_calidad")
        with col11_3:
            oper_atencion = st.selectbox("Atención del personal", [1, 2, 3, 4, 5], index=2, key="og_oper_atencion")

        # Pregunta 12: Área Comercial, Bienestar y ATC
        st.markdown("<h4 style='font-size: 20px;'>12. Área Comercial, Bienestar y ATC</h4>", unsafe_allow_html=True)
        st.caption("En una escala del 1 al 5, siendo 1=muy insatisfecho y 5=muy satisfecho, califica: (*)")
        col12_1, col12_2, col12_3 = st.columns(3)
        with col12_1:
            com_tiempo = st.selectbox("Tiempo de espera", [1, 2, 3, 4, 5], index=2, key="og_com_tiempo")
        with col12_2:
            com_calidad = st.selectbox("Calidad de servicio", [1, 2, 3, 4, 5], index=2, key="og_com_calidad")
        with col12_3:
            com_atencion = st.selectbox("Atención del personal", [1, 2, 3, 4, 5], index=2, key="og_com_atencion")

        # Pregunta 13: Área Administrativa y Financiera
        st.markdown("<h4 style='font-size: 20px;'>13. Área Administrativa y Financiera</h4>", unsafe_allow_html=True)
        st.caption("En una escala del 1 al 5, siendo 1=muy insatisfecho y 5=muy satisfecho, califica: (*)")
        col13_1, col13_2, col13_3 = st.columns(3)
        with col13_1:
            admin_tiempo = st.selectbox("Tiempo de espera", [1, 2, 3, 4, 5], index=2, key="og_admin_tiempo")
        with col13_2:
            admin_calidad = st.selectbox("Calidad de servicio", [1, 2, 3, 4, 5], index=2, key="og_admin_calidad")
        with col13_3:
            admin_atencion = st.selectbox("Atención del personal", [1, 2, 3, 4, 5], index=2, key="og_admin_atencion")

        # Pregunta 14: Área GCI y Control de Inventarios
        st.markdown("<h4 style='font-size: 20px;'>14. Área GCI y Control de Inventarios</h4>", unsafe_allow_html=True)
        st.caption("En una escala del 1 al 5, siendo 1=muy insatisfecho y 5=muy satisfecho, califica: (*)")
        col14_1, col14_2, col14_3 = st.columns(3)
        with col14_1:
            gci_tiempo = st.selectbox("Tiempo de espera", [1, 2, 3, 4, 5], index=2, key="og_gci_tiempo")
        with col14_2:
            gci_calidad = st.selectbox("Calidad de servicio", [1, 2, 3, 4, 5], index=2, key="og_gci_calidad")
        with col14_3:
            gci_atencion = st.selectbox("Atención del personal", [1, 2, 3, 4, 5], index=2, key="og_gci_atencion")

        # Pregunta 15: Servicios Contratados
        st.markdown("<h4 style='font-size: 20px;'>15. Servicios Contratados</h4>", unsafe_allow_html=True)
        st.caption("En una escala del 1 al 5, siendo 1=muy insatisfecho y 5=muy satisfecho, califica el nivel de satisfacción de su empresa en relación a los siguientes servicios que ofrece Zonamerica: (*)")
        col15_a, col15_b = st.columns(2)
        with col15_a:
            sc_limpieza = st.selectbox("Limpieza y mantenimiento", [1, 2, 3, 4, 5], index=2, key="og_sc_limp")
            sc_aire = st.selectbox("Aire acondicionado", [1, 2, 3, 4, 5], index=2, key="og_sc_aire")
            sc_telefonia = st.selectbox("Telefonía", [1, 2, 3, 4, 5], index=2, key="og_sc_tel")
        with col15_b:
            sc_internet = st.selectbox("Internet y datos", [1, 2, 3, 4, 5], index=2, key="og_sc_int")
            sc_impresiones = st.selectbox("Servicio de impresiones", [1, 2, 3, 4, 5], index=2, key="og_sc_imp")
            sc_vigilancia = st.selectbox("Vigilancia y seguridad", [1, 2, 3, 4, 5], index=2, key="og_sc_vig")

        # Pregunta 16: Servicios Generales Zonamerica
        st.markdown("<h4 style='font-size: 20px;'>16. Servicios Generales Zonamerica</h4>", unsafe_allow_html=True)
        st.caption("En una escala del 1 al 5, siendo 1=muy insatisfecho y 5=muy satisfecho, califica el nivel de satisfacción de su empresa en relación a los siguientes servicios que ofrece Zonamerica? (*)")
        col16_a, col16_b = st.columns(2)
        with col16_a:
            gen_proceso = st.selectbox("Proceso de Registro e Ingreso de Funcionarios, Visitantes y Proveedores", [1, 2, 3, 4, 5], index=2, key="og_gen_proc")
            gen_seguridad = st.selectbox("Seguridad en general", [1, 2, 3, 4, 5], index=2, key="og_gen_seg")
            gen_areas = st.selectbox("Áreas comunes de esparcimiento (internas y externas)", [1, 2, 3, 4, 5], index=2, key="og_gen_areas")
        with col16_b:
            gen_alquiler = st.selectbox("Alquiler de espacios y equipos para actividades de cada usuario/cliente", [1, 2, 3, 4, 5], index=2, key="og_gen_alq")
            gen_actividades = st.selectbox("Actividades promovidas por Zonamerica para el bienestar de la comunidad", [1, 2, 3, 4, 5], index=2, key="og_gen_act")
            gen_mantenimiento = st.selectbox("Mantenimiento y limpieza de la infraestructura de Zonamerica", [1, 2, 3, 4, 5], index=2, key="og_gen_mant")

        # Pregunta 17: Necesidades del Personal
        st.markdown("<h4 style='font-size: 20px;'>17. Necesidades del Personal</h4>", unsafe_allow_html=True)
        st.caption("Teniendo en cuenta las necesidades de su personal, por favor califique su Nivel de Satisfacción: (*)")
        col17_a, col17_b = st.columns(2)
        with col17_a:
            pers_restaurante = st.selectbox("Restaurante", [1, 2, 3, 4, 5], index=2, key="og_pers_rest")
            pers_cafe = st.selectbox("Café", [1, 2, 3, 4, 5], index=2, key="og_pers_cafe")
            pers_cajero = st.selectbox("Cajero", [1, 2, 3, 4, 5], index=2, key="og_pers_cajero")
        with col17_b:
            pers_vending = st.selectbox("Vending Machine", [1, 2, 3, 4, 5], index=2, key="og_pers_vend")
            pers_esparcimiento = st.selectbox("Áreas de esparcimiento en general", [1, 2, 3, 4, 5], index=2, key="og_pers_espa")

        st.markdown("---")

        # Pregunta 18: Satisfacción general
        st.markdown("<h4 style='font-size: 20px;'>18. ¿En general, qué tan satisfecho está con Zonamerica? (*)</h4>", unsafe_allow_html=True)
        satisfaccion_general = st.selectbox("Satisfacción general", [1, 2, 3, 4, 5], index=2, key="og_sat_gen", label_visibility="collapsed")

        # Pregunta 19: Sugerencias de Servicios para 2025
        st.markdown("<h4 style='font-size: 20px;'>19. Sugerencias de Servicios para 2025 (*)</h4>", unsafe_allow_html=True)
        st.caption("¿Cuáles nuevos servicios o mejoramientos propondría usted para el 2025?")
        servicios_2025 = st.text_area("Sugerencias 2025", key="og_sug_2025", label_visibility="collapsed")

        # Pregunta 20: Observaciones - Servicios Generales
        st.markdown("<h4 style='font-size: 20px;'>20. Observaciones - Servicios Generales (*)</h4>", unsafe_allow_html=True)
        st.caption("Con respecto a los Servicios Generales, por favor amplíe sus observaciones y/o sugerencias.")
        obs_servicios_gen = st.text_area("Observaciones servicios generales", key="og_obs_serv_gen", label_visibility="collapsed")

        # Pregunta 21: Observaciones - Servicios Contratados
        st.markdown("<h4 style='font-size: 20px;'>21. Observaciones - Servicios Contratados (*)</h4>", unsafe_allow_html=True)
        st.caption("Con respecto a los Servicios Contratados, por favor amplíe sus observaciones y/o sugerencias.")
        obs_servicios_cont = st.text_area("Observaciones servicios contratados", key="og_obs_serv_cont", label_visibility="collapsed")

        # Pregunta 22: Observaciones - Amenities
        st.markdown("<h4 style='font-size: 20px;'>22. Observaciones - Amenities (*)</h4>", unsafe_allow_html=True)
        st.caption("Con respecto a los Amenities y/o empresas de apoyo, por favor amplíe sus observaciones y/o sugerencias.")
        obs_amenities = st.text_area("Observaciones amenities", key="og_obs_amen", label_visibility="collapsed")

        # Pregunta 23: Experiencia emocional
        st.markdown("<h4 style='font-size: 20px;'>23. ¿Cómo se siente acerca de su experiencia general con Zonamerica? (*)</h4>", unsafe_allow_html=True)
        emocion = st.radio(
            "Emoción",
            ["Feliz 😄", "Encantado 🤩", "Neutral 😐", "Decepcionado 😞", "Molesto 😠"],
            horizontal=True,
            key="og_emocion",
            label_visibility="collapsed"
        )

        # Pregunta 24: NPS
        st.markdown("<h4 style='font-size: 20px;'>24. De 1 a 10, ¿Qué tanto recomendaría a sus colegas o amigos Zonamerica? (*)</h4>", unsafe_allow_html=True)
        nps = st.selectbox("NPS", options=range(1, 11), index=8, key="og_nps", label_visibility="collapsed")

        submitted = st.form_submit_button("Enviar Encuesta Obra Gris", type="primary", use_container_width=True)

        if submitted:
            if aceptacion == "No":
                st.error("⚠️ Debe aceptar la política de tratamiento de datos para continuar.")
            elif not razon_social or not nombre_completo:
                st.error("⚠️ Por favor complete la Razón Social y su Nombre.")
            else:
                data_payload = {
                    "aceptacion_politica": aceptacion == "Sí",
                    "razon_social": razon_social,
                    "nombre_completo": nombre_completo,
                    "p4_1_comunicacion": comunicacion_4_1,
                    "p4_2_soporte": comunicacion_4_2,
                    "p5_1_resolucion": fiabilidad_5_1,
                    "p5_2_capacidad": fiabilidad_5_2,
                    "p6_1_satisfecho": capacidad_6_1,
                    "p6_2_capacidad": capacidad_6_2,
                    "p7_1_integridad": confianza_7_1,
                    "p7_2_humano": confianza_7_2,
                    "p8_1_comprende": empatia_8_1,
                    "p8_2_demuestra": empatia_8_2,
                    "p9_1_oficinas": tangibles_9_1,
                    "p9_2_calidad": tangibles_9_2,
                    "p10_tic_tiempo": tic_tiempo,
                    "p10_tic_calidad": tic_calidad,
                    "p10_tic_atencion": tic_atencion,
                    "p11_oper_tiempo": oper_tiempo,
                    "p11_oper_calidad": oper_calidad,
                    "p11_oper_atencion": oper_atencion,
                    "p12_comercial_tiempo": com_tiempo,
                    "p12_comercial_calidad": com_calidad,
                    "p12_comercial_atencion": com_atencion,
                    "p13_admin_tiempo": admin_tiempo,
                    "p13_admin_calidad": admin_calidad,
                    "p13_admin_atencion": admin_atencion,
                    "p14_gci_tiempo": gci_tiempo,
                    "p14_gci_calidad": gci_calidad,
                    "p14_gci_atencion": gci_atencion,
                    "p15_limpieza": sc_limpieza,
                    "p15_aire": sc_aire,
                    "p15_telefonia": sc_telefonia,
                    "p15_internet": sc_internet,
                    "p15_impresiones": sc_impresiones,
                    "p15_vigilancia": sc_vigilancia,
                    "p16_proceso": gen_proceso,
                    "p16_seguridad": gen_seguridad,
                    "p16_areas": gen_areas,
                    "p16_alquiler": gen_alquiler,
                    "p16_actividades": gen_actividades,
                    "p16_mantenimiento": gen_mantenimiento,
                    "p17_restaurante": pers_restaurante,
                    "p17_cafe": pers_cafe,
                    "p17_cajero": pers_cajero,
                    "p17_vending": pers_vending,
                    "p17_esparcimiento": pers_esparcimiento,
                    "p18_satisfaccion_general": satisfaccion_general,
                    "p19_servicios_2025": servicios_2025,
                    "p20_obs_servicios_generales": obs_servicios_gen,
                    "p21_obs_servicios_contratados": obs_servicios_cont,
                    "p22_obs_amenities": obs_amenities,
                    "p23_emocion": emocion,
                    "p24_nps": nps
                }
                guardar_en_supabase(data_payload, "Cuestionario_Obra_Gris")

if __name__ == '__main__':
    show_survey_obra_gris()