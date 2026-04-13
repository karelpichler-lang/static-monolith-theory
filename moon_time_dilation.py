import numpy as np

# Konstanty
kappa = 7.42e-28
c = 299792458
M_earth = 5.9722e24
R_earth = 6.371e6
M_moon = 7.342e22
R_moon = 1.7371e6
D_moon_orbit = 384400000
M_sun = 1.98847e30
D_earth_sun = 1.496e11

def get_phi(m, r):
    return np.exp(-(kappa * m) / r)

def calculate_moon_dilation():
    # 1. Pozorovatel na Zemi (povrch, rotace)
    v_earth_rot = 465.1  # m/s (rychlost na rovníku)
    phi_earth_total = get_phi(M_earth, R_earth) * get_phi(M_sun, D_earth_sun)
    gamma_earth = 1 / np.sqrt(1 - (v_earth_rot**2 / c**2))
    rate_earth = phi_earth_total / gamma_earth

    # 2. Hodiny na Měsíci (povrch, oběžná rychlost kolem Země)
    v_moon_orbit = 1022.0 # m/s
    # Měsíc má vlastní dluh + dluh Země v dané vzdálenosti + dluh Slunce
    phi_moon_total = get_phi(M_moon, R_moon) * get_phi(M_earth, D_moon_orbit) * get_phi(M_sun, D_earth_sun)
    gamma_moon = 1 / np.sqrt(1 - (v_moon_orbit**2 / c**2))
    rate_moon = phi_moon_total / gamma_moon

    # Rozdíl v mikrosekundách za den
    ratio = rate_moon / rate_earth
    diff_us_day = (ratio - 1) * 86400 * 1e6
    return diff_us_day

print(f"--- ANALÝZA ČASU NA MĚSÍCI (Statický Monolit) ---")
print(f"Zahrnuta rotace Země i rychlost Měsíce.")
print(f"Časový posun: {calculate_moon_dilation():.2f} mikrosekund / den")
