# app/agents/routing_agent.py
import math

def haversine_distance(lat1, lon1, lat2, lon2):
    """Compute great-circle distance between two points in km."""
    R = 6371  # Earth radius in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat/2)**2 +
         math.cos(math.radians(lat1)) *
         math.cos(math.radians(lat2)) *
         math.sin(dlon/2)**2)
    c = 2 * math.asin(math.sqrt(a))
    return R * c

def compute_route(asset, incident):
    """
    Compute distance & ETA (km & minutes).
    asset: dict with 'location': {'lat','lon'}
    incident: dict with 'location': {'lat','lon'}
    """
    dist_km = haversine_distance(
        asset['location']['lat'], asset['location']['lon'],
        incident['location']['lat'], incident['location']['lon']
    )
    avg_speed_kmph = 40  # assume avg rescue vehicle speed
    eta_min = int((dist_km / avg_speed_kmph) * 60)
    return {"distance_km": round(dist_km, 2), "eta_min": eta_min}
