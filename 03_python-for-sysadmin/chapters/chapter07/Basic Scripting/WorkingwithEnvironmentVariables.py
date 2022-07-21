
import os

stage = os.environ['STAGE'].upper()

output = f"Running in {stage}"

if stage.startswith("PROD"):
    output = "DANGER!!! - " + output
print(output)