import requests
import base64
from io import BytesIO


class Vision:
    """Handles vision operations related to Autogon Qore."""

    endpoint = "services/"

    def __init__(self, client: any):
        """Initializes the ProductionPipelines class.

        Args:
            client (any): The client object for making requests.
        """
        self.client = client

    def _process_image_to_bytes(self, img_str: str):
        """Processes images to BytesIO objects which can be loaded by the PIL library"""

        if len(img_str) > 400:
            return BytesIO(base64.b64decode(img_str.encode("utf-8")))
        else:
            response = requests.get(img_str)
            return BytesIO(response.content)

    def text_detection(self, image) -> dict:
        body = {"image": image, "operation": "text_detection"}
        response = self.client.send_request(
            self.endpoint + "vision-ai/", form_data=body, method="post"
        )
        return response

    def document_text_detection(self, image) -> dict:
        body = {"image": image, "operation": "document_text_detection"}
        response = self.client.send_request(
            self.endpoint + "vision-ai/", form_data=body, method="post"
        )
        return response

    def label_detection(self, image) -> dict:
        body = {"image": image, "operation": "label_detection"}
        response = self.client.send_request(
            self.endpoint + "vision-ai/", form_data=body, method="post"
        )
        return response

    def landmark_detection(self, image) -> dict:
        body = {"image": image, "operation": "landmark_detection"}
        response = self.client.send_request(
            self.endpoint + "vision-ai/", form_data=body, method="post"
        )
        return response

    def logo_detection(self, image) -> dict:
        body = {"image": image, "operation": "logo_detection"}
        response = self.client.send_request(
            self.endpoint + "vision-ai/", form_data=body, method="post"
        )
        return response

    def web_detection(self, image) -> dict:
        body = {"image": image, "operation": "web_detection"}
        response = self.client.send_request(
            self.endpoint + "vision-ai/", form_data=body, method="post"
        )
        return response

    def object_detection(self, image) -> dict:
        body = {"image": image, "operation": "object_detection"}
        response = self.client.send_request(
            self.endpoint + "vision-ai/", form_data=body, method="post"
        )
        return response

    def image_generation(self, prompt, output_size) -> dict:
        body = {"prompt": prompt, "output_size": output_size}
        response = self.client.send_request(
            self.endpoint + "image-generation/", form_data=body, method="post"
        )
        response["image"] = self._process_image_to_bytes(response["image"])
        return response

    def stable_diffusion(self, text) -> dict:
        body = {"text": text}
        response = self.client.send_request(
            self.endpoint + "stable-diffusion/", json_data=body, method="post"
        )
        return response

    def image_captioning(self, image, image_url) -> dict:
        body = {"image": image, "image_url": image_url}
        response = self.client.send_request(
            self.endpoint + "image-captioning/", form_data=body, method="post"
        )
        return response

    def document_qa(self, question, document, document_url) -> dict:
        body = {
            "question": question,
            "document": document,
            "document_url": document_url,
        }
        response = self.client.send_request(
            self.endpoint + "document-qa/", form_data=body, method="post"
        )
        return response

    def visual_qa(self, text, image, image_url) -> dict:
        body = {
            "text": text,
            "image": image,
            "image_url": image_url,
        }
        response = self.client.send_request(
            self.endpoint + "viit-vq/", form_data=body, method="post"
        )
        return response


class NaturalLanguage:
    """Handles vision operations related to Autogon Qore."""

    endpoint = "services/"

    def __init__(self, client: any):
        """Initializes the ProductionPipelines class.

        Args:
            client (any): The client object for making requests.
        """
        self.client = client

    def sentiment_analysis(self, text) -> dict:
        body = {"text": text}
        response = self.client.send_request(
            self.endpoint + "sentiment-analysis/", json_data=body, method="post"
        )
        return response

    def text_to_speech(self, text, language_code) -> dict:
        body = {"text": text, "language_code": language_code}
        response = self.client.send_request(
            self.endpoint + "text-to-speech/", json_data=body, method="post"
        )
        return response

    def speech_to_text(self, audio, language_code) -> dict:
        body = {"audio": audio, "language_code": language_code}
        response = self.client.send_request(
            self.endpoint + "speech-to-text/", form_data=body, method="post"
        )
        return response

    def text_summary(self, text, max_length, min_length) -> dict:
        body = {"text": text, "max_length": max_length, "min_length": min_length}
        response = self.client.send_request(
            self.endpoint + "text-summary/", json_data=body, method="post"
        )
        return response

    def ask_your_data(self, data, prompt) -> dict:
        body = {"data": data, "prompt": prompt}
        response = self.client.send_request(
            self.endpoint + "ask-your-data/", json_data=body, method="post"
        )
        return response

    def chatgpt(self, message) -> dict:
        body = {"message": message}
        response = self.client.send_request(
            self.endpoint + "chat/", json_data=body, method="post"
        )
        return response

    def text_classification(self, text) -> dict:
        body = {"text": text}
        response = self.client.send_request(
            self.endpoint + "text-classification/", json_data=body, method="post"
        )
        return response


class Voice:
    """Handles operations related to Autogon Qore."""

    endpoint = "services/"

    def __init__(self, client: any):
        """Initializes the ProductionPipelines class.

        Args:
            client (any): The client object for making requests.
        """
        self.client = client

    def create_voice(self, voice_name, voice_description, audio) -> dict:
        body = {
            "voice_name": voice_name,
            "voice_description": voice_description,
            "audio": audio,
        }
        response = self.client.send_request(
            self.endpoint + "voice-cloning/voices/", form_data=body, method="post"
        )
        return response

    def get_voices(self) -> dict:
        response = self.client.send_request(
            self.endpoint + "voice-cloning/voices/list/", method="get"
        )
        return response

    def text_to_speech(self, voice_id, text) -> dict:
        body = {
            "voice_id": voice_id,
            "text": text,
        }
        response = self.client.send_request(
            self.endpoint + "voice-cloning/tts/", form_data=body, method="post"
        )
        return response
