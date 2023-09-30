class Vision:
    """Handles vision operations related to Autogon Qore."""

    endpoint = "services/"

    def __init__(self, client: any):
        """Initializes the ProductionPipelines class.

        Args:
            client (any): The client object for making requests.
        """
        self.client = client

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

    def text_detection(self, image) -> dict:
        body = {"image": image, "operation": "text_detection"}
        response = self.client.send_request(
            self.endpoint + "vision-ai/", form_data=body, method="post"
        )
        return response
