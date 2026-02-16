from fastapi import FastAPI, Request, Query, Body
from engine.synthesizer import DataSynthesizer

app = FastAPI(title="Universal Mock Data API")

# Initialize the synthesizer
synth = DataSynthesizer()

# --- ENDPOINT 1: Simple GET (Browser-friendly) ---
@app.get("/generate")
async def generate_data(
    request: Request, 
    count: int = Query(1, le=100), 
    seed: int = None,
    locale: str = "en_US"
):
    global synth
    synth = DataSynthesizer(locale=locale)

    # Capture query params (e.g. ?name=name&age=random_int)
    query_params = dict(request.query_params)
    
    # Filter out our control params (count, seed, locale)
    schema = {k: v for k, v in query_params.items() if k not in ["count", "seed", "locale"]}
    
    data = synth.generate(schema, count, seed)
    
    return {
        "metadata": {"count": len(data), "seed": seed, "locale": locale},
        "data": data
    }

# --- ENDPOINT 2: Advanced POST (For Nested JSON) ---
@app.post("/generate")
async def generate_complex(
    template: dict = Body(...), # Accepts the full JSON structure
    count: int = Query(1, le=100),
    seed: int = None,
    locale: str = "en_US"
):
    global synth
    synth = DataSynthesizer(locale=locale)
    
    # Use the recursive generation logic
    data = synth.generate(template, count, seed)
    
    return {
        "metadata": {"count": count, "seed": seed, "locale": locale},
        "data": data
    }