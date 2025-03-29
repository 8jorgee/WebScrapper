
Recolección de Datos con Selenium y BeautifulSoup:
Usamos Selenium para cargar la página web (se necesita un navegador y un chromedriver para interactuar con la página).
BeautifulSoup procesa el HTML y extrae los títulos de los artículos y sus enlaces.

Simulación de Ataque de Phishing:
Generamos una lista de enlaces falsificados para sitios web. En este ejemplo, solo modificamos el esquema https:// a https://fake-, lo que hace que los enlaces parezcan de sitios falsos, pero en un ataque real se usarían dominios muy parecidos a los originales.

Ataque de Ingeniería Social:
A partir de los artículos recogidos, se selecciona uno aleatoriamente y se crea un mensaje de phishing diseñado para engañar al usuario a que haga clic en el enlace falso. Este mensaje imita las notificaciones o correos electrónicos comunes que uno podría recibir.

¿Qué hace este código?
Recolección de Datos: Recopila artículos (en este caso, títulos de noticias) desde una página web (como Hacker News).
Generación de Enlaces Falsificados: Utiliza los datos para crear enlaces falsos, imitando lo que podría ser un ataque de phishing.
Simulación de un Mensaje de Phishing: Crea un mensaje de phishing que podría ser enviado a una víctima, engañándola para que haga clic en un enlace falso.
