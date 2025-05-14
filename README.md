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

## Prasības

- **Python versija**: 3.7 vai jaunāka
- **Bibliotēkas**:
  - `requests`
  - `beautifulsoup4`

Instalējiet nepieciešamās bibliotēkas ar šādu komandu:
```bash
pip install requests beautifulsoup4
