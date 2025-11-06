#Este modulo contiene la base de conocimiento para el Sistema Experto de diagnostico.

catalogo_Enfermedades = [
    {
        "nombre": "Gripe",
        "sintomas": ["Fiebre", "Dolor de garganta", "Tos", "Congestión nasal", "Fatiga leve", "Dolor de cabeza", "Dolor muscular", "Pérdida de apetito", "Sudoración leve", "Escalofríos", "Náuseas", "Vómito", "Diarrea", "Estornudos", "Irritación ocular"],
       "recomendacion": "Tu cuerpo está luchando contra una infección y necesita toda la energía posible. Duerme lo suficiente y evita las actividades físicas intensas. Quedarte en casa no solo te ayuda a recuperarte, sino que también previene que contagies a otros.\nLa fiebre puede causar deshidratación. Bebe abundantes líquidos como agua, tés de hierbas tibios, caldos o jugos naturales. Una buena hidratación ayuda a aliviar el dolor de garganta y a fluidificar la mucosidad."


    },
    {
        "nombre": "Influenza",
        "sintomas": ["Fiebre", "Dolor de garganta", "Tos seca", "Congestión nasal", "Fatiga alta", "Dolor de cabeza", "Dolor de pecho", "Dolor muscular", "Dolor en las articulaciones", "Dificultad para respirar", "Escalofríos", "Mareos", "Dolor ocular", "Dolor detrás de los ojos", "Irritación ocular"],
        "recomendacion":"La influenza agota las defensas de tu cuerpo. El descanso no es solo una recomendación, es una necesidad. Quédate en casa, evita cualquier tipo de esfuerzo y duerme todo lo que tu cuerpo te pida. Esto es fundamental para que tu sistema inmunitario pueda combatir el virus eficazmente.\n\nLa fiebre alta, un síntoma común de la influenza, puede deshidratarte rápidamente. Es vital que bebas líquidos de manera constante a lo largo del día. Prioriza el agua, los tés calientes (como el de jengibre o manzanilla), caldos nutritivos y sueros de rehidratación oral si es necesario.\n\nA diferencia de un resfriado, para la influenza existen medicamentos antivirales recetados. Es muy importante que consultes a un médico lo antes posible, idealmente dentro de las primeras 48 horas desde el inicio de los síntomas. Si el médico lo considera adecuado, un tratamiento antiviral puede reducir la duración y la severidad de la enfermedad, así como el riesgo de complicaciones."
    

    },
    {
        "nombre": "Covid 19",
        "sintomas": ["Fiebre", "Dolor de garganta", "Tos", "Tos persistente", "Congestión nasal", "Fatiga leve", "Dolor de cabeza", "Pérdida de apetito", "Pérdida de olfato", "Pérdida de gusto", "Dificultad para respirar", "Escalofríos", "Mareos", "Náuseas", "Vómito", "Diarrea"],
        "recomendacion":" Duerme lo suficiente y descansa el cuerpo, consume alimentos saludables y bebe muchos líquidos ademas de  hablar con amigos y familiares a través de videollamadas o llamadas telefónicas porque es importante aislarte para no contagiar a otros y contactar a tus seres queridos por medios virtuales para no sentirte solo"
    },
    {
        "nombre": "Neumonia",
        "sintomas": ["Fiebre","Tos","Tos persistente", "Congestión nasal", "Fatiga leve", "Dolor de cabeza", "Dolor de pecho", "Dolor muscular", "Pérdida de apetito", "Dificultad para respirar", "Sudoración leve", "Escalofríos", "Náuseas", "Vómito", "Diarrea", "Dolor abdominal"],
        "recomendacion":"Los cuidados para la neumonía incluyen descansar mucho, beber abundantes líquidos, tomar los medicamentos recetados por el médico (como antibióticos y analgésicos) y seguir una dieta saludable. También es importante evitar fumar y el humo de segunda mano, así como lavarse las manos frecuentemente para prevenir la propagación"
    },
    {
        "nombre": "Faringitis",
        "sintomas": ["Fiebre", "Dolor de garganta", "Tos", "Congestión nasal" , "Fatiga leve", "Fatiga alta", "Dolor de cabeza", "Dolor muscular", "Dolor en las articulaciones", "Pérdida de apetito", "Escalofríos", "Náuseas", "Vómito", "Estornudos", "Sarpullido"],
        "recomendacion":"Para aliviar la faringitis, se recomienda hacer gárgaras con agua tibia y sal, chupar caramelos o pastillas para la garganta y mantenerse bien hidratado con líquidos tibios o fríos. También es útil utilizar un humidificador, evitar irritantes como el humo y descansar lo suficiente. Si los síntomas persisten o son severos, es importante consultar a un médico, ya que podría requerir antibióticos si es de origen bacteriano"

    },
    {
        "nombre":"Tuberculosis",
        "sintomas": ["Fiebre", "Tos","Tos seca", "Tos persistente", "Fatiga leve", "Fatiga alta", "Dolor de cabeza", "Dolor de pecho", "Dolor muscular", "Dolor en las articulaciones", "Pérdida de apetito", "Dificultad para respirar", "Sudoración excesiva", "Escalofríos"],
        "recomendacion":"Los cuidados de la tuberculosis incluyen completar el tratamiento médico prescrito, mantener una buena higiene personal y respiratoria (cubrirse al toser), ventilar los espacios, y evitar el contacto estrecho con otras personas hasta que el médico lo autorice. Es crucial tomar todos los medicamentos exactamente como se lo indicaron y no suspender el tratamiento prematuramente"
    },
    {
         "nombre":"Cancer (de pulmon)",
         "sintomas": ["Fiebre", "Tos", "Tos persistente", "Fatiga alta", "Dolor de cabeza", "Dolor de pecho", "Dolor muscular", "Dolor en las articulaciones", "Pérdida de apetito", "Dificultad para respirar"],
         "recomendacion":"Mantenerse hidratado, seguir una dieta nutritiva y blanda, y cuidar la salud pulmonar a través de ejercicios de respiración. También es importante protegerse de infecciones, buscar apoyo emocional en familiares y amigos, y comunicarse abiertamente con un equipo médico sobre los síntomas y efectos secundarios para ajustar el tratamiento"
    }
]

