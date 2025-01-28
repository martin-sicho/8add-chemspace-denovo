class SequenceRNN(SequenceRNN):
    """Just the original model, but with bugs corrected"""

    def attachToGPUs(self, gpus):
        """Needed to fix a bug with loading on a CPU"""
        if self.device == torch.device('cpu'):
            self.device = self.device
            self.to(self.device)
            self.gpus = (-1,)
            return self.gpus
        else:
            return super().attachToGPUs(gpus)