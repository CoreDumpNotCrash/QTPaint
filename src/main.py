from core import logger, config

def main():
    logger.log(f"Starting {config.APP_NAME} v{config.APP_VERSION}")
    print("Hello, World!")
    logger.log(f"Finishing {config.APP_NAME} v{config.APP_VERSION}")

if __name__ == "__main__":
    main()