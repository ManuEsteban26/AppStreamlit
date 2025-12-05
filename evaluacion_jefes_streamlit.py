import streamlit as st
import time
from PIL import Image 
import requests 
from io import BytesIO 

# --- CONFIGURACIÓN INICIAL ---
st.set_page_config(
    page_title="Encuesta de Liderazgo - Motorola Solutions", 
    page_icon="⭐", 
    layout="centered"
)

# --- FUNCIÓN GUARDAR EN SUPABASE ---
def guardar_en_supabase(datos, tabla):
    """
    Guarda los datos de la encuesta en Supabase.
    """
    try:
        # Importar el cliente de Supabase (se asume que está configurado)
        from supabase import create_client, Client
        
        # **REEMPLAZA ESTAS VARIABLES CON TUS CREDENCIALES REALES DE SUPABASE**
        url = "https://ekyfwvxmkagwaonrbafk.supabase.co" # Reemplaza con tu URL
        key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVreWZ3dnhta2Fnd2FvbnJiYWZrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ2NjE5MTIsImV4cCI6MjA4MDIzNzkxMn0.VD1QFtqxHAkfp1D_TQj4GUCD8YKzmu14oQMpiOkrDX0" # Reemplaza con tu Service Key
        
        supabase: Client = create_client(url, key)

        # --- LÓGICA DE GUARDADO ESPECÍFICA PARA MOTOROLA ---
        if tabla == "Cuestionario_Motorola":
            supabase_data = {
                "jefe_evaluado": datos.get("jefe_evaluado"),
                "p1_frecuencia_acompañamiento": datos.get("p1_frecuencia_acompañamiento"),
                "p2_calidad_feedback": datos.get("p2_calidad_feedback"),
                "p3_sentimiento_escucha": datos.get("p3_sentimiento_escucha"),
                "p4_comunicacion_objetivos": datos.get("p4_comunicacion_objetivos"),
                "p5_disposicion_apoyo": datos.get("p5_disposicion_apoyo"),
                "p6_reconocimiento_logros": datos.get("p6_reconocimiento_logros"),
                "p7_ambiente_colaborativo": datos.get("p7_ambiente_colaborativo"),
                "p8_efectividad_liderazgo": datos.get("p8_efectividad_liderazgo"),
            }
            
            with st.spinner("Guardando respuestas..."):
                result = supabase.table(tabla).insert(supabase_data).execute()
            
            if result.data:
                st.success("✅ ¡Datos de la encuesta de Liderazgo guardados exitosamente!")
                if 'jefe_seleccionado' in st.session_state:
                    del st.session_state['jefe_seleccionado']
                st.balloons()
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
    
    # LADO IZQUIERDO: LOGO MOTOROLA
    with col_logo1:
        # Uso de raw string (r"...") para la ruta de Windows
        st.image("https://i.pinimg.com/originals/7e/aa/7d/7eaa7db5ff7e2a11db308974ead0e43c.png") 
        # Se eliminaron los placeholders
    
    # CENTRO: TÍTULO PRINCIPAL
    with col_titulo:
        st.markdown("<h1 style='text-align: center; color: white;'>Evaluación de Liderazgo</h1>", unsafe_allow_html=True)

    # LADO DERECHO: LOGO ADECCO
    with col_logo2:
        # Se eliminaron los placeholders
        st.image("https://static.ybox.vn/2024/9/5/1725613931704-logo-adecco.png")
    
    st.markdown("---")
    # ---------------------------------------------------------------------------------------
    
    # Formulario Streamlit
    with st.form("form_motorola"):
        
        # 1. Lista Desplegable de Jefes
        st.markdown("<h3 style='font-size: 20px;'>Selecciona el Lider a Evaluar: (*)</h3>", unsafe_allow_html=True)
        jefe_evaluado = st.selectbox(
            "Lider a Evaluar", 
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
        
        # --- PREGUNTAS DE LA ENCUESTA (8) ---
        
        st.markdown("### **Preguntas de Evaluación**")
        
        # P1 - CAMBIO: Tamaño de fuente ajustado a 18px
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>1. ¿Con qué frecuencia tu líder te acompaña a campo o en tus actividades comerciales para observar y retroalimentar tu gestión? (*)</span>", unsafe_allow_html=True)
        p1 = st.radio("P1", RATING_OPTIONS, index=None, key="p1_q", horizontal=True, label_visibility="collapsed")
        
        # P2 - CAMBIO: Tamaño de fuente ajustado a 18px
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>2. ¿Cómo calificarías la calidad del feedback que recibes por parte de tu líder (específico, constructivo y enfocado en mejorar tu desempeño)? (*)</span>", unsafe_allow_html=True)
        p2 = st.radio("P2", RATING_OPTIONS, index=None, key="p2_q", horizontal=True, label_visibility="collapsed")
        
        # P3 - CAMBIO: Tamaño de fuente ajustado a 18px
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>3. ¿Te sientes escuchado(a) y comprendido(a) por tu líder cuando compartes ideas, inquietudes o necesidades relacionadas con tu trabajo? (*)</span>", unsafe_allow_html=True)
        p3 = st.radio("P3", RATING_OPTIONS, index=None, key="p3_q", horizontal=True, label_visibility="collapsed")
        
        # P4 - CAMBIO: Tamaño de fuente ajustado a 18px
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>4. ¿Tu líder comunica de manera clara y oportuna los objetivos, estrategias, incentivos y/o cambios relevantes para tu punto de venta? (*)</span>", unsafe_allow_html=True)
        p4 = st.radio("P4", RATING_OPTIONS, index=None, key="p4_q", horizontal=True, label_visibility="collapsed")
        
        # P5 - CAMBIO: Tamaño de fuente ajustado a 18px
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>5. ¿Cómo evalúas la disposición de tu líder para apoyarte en la resolución de problemas o situaciones difíciles en Pdv o procesos internos? (*)</span>", unsafe_allow_html=True)
        p5 = st.radio("P5", RATING_OPTIONS, index=None, key="p5_q", horizontal=True, label_visibility="collapsed")
        
        # P6 - CAMBIO: Tamaño de fuente ajustado a 18px
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>6. ¿Sientes que tu líder reconoce y valora tus logros y esfuerzos en el rol comercial? (*)</span>", unsafe_allow_html=True)
        p6 = st.radio("P6", RATING_OPTIONS, index=None, key="p6_q", horizontal=True, label_visibility="collapsed")
        
        # P7 - CAMBIO: Tamaño de fuente ajustado a 18px
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>7. ¿Tu líder promueve un ambiente de trabajo colaborativo, motivador y orientado al cumplimiento de resultados? (*)</span>", unsafe_allow_html=True)
        p7 = st.radio("P7", RATING_OPTIONS, index=None, key="p7_q", horizontal=True, label_visibility="collapsed")
        
        # P8 - CAMBIO: Tamaño de fuente ajustado a 18px
        st.markdown("<span style='font-size: 18px; font-weight: bold;'>8. ¿Qué tan efectivo consideras el liderazgo de tu jefe para impulsar el cumplimiento de las metas del equipo de ventas? (*)</span>", unsafe_allow_html=True)
        p8 = st.radio("P8", RATING_OPTIONS, index=None, key="p8_q", horizontal=True, label_visibility="collapsed")

        st.markdown("---")
        
        submitted = st.form_submit_button("Enviar Encuesta de Liderazgo", type="primary", use_container_width=True)

        if submitted:
            # Validaciones de formulario
            if jefe_evaluado == JEFES[0]:
                st.error("⚠️ Por favor, selecciona el nombre del jefe/a a evaluar.")
            elif any(q is None for q in [p1, p2, p3, p4, p5, p6, p7, p8]):
                st.error("⚠️ Por favor, responde a todas las preguntas de la encuesta (califica del 1 al 5).")
            else:
                # Payload con los datos de la encuesta
                data_payload = {
                    "jefe_evaluado": jefe_evaluado,
                    "p1_frecuencia_acompañamiento": p1,
                    "p2_calidad_feedback": p2,
                    "p3_sentimiento_escucha": p3,
                    "p4_comunicacion_objetivos": p4,
                    "p5_disposicion_apoyo": p5,
                    "p6_reconocimiento_logros": p6,
                    "p7_ambiente_colaborativo": p7,
                    "p8_efectividad_liderazgo": p8,
                }
                
                # Llamar a la función de guardado
                guardar_en_supabase(data_payload, "Cuestionario_Motorola")

# --- NAVEGACIÓN PRINCIPAL (MAIN) ---
def main():
    show_survey_motorola()

# Ejecutar la aplicación
if __name__ == '__main__':
    main()  