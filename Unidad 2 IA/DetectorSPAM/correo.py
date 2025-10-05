class correo:
    def __init__(self,remitente,asunto,contenido,link,adjunto,spam_real):
        self.remitente=remitente
        self.asunto=asunto
        self.contenido=contenido
        self.link=link
        self.adjunto=adjunto
        self.spam_real=spam_real
        self.spam=""

    
    ##Regla 1.- Activadores de palabras clave:
    ##Si el asunto o contenido o la direccion del remitente contiene palabras relacionadas con promociones, premios,
    ##urgencias, recompensas, dar clic,ectc.., se suma 1 punto a la probabilidad de spam por cada palabra sospechosa.
    ##Regla 2.- Reputacion del remitente:
    ##Si el dominio del link del correo o de la direccion del remitente esta en la lista de dominios sospechosos,
    ## se suman 2 puntos a la probabilidad de spam.
    ##Regla 3.- Archivos riesgosos:
    ##Si el archivo adjunto es un ejecutable o contenido comprimido se considera 
    ##riesgoso y por lo tanto se suman 3 puntos a la probabilidad de spam.

    ##Al final si el correo sumo por lo menos 3 puntos, se considerara "Spam",
    ## en caso contrario sera considerado "Legítimo" 
    def comprobar_spam(self):
        palabras_sus=["premio","felicitaciones","gan","seleccion","selección","recibir","regalo",
                      "gratis","oferta","exclusiv","descuento","milagro","pierde","infectad",
                      "bloque","clic","registr","invit","juegue","jugar","compra","problema","recib",
                      "sospechos","costo","bajo","promo","rapido","rápido","agota","accede","descarg",
                      "facil","fácil","prestamo","préstamo","hoy","vence","esfuerzo","segur","cripto","duplica",
                      "virus","dinero","millonari","loteria","cancel","actuali"]
        dominios_sus=[".io",".biz",".tk",".ru",".org",".net"]
        adjunto_sus=[".exe",".src",".bat",".zip",".js"]
        puntuacion=0
        for palabra in palabras_sus:
            if palabra in self.asunto.lower():
                puntuacion+=1
            if palabra in self.contenido.lower():
                puntuacion+=1
            if palabra in self.remitente.lower():
                puntuacion+=1 
        for dominio in dominios_sus:
            if dominio in self.remitente.lower():
                puntuacion+=2
            if dominio in self.link.lower():
                puntuacion+=2
        
        for adjunto in adjunto_sus:
            if adjunto in self.adjunto.lower():
                puntuacion+=3
        
        if puntuacion>=3:
            self.spam="Spam"
        else:
            self.spam="Legítimo"
    
    def __str__(self):
        return f"{self.remitente}|{self.asunto}|{self.contenido}|{self.link}|{self.adjunto}|{self.spam_real}|{self.spam}"