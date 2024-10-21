import logging as log


log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos_persona.log'),
                    log.StreamHandler()
                ])  
   


if __name__ == "__main__":
    log.debug("Mensaje de level debug")
    log.info("Mensaje de level debug")
    log.error("Mensaje de level error")
    log.warning("Mensaje de level warning")
    log.critical("Mensaje de level critical")

