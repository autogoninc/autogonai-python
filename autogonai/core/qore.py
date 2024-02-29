import requests
import base64
from io import BytesIO


class Vision:
    """Handles vision operations related to Autogon Qore."""

    endpoint = "services/"

    def __init__(self, client: any):
        """Initializes the Production class.

        Args:
            client (any): The client object for making requests.
        """
        self.client = client

    @staticmethod
    def _process_image_to_bytes(img_str: str):
        """
        Processes images to BytesIO objects which can be loaded by the PIL library
        Args:
            img_str (str): The image in base64 format.
        Returns:
            BytesIO: The image in bytes.
        """
        return BytesIO(base64.b64decode(img_str.encode("utf-8")))

    @staticmethod
    def _download_image(img_url: str):
        """
        Downloads image from a url and processes it to bytes
        Args:
            img_url (str): The url of the image to be downloaded.
        Returns:
            BytesIO: The image in bytes.
        """
        response = requests.get(img_url)
        return BytesIO(response.content)

    def text_detection(self, image_url) -> dict:
        """
        Detects text in an image.
        Args:
            image_url (str): The url of the image to be processed.
        Returns:
            dict: The response from the API.
        """
        body = {"image_url": image_url, "operation": "text_detection"}
        response = self.client.send_request(
            self.endpoint + "vision-ai/", json_data=body, method="post"
        )
        return response

    def document_text_detection(self, image_url) -> dict:
        """
        Detects text in a document.
        Args:
            image_url (str): The url of the image to be processed.
        Returns:
            dict: The response from the API.
        """
        body = {"image_url": image_url, "operation": "document_text_detection"}
        response = self.client.send_request(
            self.endpoint + "vision-ai/", form_data=body, method="post"
        )
        return response

    def label_detection(self, image_url) -> dict:
        """
        Detects labels in an image.
        Args:
            image_url (str): The url of the image to be processed.
        Returns:
            dict: The response from the API.
        """
        body = {"image_url": image_url, "operation": "label_detection"}
        response = self.client.send_request(
            self.endpoint + "vision-ai/", form_data=body, method="post"
        )
        return response

    def landmark_detection(self, image_url) -> dict:
        """
        Detects landmarks in an image.
        Args:
            image_url (str): The url of the image to be processed.
        Returns:
            dict: The response from the API.
        """
        body = {"image_url": image_url, "operation": "landmark_detection"}
        response = self.client.send_request(
            self.endpoint + "vision-ai/", form_data=body, method="post"
        )
        return response

    def logo_detection(self, image_url) -> dict:
        """
        Detects logos in an image.
        Args:
            image_url (str): The url of the image to be processed.
        Returns:
            dict: The response from the API.
        """
        body = {"image_url": image_url, "operation": "logo_detection"}
        response = self.client.send_request(
            self.endpoint + "vision-ai/", form_data=body, method="post"
        )
        return response

    def web_detection(self, image_url) -> dict:
        """
        Returns web results for an image, including full matching images and similar images.
        Args:
            image_url (str): The url of the image to be processed.
        Returns:
            dict: The response from the API.
        """
        body = {"image_url": image_url, "operation": "web_detection"}
        response = self.client.send_request(
            self.endpoint + "vision-ai/", form_data=body, method="post"
        )
        return response

    def object_detection_v1(self, image_url) -> dict:
        """
        Detects objects in an image.
        Args:
            image_url (str): The url of the image to be processed.
        Returns:
            dict: The response from the API.
        """
        body = {"image_url": image_url, "operation": "object_detection"}
        response = self.client.send_request(
            self.endpoint + "vision-ai/", form_data=body, method="post"
        )
        return response
    
    def object_detection_v2(self, images: list, confidence_threshold=0.5, overlap_threshold=0.5) -> dict:
        """
        Detects objects in an image.
        Args:
            images (list): The list of image urls to be processed.
            confidence_threshold (float): The minimum confidence threshold for detected objects.
            overlap_threshold (float): The minimum overlap threshold for detected objects.
        Returns:
            dict: The response from the API.
        """
        body = {
            "image_urls": images,
            "confidence_thresh": confidence_threshold,
            "overlap_thresh": overlap_threshold
        }
        response = self.client.send_request(
            self.endpoint + "object-detection/", json_data=body, method="post"
        )
        return response
    
    def license_plate_detection(self, images: list, confidence_threshold=0.5, overlap_threshold=0.5) -> dict:
        """
        Detects license plates in an image.
        Args:
            images (list): The list of image urls to be processed.
            confidence_threshold (float): The minimum confidence threshold for detected objects.
            overlap_threshold (float): The minimum overlap threshold for detected objects.
        Returns:
            dict: The response from the API.
        """
        body = {
            "image_urls": images,
            "confidence_thresh": confidence_threshold,
            "overlap_thresh": overlap_threshold
        }
        response = self.client.send_request(
            self.endpoint + "license-plate-detection/", json_data=body, method="post"
        )
        return response

    def image_generation(self, prompt, output_size) -> dict:
        """
        Generates an image from a prompt.
        Args:
            prompt (str): The prompt for generating the image.
            output_size (str): The size of the output image. e.g. 256x256, 512x512, 1024x1024, etc.
        Returns:
            dict: The response from the API.
        """
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

    def image_captioning(self, image_url) -> dict:
        body = {"image_url": image_url}
        response = self.client.send_request(
            self.endpoint + "image-captioning/", form_data=body, method="post"
        )
        return response

    def document_qa(self, question, document) -> dict:
        """
        This function is used to answer questions based on a document image.
        Args:
            question (str): The question to be answered.
            document (str): The document image to be used for answering the question.
        Returns:
            dict: The response from the API.
        """
        body = {
            "question": question,
            "document": document
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
        """Initializes the Production class.

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

    def text_to_speech(self, text: str, language_code: str) -> dict:
        """
        Generates audio from text.
        Args:
            text (str): The text to be converted to speech.
            language_code (str): The language code of the text. e.g. en-US, en-GB, es-ES, etc.
        Returns:
            dict: The response from the API.
        """
        body = {"text": text, "language_code": language_code}
        response = self.client.send_request(
            self.endpoint + "text-to-speech/", json_data=body, method="post"
        )
        return response

    def speech_to_text(self, audio, language_code) -> dict:
        """
        Converts audio to text.
        Args:
            audio (str): The audio to be converted to text.
            language_code (str): The language code of the audio. e.g. en-US, en-GB, es-ES, etc.
        Returns:
            dict: The response from the API.
        """
        body = {"audio": audio, "language_code": language_code}
        response = self.client.send_request(
            self.endpoint + "speech-to-text/", form_data=body, method="post"
        )
        return response

    def text_summary(self, text, max_length, min_length) -> dict:
        """
        Summarizes text.
        Args:
            text (str): The text to be summarized.
            max_length (int): The maximum length of the summary.
            min_length (int): The minimum length of the summary.
        Returns:
            dict: The response from the API.
        """
        body = {"text": text, "max_length": max_length, "min_length": min_length}
        response = self.client.send_request(
            self.endpoint + "text-summary/", json_data=body, method="post"
        )
        return response

    def ask_your_data(self, dataset_url: str, prompt: str) -> dict:
        """
        This function is used to ask questions and gain insights from your dataset.
        Args:
            dataset_url (str): The url of the dataset to be used for asking questions.
            prompt (str): The prompt for asking questions.
        Returns:
            dict: The response from the API.
        """
        body = {"data": dataset_url, "prompt": prompt}
        response = self.client.send_request(
            self.endpoint + "ask-your-data/", json_data=body, method="post"
        )
        return response

    def llm_chat(self, message) -> dict:
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
    
    def essay_marker(self, question: str, essay: str, answer: str=None, word_length: int=None) -> dict:
        """
        This function is used to mark an essay based on a question and an answer.
        Args:
            question (str): The question to be answered.
            essay (str): The essay to be marked.
            answer (str): The answer to the question. If not provided, the question will be used to mark the essay.
            word_length (int): The word length of the essay. If not provided, the final score will be returned without word length consideration.
        Returns:
            dict: The response from the API.
        """
        body = {"question": question, "essay": essay}
    
        if answer:
            body["answer"] = answer
        if word_length:
            body["word_length"] = word_length

        response = self.client.send_request(
            self.endpoint + "essay-marker/", json_data=body, method="post"
        )
        return response
    
    def job_description_analyzer(self, job_description: str, resume_url: str) -> dict:
        """
        This function is used to analyze a job description and a resume to check for compatibility.
        Args:
            job_description (str): The job description to be analyzed.
            resume_url (str): The url of the resume to be analyzed.
        Returns:
            dict: The response from the API.
        """
        body = {"job_description": job_description, "resume_url": resume_url}
        response = self.client.send_request(
            self.endpoint + "rank-resume/", json_data=body, method="post"
        )
        return response
    
    def employee_analyzer(self, survey: list) -> dict:
        """
        This function is used to analyze employee experience using survey data.
        Args:
            survey (List): The survey data to be analyzed. This is a list of dictionaries with the following structure:
            [
                {
                    "question": "", // survey question
                    "answer": "" // survey answer
                },
                {
                    "question": "", // survey question
                    "answer": "" // survey answer
                }
            ]
        Returns:
            dict: The response from the API.
        """
        body = {
            "question_answers": survey
        }
        response = self.client.send_request(
            self.endpoint + "employee-analysis/", json_data=body, method="post"
        )
        return response
    
    def generate_dataset(self, prompt: str, rows: int) -> dict:
        """
        Generate artificial dataset in csv format from a text prompt given a defined number of rows
        Args:
            prompt (str): This states the type of data to be generated e.g Generate a bank transaction dataset.
            rows (int): This defines the number of rows the dataset would have.
        Returns:
            dict: The response from the API.
        """
        body = {
            "prompt": prompt,
            "rows": rows
        }
        response = self.client.send_request(
            self.endpoint + "generate-data/", json_data=body, method="post"
        )
        return response
    
    def translate_text(self, text: str, target_language: str, source_language: str = None) -> dict:
        """
        Dynamically translate text from one language to another. It supports text translation between two language pairs.
        This service supports a wide variety of languages in language code that conform to ISO-639 (https://en.wikipedia.org/wiki/ISO_639)
        Args:
            text (str): Required. The content of the text to be translated in string format.
            source_language (str): Optional. The ISO-639 language code of the input text if known.
            target_language (str): Required. The ISO-639 language code to use for translation of the input text
        Returns:
            dict: The response from the API.
        """
        if source_language is None:
            request_data = {
                "text": text,
                "target_language": target_language,
            }
        else:
            request_data = {
                "text": text,
                "target_language": target_language,
                "source_language": source_language,
            }
        response = self.client.send_request(
            self.endpoint + "text-translation/", json_data=request_data, method="post"
        )
        return response


class Voice:
    """Handles operations related to Autogon Qore."""

    endpoint = "services/"

    def __init__(self, client: any):
        """Initializes the Production class.

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
    

class Agriculture:
    """Handles agriculture operations related to Autogon Qore."""
    
    endpoint = "services/"

    def __init__(self, client: any):
        """Initializes the Production class.

        Args:
            client (any): The client object for making requests.
        """
        self.client = client

    
    def ripe_strawberry_detection(self, image_urls: list, overlap_threshold: float = 0.5, confidence_threshold: float = 0.3) -> dict:
        """
        Detects ripe strawberries in an image.
        Args:
            image_urls (list): The list of image urls to be processed.
            overlap_threshold (float): The minimum overlap threshold for detected objects.
            confidence_threshold (float): The minimum confidence threshold for detected objects.
        Returns:
            dict: The response from the API.
        """
        body = {
            "study_type": "ripe_strawberry_detection",
            "image_urls": image_urls,
            "overlap_threshold": overlap_threshold,
            "confidence_threshold": confidence_threshold
        }
        response = self.client.send_request(
            self.endpoint + "agro-studies/", json_data=body, method="post"
        )
        return response
    

    def crop_weed_detection(self, image_urls: list, overlap_threshold: float = 0.5, confidence_threshold: float = 0.3) -> dict:
        """
        Detects weeds in a an image and classifies them as crop or weed.
        Args:
            image_urls (list): The list of image urls to be processed.
            overlap_threshold (float): The minimum overlap threshold for detected objects.
            confidence_threshold (float): The minimum confidence threshold for detected objects.
        Returns:
            dict: The response from the API.
        """
        body = {
            "study_type": "crop_weed_detection",
            "image_urls": image_urls,
            "overlap_threshold": overlap_threshold,
            "confidence_threshold": confidence_threshold
        }
        response = self.client.send_request(
            self.endpoint + "agro-studies/", json_data=body, method="post"
        )
        return response
    

    def palm_tree_health_detection(self, image_urls: list, overlap_threshold: float = 0.5, confidence_threshold: float = 0.3) -> dict:
        """
        Detects and classifies the health of palm trees in an image.
        Args:
            image_urls (list): The list of image urls to be processed.
            overlap_threshold (float): The minimum overlap threshold for detected objects.
            confidence_threshold (float): The minimum confidence threshold for detected objects.
        Returns:
            dict: The response from the API.
        """
        body = {
            "study_type": "palm_tree_health_detection",
            "image_urls": image_urls,
            "overlap_threshold": overlap_threshold,
            "confidence_threshold": confidence_threshold
        }
        response = self.client.send_request(
            self.endpoint + "agro-studies/", json_data=body, method="post"
        )
        return response
    

    def cashew_disease_detection(self, image_urls: list, overlap_threshold: float = 0.5, confidence_threshold: float = 0.3) -> dict:
        """
        Detects and classifies diseases in cashew leaves in an image.
        Args:
            image_urls (list): The list of image urls to be processed.
            overlap_threshold (float): The minimum overlap threshold for detected objects.
            confidence_threshold (float): The minimum confidence threshold for detected objects.
        Returns:
            dict: The response from the API.
        """
        body = {
            "study_type": "cashew_disease_detection",
            "image_urls": image_urls,
            "overlap_threshold": overlap_threshold,
            "confidence_threshold": confidence_threshold
        }
        response = self.client.send_request(
            self.endpoint + "agro-studies/", json_data=body, method="post"
        )
        return response
    

    def apple_disease_detection(self, image_urls: list, overlap_threshold: float = 0.5, confidence_threshold: float = 0.3) -> dict:
        """
        Detects and classifies diseases in apple leaves in an image.
        Args:
            image_urls (list): The list of image urls to be processed.
            overlap_threshold (float): The minimum overlap threshold for detected objects.
            confidence_threshold (float): The minimum confidence threshold for detected objects.
        Returns:
            dict: The response from the API.
        """
        body = {
            "study_type": "apple_disease_detection",
            "image_urls": image_urls,
            "overlap_threshold": overlap_threshold,
            "confidence_threshold": confidence_threshold
        }
        response = self.client.send_request(
            self.endpoint + "agro-studies/", json_data=body, method="post"
        )
        return response
    
    def grape_detection(self, image_urls: list, overlap_threshold: float = 0.5, confidence_threshold: float = 0.3) -> dict:
        """
        Detects grapes in an image.
        Args:
            image_urls (list): The list of image urls to be processed.
            overlap_threshold (float): The minimum overlap threshold for detected objects.
            confidence_threshold (float): The minimum confidence threshold for detected objects.
        Returns:
            dict: The response from the API.
        """
        body = {
            "study_type": "grape_detection",
            "image_urls": image_urls,
            "overlap_threshold": overlap_threshold,
            "confidence_threshold": confidence_threshold
        }
        response = self.client.send_request(
            self.endpoint + "agro-studies/", json_data=body, method="post"
        )
        return response
    



class Medical:
    """Handles medical operations related to Autogon Qore."""

    endpoint = "services/"

    def __init__(self, client: any):
        """Initializes the Production class.

        Args:
            client (any): The client object for making requests.
        """
        self.client = client


    def surgical_tools_detection(self, image_urls: list, overlap_threshold: float = 0.5, confidence_threshold: float = 0.3) -> dict:
        """
        Detects surgical tools in an image.
        Args:
            image_urls (list): The list of image urls to be processed.
            overlap_threshold (float): The minimum overlap threshold for detected objects.
            confidence_threshold (float): The minimum confidence threshold for detected objects.
        Returns:
            dict: The response from the API.
        """
        body = {
            "study_type": "surgical_tools_detection",
            "image_urls": image_urls,
            "overlap_threshold": overlap_threshold,
            "confidence_threshold": confidence_threshold
        }
        response = self.client.send_request(
            self.endpoint + "health-studies/", json_data=body, method="post"
        )
        return response
    

    def tuberculosis_detection(self, image_urls: list, overlap_threshold: float = 0.5, confidence_threshold: float = 0.3) -> dict:
        """
        Detects and classifies tuberculosis in an image.
        Args:
            image_urls (list): The list of image urls to be processed.
            overlap_threshold (float): The minimum overlap threshold for detected objects.
            confidence_threshold (float): The minimum confidence threshold for detected objects.
        Returns:
            dict: The response from the API.
        """
        body = {
            "study_type": "tuberculosis_detection",
            "image_urls": image_urls,
            "overlap_threshold": overlap_threshold,
            "confidence_threshold": confidence_threshold
        }
        response = self.client.send_request(
            self.endpoint + "health-studies/", json_data=body, method="post"
        )
        return response
    
    
    def cervical_fracture_detection(self, image_urls: list, overlap_threshold: float = 0.5, confidence_threshold: float = 0.3) -> dict:
        """
        Detects and classifies cervical fractures in an image.
        Args:
            image_urls (list): The list of image urls to be processed.
            overlap_threshold (float): The minimum overlap threshold for detected objects.
            confidence_threshold (float): The minimum confidence threshold for detected objects.
        Returns:
            dict: The response from the API.
        """
        body = {
            "study_type": "cervical_fracture_detection",
            "image_urls": image_urls,
            "overlap_threshold": overlap_threshold,
            "confidence_threshold": confidence_threshold
        }
        response = self.client.send_request(
            self.endpoint + "health-studies/", json_data=body, method="post"
        )
        return response
    

    def chest_xray_detection(self, image_urls: list, overlap_threshold: float = 0.5, confidence_threshold: float = 0.3) -> dict:
        """
        Detects and classifies diseases in chest x-ray images.
        Args:
            image_urls (list): The list of image urls to be processed.
            overlap_threshold (float): The minimum overlap threshold for detected objects.
            confidence_threshold (float): The minimum confidence threshold for detected objects.
        Returns:
            dict: The response from the API.
        """
        body = {
            "study_type": "chest_xray_detection",
            "image_urls": image_urls,
            "overlap_threshold": overlap_threshold,
            "confidence_threshold": confidence_threshold
        }
        response = self.client.send_request(
            self.endpoint + "health-studies/", json_data=body, method="post"
        )
        return response
    

    def kidney_stone_detection(self, image_urls: list, overlap_threshold: float = 0.5, confidence_threshold: float = 0.3) -> dict:
        """
        Detects and classifies kidney stones in an image.
        Args:
            image_urls (list): The list of image urls to be processed.
            overlap_threshold (float): The minimum overlap threshold for detected objects.
            confidence_threshold (float): The minimum confidence threshold for detected objects.
        Returns:
            dict: The response from the API.
        """
        body = {
            "study_type": "kidney_stone_detection",
            "image_urls": image_urls,
            "overlap_threshold": overlap_threshold,
            "confidence_threshold": confidence_threshold
        }
        response = self.client.send_request(
            self.endpoint + "health-studies/", json_data=body, method="post"
        )
        return response
    

    def head_ct_scan_analyzer(self, image_urls: list, overlap_threshold: float = 0.5, confidence_threshold: float = 0.3) -> dict:
        """
        Detects and classifies the presence of tumors in head CT scan images.
        Args:
            image_urls (list): The list of image urls to be processed.
            overlap_threshold (float): The minimum overlap threshold for detected objects.
            confidence_threshold (float): The minimum confidence threshold for detected objects.
        Returns:
            dict: The response from the API.
        """
        body = {
            "study_type": "head_ct_scan",
            "image_urls": image_urls,
            "overlap_threshold": overlap_threshold,
            "confidence_threshold": confidence_threshold
        }
        response = self.client.send_request(
            self.endpoint + "health-studies/", json_data=body, method="post"
        )
        return response