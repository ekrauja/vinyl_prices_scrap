# Vinila Plašu Informācijas Iegūšanas Skripts

Šis Python skripts ir paredzēts, lai iegūtu informāciju par vinila platēm no konkrētas tīmekļa vietnes. Tas izmanto tīmekļa skrāpēšanas tehniku, lai iegūtu informāciju par māksliniekiem, albumiem, cenām, formātiem un pieejamību.

## Funkcionalitāte

- **Informācijas iegūšana par vinila platēm**:
  - Mākslinieka vārds
  - Albuma nosaukums
  - Cena (eiro)
  - Formāts (piemēram, "Vinyl")
  - Pieejamība (piemēram, "Ir veikalā" vai "Pārdots")
- **Datu glabāšana**:
  - Visa iegūtā informācija tiek saglabāta sarakstā `self.products_info_list`.

- **Kā lietot**:
  - 1. Izveidojiet klases instanci
    Izmantojiet `Product` klasi, lai iegūtu informāciju par vinila platēm.
  - 2. Izsauciet `getVinylInfo` metodi
    Nododiet mākslinieka vārdu kā argumentu, lai iegūtu informāciju par konkrētā mākslinieka albumiem.
  - 3. Piekļūstiet datiem
    Iegūtā informācija tiks saglabāta `self.products_info_list`.

- **Datu Struktūra**
  Iegūtā informācija tiek saglabāta kā saraksts (self.products_info_list), kur katrs elements ir vārdnīca ar šādiem laukiem:

  artist: Mākslinieka vārds
  title: Albuma nosaukums
  price: Cena eiro
  format: Formāts (piemēram, "Vinyl")
  availability: Pieejamība (piemēram, "Ir veikalā" vai "Pārdots")

## Prasības

- **Python versija**: 3.7 vai jaunāka
- **Bibliotēkas**:
  - `requests`
  - `beautifulsoup4`

Instalējiet nepieciešamās bibliotēkas ar šādu komandu:
```bash
pip install requests beautifulsoup4
