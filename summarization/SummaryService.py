import threading
from queue import Queue
from time import sleep
import requests
from dotenv import load_dotenv
import os
load_dotenv()

summarizedTextStore = ["Summary bla bla bla"]

lock = threading.Lock()


class SummaryService(threading.Thread):
    def __init__(self, transcribedTextQueue: Queue):
        threading.Thread.__init__(self)
        self.transcribedTextQueue = transcribedTextQueue
        self.model_id = 'facebook/bart-large-cnn'
        self.api_token = os.environ["hf_api_token"]

    def summarize(self, payload):
        headers = {"Authorization": f"Bearer {self.api_token}"}
        API_URL = f"https://api-inference.huggingface.co/models/{self.model_id}"
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    def run(self):
        global summarizedTextStore

        while True:
            textBlock = self.transcribedTextQueue.get()
            summary = self.summarize(textBlock)
            with lock:
                summarizedTextStore.append(summary)
            self.transcribedTextQueue.task_done()


def testSummaryService():
    global summarizedTextStore

    transcribedTextQueue = Queue()

    summarizer = SummaryService(transcribedTextQueue=transcribedTextQueue)
    summarizer.start()

    article1 = '''
    It's been six years since that fateful career fair but since then you've learned all sorts of things about circuits, and computer architecture only to find out that very few EE students ever see a circuit diagram ever again past their undergrad. You enjoyed the communications and signals processing aspect so much you decided to go to graduate school and now you are six months into writing a thesis which involves research into Wavelets!

    You've been so busy, you haven't seen your family since your cousins wedding last Spring and have barely talked to anyone outside of your research associates. Your world is filled with fever dreams of L-p function spaces and frequency domains further isolating yourself from society and any long lasting relationship with normal people. You made a point to drive home for Thanksgiving and you can finally catch up with not only your parents and siblings but even some of your extended family!

    Your mom gives you a hug, you all sit down to snack on artichoke dip and she asks, “Tell me about school! What are you researching? Build any killer robots?” the room laughs and waits in anticipation. What do you do?
    '''
    article2 = '''
    It's been seven years since that fateful career fair where you settled on math You took some more math classes in college and you just kept taking more cause you couldn't get away from the stuff. Normal calculus, optimization problems, or numerical algorithms were fun but you truly fell in love with number theory. Something about talking about prime numbers and writing proofs just really got your heart racing all the way to grad school for a PhD specializing in cryptography.

    You've been so busy, you haven't seen your family since your cousins wedding last Spring and have barely talked to anyone outside of your research associates. Your world is filled with fever dreams of the Riemman Hypothesis and quantum computing resistant encryption ideas, further isolating yourself from society and any long lasting relationship with normal people. You made a point to drive home for Thanksgiving and you can finally catch up with not only your parents and siblings but even some of your extended family!

    Your mom gives you a hug, you all sit down to snack on artichoke dip and she asks, “Tell me about school! What are you researching? Solve any cool calculus problems lately?” the room laughs and waits in anticipation. What do you do?
    '''

    transcribedTextQueue.put(article1)
    sleep(8)
    print(summarizedTextStore)
    transcribedTextQueue.put(article2)
    sleep(8)
    print(summarizedTextStore)


if __name__ == "__main__":
    testSummaryService()
