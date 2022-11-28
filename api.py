import requests
from dotenv import load_dotenv
import os
load_dotenv()
API_TOKEN = os.environ["hf_api_token"]


def query(payload, model_id, api_token):
    headers = {"Authorization": f"Bearer {api_token}"}
    API_URL = f"https://api-inference.huggingface.co/models/{model_id}"
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


if __name__ == "__main__":
    model_id = "facebook/bart-large-cnn"
    article = '''
    It's been six years since that fateful career fair but since then you've learned all sorts of things about circuits, and computer architecture only to find out that very few EE students ever see a circuit diagram ever again past their undergrad. You enjoyed the communications and signals processing aspect so much you decided to go to graduate school and now you are six months into writing a thesis which involves research into Wavelets!

    You've been so busy, you haven't seen your family since your cousins wedding last Spring and have barely talked to anyone outside of your research associates. Your world is filled with fever dreams of L-p function spaces and frequency domains further isolating yourself from society and any long lasting relationship with normal people. You made a point to drive home for Thanksgiving and you can finally catch up with not only your parents and siblings but even some of your extended family!

    Your mom gives you a hug, you all sit down to snack on artichoke dip and she asks, “Tell me about school! What are you researching? Build any killer robots?” the room laughs and waits in anticipation. What do you do?
    '''
    data = query(payload=article, model_id=model_id, api_token=API_TOKEN)
    print(data)
