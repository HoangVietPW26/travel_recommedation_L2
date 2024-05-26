from os import environ
from dotenv import dotenv_values

env_values = {
    **dotenv_values(),
    **environ
}

class Configuration:
    
    """
        App configuration.

        Notes: if the variable is required, access using env_values['VARIABLE_NAME']
        to make the runtime error show up sooner, otherwise provide default value using
        env_values.get('VARIABLE_NAME', VALUE)
    """

    APP_HOST = env_values.get("APP_HOST", "0.0.0.0")
    APP_PORT = int(env_values.get("APP_PORT", 3000))
    OPENAI_API_KEY = env_values.get("OPENAI_API_KEY", "")
    OPENAI_MODEL = env_values.get("OPENAI_MODEL", "gpt-3.5-turbo")
