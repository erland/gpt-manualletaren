# State- och verktygskontrakt

Samtalets produktkandidater och svar behöver bara finnas under den aktuella dialogen. Ingen persistent state krävs. Lagra aldrig serienummer eller foton permanent i projektet.

Verktyg: generisk `search_web(query)` och `open_source(url)` är **capabilities/hostkrav**, inte deklarerade anropbara MCP-verktyg. En runtime ska mappa dessa mot faktisk, tillgänglig funktion eller redovisa fallback. Ingen obligatorisk MCP-server.
