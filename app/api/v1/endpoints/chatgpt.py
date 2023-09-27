import openai
import sys,os, random,math
# Add the parent directory of the current script to the Python path
current_script_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = (current_script_dir.split('\\app'))[0]

sys.path.append(root_dir)


# Now you can import modules from the common package
from app.api.common import load_environment_variables


def get_project_idea(technologies:[str],difficulty:str=''):
    openai.api_key=load_environment_variables.OPENAI_API_KEY
    if not difficulty:
        difficulty_options = ['beginner','intermediate','advanced']
        difficulty=difficulty_options[math.floor(random.random()*3)]
    
    tech =','.join(technologies)

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": "You are a very informative software development project idea provider. Users will just provide the technologies they are interested to get a hands-on experience along with the difficulty level and you will suggest a project and complete set of technologies & tools they will need to use which will include all their aforementioned interested technologies.\nNOTE: keep the descriptions short.\nIf possible give links to existing projects in internet which would match the criteria\n\nThe user inputs are,\ntech: tech1, tech2, tech3, tec.,\ndifficulty: beginner or intermediate or advanced"
        },
        {
        "role": "user",
        "content": "tech: reactJS, polygon blockchain difficulty: beginner"
        },
        {
        "role": "assistant",
        "content": "Project Idea: Decentralized Voting Application\n\nTechnologies:\n1. React JS: JavaScript library for building user interfaces\n\nTools:\n1. Polygon Blockchain: Ethereum layer 2 scaling solution for building decentralized applications (DApps)\n2. Solidity: Programming language for writing smart contracts on the Ethereum network\n3. Truffle: Development framework for Ethereum DApps, providing tools for testing, compiling, and deploying smart contracts\n4. Web3.js: JavaScript library for interacting with Ethereum and Polygon blockchains from within the DApp\n5. Remix IDE: Online development environment for writing, deploying, and testing smart contracts on Ethereum\n6. Metamask: Browser extension for interacting with Ethereum and Polygon networks, providing wallet functionality\n\nDescription:\nBuild a decentralized voting application using React JS and the Polygon blockchain. The application will allow users to vote on various topics securely and transparently. Users will connect their Metamask wallet to the application, which will interact with the Polygon blockchain. Smart contracts written in Solidity will handle the voting process, ensuring fairness and integrity. With a beginner level of difficulty, this project will help you understand the basics of blockchain development and how to integrate it with a web application using React JS."
        },
        {
        "role": "user",
        "content": f"tech:{tech}, difficulty:{difficulty}"
        }
        ],
    temperature=0.7,
    max_tokens=400,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return (response['choices'][0]['message']['content'],difficulty)





if __name__ == "__main__":
    print(get_project_idea(['react JS','python']))