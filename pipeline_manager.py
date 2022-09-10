import torch
import os
import pathlib

from imagine_pipeline import ImaginePipeline


class PipeLineManager(object):

    def __init__(self, params) -> None:
        super().__init__()
        self.model_id = params["model_id"]
        self.device = params["device"]
        self.auth_token = os.environ["HUGGINGFACE_AUTH_TOKEN"]
        self.pipe = ImaginePipeline.from_pretrained(
            self.model_id,
            revision="fp16",
            torch_dtype=torch.float16,
            use_auth_token=self.auth_token
        ).to(self.device)
        self.out_dir = os.environ["OUT_DIR"]
        pathlib.Path(self.out_dir).mkdir(parents=True, exist_ok=True)

    def prompt(self, params):
        prompt = params["prompt"]
        images = self.pipe(prompt=prompt)["generated"]
