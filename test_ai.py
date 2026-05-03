import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargamos las variables del archivo .env
load_dotenv()

# Inicializamos el cliente de OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generar_post_linkedin(tema):
    prompt = f"""
    Actúa como un experto en estrategia de procesos con 30 años de experiencia.
    Tengo 58 años y me estoy especializando en automatización con IA.
    Escribe un post corto para LinkedIn sobre: {tema}.
    El tono debe ser maduro, profesional y directo. 
    Evita palabras exageradas como 'revolucionario' o 'increíble'.
    Céntrate en el valor de negocio y la eficiencia.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    mi_tema = "Por qué la experiencia de gestión es vital antes de automatizar con IA"
    resultado = generar_post_linkedin(mi_tema)
    print("\n--- BORRADOR PARA LINKEDIN ---\n")
    print(resultado)