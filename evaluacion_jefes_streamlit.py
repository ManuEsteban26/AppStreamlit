import streamlit as st
import time
from PIL import Image 
import requests 
from io import BytesIO 


# --- CONFIGURACIÓN INICIAL ---
st.set_page_config(
    page_title="Encuesta de Liderazgo - Motorola Solutions", 
    page_icon="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAADi0lEQVRIia1WPUsrQRSdfRohYpJSsVDR1lIUUVAQI8TGTsRCbBJBg1iYHyBiEwVJimhhk7UxgmKhIkHZKhgsxA8sTDBIFAlENCaZzW52975ifGvYncnzyTtFmL1n7jnZmZ25l8MYIwY4jrNYLDU1NaVSKZVKZTKZYrGIELLZbE1NTW1tbXV1dYqiKIoCACwRhGkQRVHTtI+PD57nnU4nK3dsbCwSiWCMVVUVRZEqRTEol8sY45WVFeafMiEYDEqSJMvy3w0AIBaLfV9ah91uv76+1jStmgEAbGxs/EBdx+7uLgDQDQDA7/ebc2ZnZ1lyc3Nz5iDP85UenwaapkUiEaqKKIosg0KhQI0LgqAoypeBJEkPDw/UqW63GwAGBwfNlNfrBYDu7m5qYjabLZVKnwYA0N/fT513fHwMAFtbW2YqGo0CwObmJjVxamqKLBSSZfn09JQ6CSFULBYBIJVKmSlRFAEgmUyycm9vbyVJQqwVQAg5nU4A0DQNABwORyU1OjqqUywDj8cDACidTrNmhMNhXWV5ebmS2t7e1qmlpSWWQqFQQDs7Oyw6nX7SVS4uLiqp5+dnnYrH4ywFQRCQz+ejci0tLUSCqFQuRWtrK4syIBAI/Lq5uaFyXq9XHxMJj8dDHivPF6HcbjdVJJFIoObmZip3dXWlLwL5PTw8ZFFHR0dUEZfLhSwWC5WDP8jlcmSQz+cNVD6fJwNSJ8wYGhr6Zfj+CBYWFhBCyWSysbHR4XBwHHd/f9/Q0NDX10fWJxaLcRxns9m6urqy2Wx9ff3IyIhZp7a2Fg0PD5sJQRDM90wulwuFQicnJ+bDBQA8z5t1ZmZm0Pz8vJkAAPNN6XK5np6eisWieduCweDr66tZZ3V1FYX5sCE6Pj5eLpfNsxFCd3d3rP0EgI6ODkMwGo2iRCJhiB4cHLCu7snJyZ6eHip1fn4eCAQMwbe3NwQAnZ2dlVFRFKk7Vh2Li4uGvZmYmAAAVC6X9/f39ejAwEC1HqQqDInxeFyWZUTKWXt7O4na7fafqSOErFar1WolY3LdfhYcWZYvLy9/rEtFOp3+qmikqK2vr/8v9b29PVVVKV0FtUv4V/j9fkpXgTEmJZB1e38TgUCA2Rfp71GlBFXH2dmZQZ1igDFWVfXl5WV6evr70j6f7/39Xe+F/mKAMS6VSgDw+Pi4trZmOIaV6O3tDYVCmUwGAFjd9W/hH7T1NboR6gAAAABJRU5ErkJggg==", 
    layout="centered"
)

# --- FUNCIÓN GUARDAR EN SUPABASE ---
def guardar_en_supabase(datos, tabla):
    """
    Guarda los datos de la encuesta en Supabase.
    """
    try:
        from supabase import create_client, Client
        
        url = "https://ekyfwvxmkagwaonrbafk.supabase.co"
        key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVreWZ3dnhta2Fnd2FvbnJiYWZrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ2NjE5MTIsImV4cCI6MjA4MDIzNzkxMn0.VD1QFtqxHAkfp1D_TQj4GUCD8YKzmu14oQMpiOkrDX0"
        
        supabase: Client = create_client(url, key)

        if tabla == "Cuestionario_Motorola":
            supabase_data = {
                "jefe_evaluado": datos.get("jefe_evaluado"),
                "p1_comunicacion_clara": datos.get("p1_comunicacion_clara"),
                "p2_comunicacion_abierta": datos.get("p2_comunicacion_abierta"),
                "p3_retro_frecuente": datos.get("p3_retro_frecuente"),
                "p4_retro_constructiva": datos.get("p4_retro_constructiva"),
                "p5_indicadores_claros": datos.get("p5_indicadores_claros"),
                "p6_indicadores_mejora": datos.get("p6_indicadores_mejora"),
                "p7_admin_facilita": datos.get("p7_admin_facilita"),
                "p8_admin_herramientas": datos.get("p8_admin_herramientas"),
                "p9_trato_respeto": datos.get("p9_trato_respeto"),
                "p10_trato_ambiente": datos.get("p10_trato_ambiente"),
                "p11_desarrollo_oportunidades": datos.get("p11_desarrollo_oportunidades"),
                "p12_desarrollo_aprendizaje": datos.get("p12_desarrollo_aprendizaje"),
                "p13_motivacion_reconocimiento": datos.get("p13_motivacion_reconocimiento"),
                "p14_motivacion_confianza": datos.get("p14_motivacion_confianza"),
                "p15_comentarios_abiertos": datos.get("p15_comentarios_abiertos"),
            }

            with st.spinner("Guardando respuestas..."):
                result = supabase.table(tabla).insert(supabase_data).execute()
            
            if result.data:
                st.success("✅ ¡Datos de la encuesta de Liderazgo guardados exitosamente!")
                st.balloons()
                time.sleep(2)
                
                # IMPORTANTE: Limpiar TODAS las keys relacionadas con el formulario
                keys_to_delete = [
                    'jefe_seleccionado',
                    'p1_q', 'p2_q', 'p3_q', 'p4_q', 'p5_q', 'p6_q', 'p7_q',
                    'p8_q', 'p9_q', 'p10_q', 'p11_q', 'p12_q', 'p13_q', 'p14_q', 'p15_q'
                ]
                
                for key in keys_to_delete:
                    if key in st.session_state:
                        del st.session_state[key]
                
                st.rerun()
                return True
            else:
                st.warning("⚠️ No se pudo confirmar el guardado de los datos.")
                return False
        else:
             st.warning(f"Tabla '{tabla}' no reconocida en la lógica de guardado.")
             return False

    except Exception as e:
        st.error(f"❌ Error al intentar conectar o guardar en Supabase: {e}")
        st.info("Revisa si tienes el paquete 'supabase' instalado y si las credenciales son correctas.")
        with st.expander("Ver datos que se intentaron guardar"):
            st.json(datos)
        return False

# --- FUNCIÓN DE LA ENCUESTA MOTOROLA LIDERAZGO ---
def show_survey_motorola():
    
    # Lista de jefes
    JEFES = [
        "Selecciona un jefe/a...",
        "Juan Pérez - Gerente Comercial", 
        "Ana Rodríguez - Coordinadora de Ventas", 
        "Carlos Gómez - Director Regional", 
        "Laura Martínez - Jefe de Equipo"
    ]
    
    # ---------------------------------------------------------------------------------------
    # ENCABEZADO DE LOGOS Y TÍTULO
    col_logo1, col_titulo, col_logo2 = st.columns([1.5, 5, 1.5])
    
    with col_logo1:
        st.image("https://i.pinimg.com/originals/7e/aa/7d/7eaa7db5ff7e2a11db308974ead0e43c.png") 
    
    with col_titulo:
        st.markdown("<h1 style='text-align: center'>Evaluación de Liderazgo</h1>", unsafe_allow_html=True)

    with col_logo2:
        st.image("https://static.ybox.vn/2024/9/5/1725613931704-logo-adecco.png")
    
    st.markdown("---")
    # ---------------------------------------------------------------------------------------
    
    # Formulario Streamlit
    with st.form("form_motorola"):
        
        # 1. Lista Desplegable de Jefes
        st.markdown("<h3 style='font-size: 20px;'>Selecciona el Líder a Evaluar: (*)</h3>", unsafe_allow_html=True)
        jefe_evaluado = st.selectbox(
            "Líder a Evaluar", 
            options=JEFES, 
            index=0,
            key="jefe_seleccionado",
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Instrucciones de Calificación
        st.markdown("<p style='font-size: 16px;'>Instrucción: Califica del 1 al 5, donde 1 es el nivel Más Bajo y 5 es el nivel Más Alto.</p>", unsafe_allow_html=True)
        st.markdown("---")

        # Opciones de Rating (1-5)
        RATING_OPTIONS = [1, 2, 3, 4, 5]
        
        # --- DIMENSIÓN: COMUNICACIÓN ---
        st.markdown("##### 📢 COMUNICACIÓN")
        
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>Mi líder comunica de manera clara y oportuna información relevante. (*)</span>", unsafe_allow_html=True)
        p1_comunicacion_clara = st.radio("P1", RATING_OPTIONS, index=None, key="p1_q", horizontal=True, label_visibility="collapsed")
        
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>Mi líder promueve espacios para una comunicación abierta y transparente. (*)</span>", unsafe_allow_html=True)
        p2_comunicacion_abierta = st.radio("P2", RATING_OPTIONS, index=None, key="p2_q", horizontal=True, label_visibility="collapsed")
        
        st.markdown("---")
        
        # --- DIMENSIÓN: RETROALIMENTACIÓN ---
        st.markdown("#### 💬 RETROALIMENTACIÓN")
        
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>Mi líder brinda retroalimentación frecuente sobre mi desempeño. (*)</span>", unsafe_allow_html=True)
        p3_retro_frecuente = st.radio("P3", RATING_OPTIONS, index=None, key="p3_q", horizontal=True, label_visibility="collapsed")
        
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>La retroalimentación que recibo es constructiva y me ayuda a mejorar. (*)</span>", unsafe_allow_html=True)
        p4_retro_constructiva = st.radio("P4", RATING_OPTIONS, index=None, key="p4_q", horizontal=True, label_visibility="collapsed")
        
        st.markdown("---")
        
        # --- DIMENSIÓN: INDICADORES ---
        st.markdown("#### 📊 INDICADORES")
        
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>Mi líder explica claramente los indicadores que se usan para medir el desempeño. (*)</span>", unsafe_allow_html=True)
        p5_indicadores_claros = st.radio("P5", RATING_OPTIONS, index=None, key="p5_q", horizontal=True, label_visibility="collapsed")
        
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>Mi líder utiliza los indicadores para mejorar procesos y resultados. (*)</span>", unsafe_allow_html=True)
        p6_indicadores_mejora = st.radio("P6", RATING_OPTIONS, index=None, key="p6_q", horizontal=True, label_visibility="collapsed")
        
        st.markdown("---")
        
        # --- DIMENSIÓN: ADMINISTRATIVO ---
        st.markdown("#### 📋 ADMINISTRATIVO")
        
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>Mi líder facilita la gestión de procesos administrativos. (*)</span>", unsafe_allow_html=True)
        p7_admin_facilita = st.radio("P7", RATING_OPTIONS, index=None, key="p7_q", horizontal=True, label_visibility="collapsed")
        
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>Mi líder conoce y maneja adecuadamente las herramientas administrativas. (*)</span>", unsafe_allow_html=True)
        p8_admin_herramientas = st.radio("P8", RATING_OPTIONS, index=None, key="p8_q", horizontal=True, label_visibility="collapsed")
        
        st.markdown("---")
        
        # --- DIMENSIÓN: TRATO ---
        st.markdown("#### 🤝 TRATO")
        
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>Mi líder me trata con respeto, equidad y empatía. (*)</span>", unsafe_allow_html=True)
        p9_trato_respeto = st.radio("P9", RATING_OPTIONS, index=None, key="p9_q", horizontal=True, label_visibility="collapsed")
        
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>Mi líder promueve un ambiente laboral positivo y colaborativo. (*)</span>", unsafe_allow_html=True)
        p10_trato_ambiente = st.radio("P10", RATING_OPTIONS, index=None, key="p10_q", horizontal=True, label_visibility="collapsed")
        
        st.markdown("---")
        
        # --- DIMENSIÓN: DESARROLLO DEL EQUIPO ---
        st.markdown("#### 🚀 DESARROLLO DEL EQUIPO")
        
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>Mi líder brinda oportunidades para mejorar mis competencias. (*)</span>", unsafe_allow_html=True)
        p11_desarrollo_oportunidades = st.radio("P11", RATING_OPTIONS, index=None, key="p11_q", horizontal=True, label_visibility="collapsed")
        
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>Mi líder fomenta el aprendizaje y crecimiento dentro del equipo. (*)</span>", unsafe_allow_html=True)
        p12_desarrollo_aprendizaje = st.radio("P12", RATING_OPTIONS, index=None, key="p12_q", horizontal=True, label_visibility="collapsed")
        
        st.markdown("---")
        
        # --- DIMENSIÓN: MOTIVACIÓN E INSPIRACIÓN ---
        st.markdown("#### ⭐ MOTIVACIÓN E INSPIRACIÓN")
        
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>Mi líder reconoce los logros y motiva al equipo para alcanzarlos. (*)</span>", unsafe_allow_html=True)
        p13_motivacion_reconocimiento = st.radio("P13", RATING_OPTIONS, index=None, key="p13_q", horizontal=True, label_visibility="collapsed")
        
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>Mi líder inspira confianza y compromiso. (*)</span>", unsafe_allow_html=True)
        p14_motivacion_confianza = st.radio("P14", RATING_OPTIONS, index=None, key="p14_q", horizontal=True, label_visibility="collapsed")
        
        st.markdown("---")
        
        # --- PREGUNTA ABIERTA ---
        st.markdown("#### 💭 PREGUNTA ABIERTA")
        
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>¿Qué aspectos consideras que tu líder podría mejorar?</span>", unsafe_allow_html=True)
        p15_abierta = st.text_area("Comentarios adicionales", key="p15_q", label_visibility="collapsed", height=120)

        st.markdown("---")
        
        submitted = st.form_submit_button("Enviar Encuesta de Liderazgo", type="primary", use_container_width=True)

        if submitted:
            # Validaciones de formulario
            if jefe_evaluado == JEFES[0]:
                st.error("⚠️ Por favor, selecciona el nombre del jefe/a a evaluar.")
            elif any(q is None for q in [p1_comunicacion_clara, p2_comunicacion_abierta, p3_retro_frecuente, 
                                          p4_retro_constructiva, p5_indicadores_claros, p6_indicadores_mejora,
                                          p7_admin_facilita, p8_admin_herramientas, p9_trato_respeto,
                                          p10_trato_ambiente, p11_desarrollo_oportunidades, p12_desarrollo_aprendizaje,
                                          p13_motivacion_reconocimiento, p14_motivacion_confianza]):
                st.error("⚠️ Por favor, responde a todas las preguntas de la encuesta (califica del 1 al 5).")
            else:
                # Payload con los datos de la encuesta
                data_payload = {
                    "jefe_evaluado": jefe_evaluado,
                    "p1_comunicacion_clara": p1_comunicacion_clara,
                    "p2_comunicacion_abierta": p2_comunicacion_abierta,
                    "p3_retro_frecuente": p3_retro_frecuente,
                    "p4_retro_constructiva": p4_retro_constructiva,
                    "p5_indicadores_claros": p5_indicadores_claros,
                    "p6_indicadores_mejora": p6_indicadores_mejora,
                    "p7_admin_facilita": p7_admin_facilita,
                    "p8_admin_herramientas": p8_admin_herramientas,
                    "p9_trato_respeto": p9_trato_respeto,
                    "p10_trato_ambiente": p10_trato_ambiente,
                    "p11_desarrollo_oportunidades": p11_desarrollo_oportunidades,
                    "p12_desarrollo_aprendizaje": p12_desarrollo_aprendizaje,
                    "p13_motivacion_reconocimiento": p13_motivacion_reconocimiento,
                    "p14_motivacion_confianza": p14_motivacion_confianza,
                    "p15_comentarios_abiertos": p15_abierta if p15_abierta else None
                }
                
                # Llamar a la función de guardado
                guardar_en_supabase(data_payload, "Cuestionario_Motorola")
                
# --- NAVEGACIÓN PRINCIPAL (MAIN) ---
def main():
    show_survey_motorola()

# Ejecutar la aplicación
if __name__ == '__main__':
    main()
