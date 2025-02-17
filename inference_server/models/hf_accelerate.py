from argparse import Namespace

import torch

from transformers import AutoModelForCausalLM, AutoTokenizer

from ..utils import print_rank_n
from .model import Model, get_downloaded_model_path


class HFAccelerateModel(Model):
    def __init__(self, args: Namespace) -> None:
        print_rank_n("Loading model...")

        super().__init__(args)

        downloaded_model_path = get_downloaded_model_path(args.model_name)

        self.tokenizer = AutoTokenizer.from_pretrained(downloaded_model_path)
        if self.tokenizer.pad_token_id is None:
            self.tokenizer.add_special_tokens({'pad_token': '[PAD]'})
        self.pad = self.tokenizer.pad_token_id

        kwargs = {
            "pretrained_model_name_or_path": downloaded_model_path,
            "device_map": "auto" if args.num_gpus==1 else "balanced_low_0",
        }
        if args.dtype == torch.int8:
            # using LLM.int8()
            kwargs["load_in_8bit"] = True
        else:
            kwargs["torch_dtype"] = args.dtype

        # this is the CUDA device for the current process. This will be used
        # later to identify the GPU on which to transfer tensors
        self.model = AutoModelForCausalLM.from_pretrained(**kwargs)

        self.model.requires_grad_(False)
        self.model.eval()
        self.input_device = "cuda:0"

        print_rank_n("Model loaded")
