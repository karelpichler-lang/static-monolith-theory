import numpy as np

# Konstanty Monolitu
kappa = 7.42e-28  # m/kg
M_sun = 1.98847e30
a_orbit = 5.7909e10
e_orbit = 0.2056

def get_phi(r):
    return np.exp(-(kappa * M_sun) / r)

def calculate_precession():
    dt = 1000  
    r = np.array([a_orbit * (1 + e_orbit), 0.0])
    v = np.array([0.0, np.sqrt(6.674e-11 * M_sun * (1 - e_orbit) / (a_orbit * (1 + e_orbit)))])
    
    min_dist = float('inf')
    angle_at_perihelion = 0
    
    # Simulace jednoho oběhu
    for t in range(0, 8000000, dt):
        dist = np.linalg.norm(r)
        phi = get_phi(dist)
        
        # Gravitační zrychlení upravené kapacitou pletiva
        acc = - (6.674e-11 * M_sun / dist**3) * r
        acc = acc * (1 / phi**3)  # Faktor pnutí 3 pro precesi
        
        v += acc * dt
        r += v * dt
        
        if t > 4000000 and dist < min_dist:
            min_dist = dist
            angle_at_perihelion = np.arctan2(r[1], r[0])
            
    return np.degrees(angle_at_perihelion)

drift_arcsec = calculate_precession() * 3600
century_drift = abs(drift_arcsec) * 415.2

print(f"Predikce precese Merkuru (Monolit): {century_drift:.2f} vteřin/století")
