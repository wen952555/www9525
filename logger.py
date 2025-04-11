import logging

logging.basicConfig(level=logging.INFO, filename="vpn_service.log",
                    format="%(asctime)s - %(levelname)s - %(message)s")

def log_event(event: str):
    logging.info(event)