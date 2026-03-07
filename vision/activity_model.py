import torch

class ActivityModel:

    def __init__(self):
        self.model = torch.hub.load('facebookresearch/pytorchvideo', 'slowfast_r50', pretrained=True)
        self.model.eval()

    def predict(self, frames):

        # simplified example
        prediction = torch.randint(0,10,(1,)).item()

        return prediction