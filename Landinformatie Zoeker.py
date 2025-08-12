import requests

# Basis URL API
base_url = "https://restcountries.com/v3.1/"

# Functie om data op te halen + succesvol (get) statuscode_gegevens ophalen
def data_ophalen(endpoint):
    response = requests.get(base_url + endpoint)
    if response.status_code == 200:
        return response.json()[0]
    else:
        return None

# Keuzemenu: Opties tonen voor gebruikers
while True:
    print("\nWelkom bij de Landinformatie Zoeker!")
    print("\n1. De hoofdstad opzoeken via de landnaam.")
    print("2. Het land opzoeken via de hoofdstad.")
    print("3. De taal/talen opzoeken via de landnaam.")
    print("4. De valuta opzoeken via de landnaam.")
    print("5. Stoppen/Afsluiten.")

    keuze = input("\nMaak een keuze uit 1 t/m 5.: ")

# Keuze-opties coderen + weergeven foutstatus bij geen data

# Input land_output hoofdstad
    if keuze == "1":
        land = input("Voer de naam (voorkeur Engels) van het land in.: ")
        data = data_ophalen(f"name/{land}")
        if data and "capital" in data:
            print("De hoofdstad is:", data["capital"][0])
        else:
            print("Fout: er zijn geen gegevens gevonden.")

# Input hoofdstad_output land
    elif keuze == "2":
        hoofdstad = input("Voer de naam (voorkeur Engels) van de hoofdstad in.: ")
        data = data_ophalen(f"capital/{hoofdstad}")
        if data and "name" in data:
            print("De hoofdstad hoort bij:", data["name"]["common"])
        else:
            print("Fout: er zijn geen gegevens gevonden.")

# Input land_output taal
    elif keuze == "3":
        land = input("Voer de naam (voorkeur Engels) van het land in.: ")
        data = data_ophalen(f"name/{land}")
        if data and "languages" in data:
            talen = ", ".join(data["languages"].values())
            print("De gesproken taal/talen in dit land is/zijn:", talen)
        else:
            print("Fout: land/taal niet gevonden.")

# Input land_output valuta
    elif keuze == "4":
        land = input("Voer de naam (voorkeur Engels) van het land in.: ")
        data = data_ophalen(f"name/{land}?fields=name,currencies")
        if data and "currencies" in data:
            valuta_naam = [valuta_info["name"] for valuta_info in data["currencies"].values()]
            print("De valuta van dit land is:", ", ".join(valuta_naam))
        else:
            print("Fout: geen land/valuta-informatie gevonden.")

# Applicatie stopen en afsluiten
    elif keuze == "5":
        print("Programma beëindigd. Tot kijk!")
        break

# Als menu input niet is 1 t/m 5
    else:
        print("Fout: ongeldige keuze, probeer het opnieuw.")