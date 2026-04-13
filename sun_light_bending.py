import numpy as np

# Konstanty
kappa = 7.42e-28  # m/kg
M_sun = 1.98847e30
R_sun = 6.957e8   # Poloměr Slunce (m)

# Výpočet ohybu světla
# U fotonů se pnutí projevuje faktorem 4 (vliv na čas i prostor rovnoměrně)
def calculate_light_bending():
    # Úhel ohybu v radiánech: alpha = 4 * kappa * M / R
    alpha_rad = (4 * kappa * M_sun) / R_sun
    
    # Převod na úhlové vteřiny
    alpha_arcsec = alpha_rad * (180 / np.pi) * 3600
    return alpha_arcsec

bending = calculate_light_bending()
print(f"Ohyb světla u okraje Slunce: {bending:.4f} úhlových vteřin")
