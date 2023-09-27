import openai
from .api.common.load_environment_variables import OPENAI_API_KEY


def list_all_gpt_models():
    openai.api_key = OPENAI_API_KEY
    openai.Model.list()




if __name__ == "__main__":
    list_all_gpt_models()