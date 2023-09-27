import openai
import sys,os
# Add the parent directory of the current script to the Python path
current_script_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = (current_script_dir.split('\\app'))[0]

sys.path.append(root_dir)


# Now you can import modules from the common package
from app.api.common import load_environment_variables


def list_all_gpt_models():
    openai.api_key = load_environment_variables.OPENAI_API_KEY
    print(openai.Model.list())





if __name__ == "__main__":
    list_all_gpt_models()