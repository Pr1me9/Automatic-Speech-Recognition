def build_lattice(outputs):
    lattice = []

    for i in range(len(outputs[0])):
        options = set()
        for out in outputs:
            if i < len(out):
                options.add(out[i])
        lattice.append(list(options))

    return lattice


outputs = [
    ["उसने", "चौदह", "किताबें"],
    ["उसने", "14", "पुस्तकें"]
]

print(build_lattice(outputs))