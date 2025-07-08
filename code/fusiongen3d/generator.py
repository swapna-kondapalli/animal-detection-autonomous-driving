def generate_code(modalities, fusion, dataset, model):
    print("\n🚀 Generating FusionGen3D Code...")
    print(f"✔️ Modalities: {modalities}")
    print(f"✔️ Fusion Strategy: {fusion}")
    print(f"✔️ Dataset: {dataset}")
    print(f"✔️ Model: {model}")

    with open("output/model.py", "w") as f:
        f.write("# Auto-generated model file\n")
        f.write(f"# Modalities: {modalities}\n")
        f.write(f"# Fusion: {fusion}\n")
        f.write(f"# Dataset: {dataset}\n")
        f.write(f"# Model: {model}\n\n")
        f.write("class FusionModel:\n")
        f.write("    def __init__(self):\n")
        f.write("        pass  # TODO: Add fusion layers here\n")

    print("\n✅ Code generated at: output/model.py")
