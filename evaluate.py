from jiwer import wer

refs = ["हम वहां गए थे"]
preds = ["हम गए थे"]

print("WER:", wer(refs, preds))