def convert_dataset_format(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    converted_lines = []
    current_sentence = []
    current_entity = []
    entity_label = None

    for line in lines:
        line = line.strip()
        if line:
            word, label = line.split()
            if label.startswith("B-"):
                if current_entity:
                    current_sentence.append(f"{entity_label} {''.join(current_entity)}")
                entity_label = label[2:]
                current_entity = [word]
            elif label.startswith("I-") and entity_label:
                current_entity.append(word)
            elif label.startswith("E-") and entity_label:
                current_entity.append(word)
                current_sentence.append(f"{entity_label} {''.join(current_entity)}")
                current_entity = []
                entity_label = None
            else:  # handle 'O' or any other tags
                if current_entity:
                    current_sentence.append(f"{entity_label} {''.join(current_entity)}")
                    current_entity = []
                    entity_label = None
                current_sentence.append(word)
        else:
            if current_entity:
                current_sentence.append(f"{entity_label} {''.join(current_entity)}")
                current_entity = []
                entity_label = None
            if current_sentence:
                converted_lines.append(" ".join(current_sentence))
                current_sentence = []

    # Add the last sentence if exists
    if current_sentence:
        if current_entity:
            current_sentence.append(f"{entity_label} {''.join(current_entity)}")
        converted_lines.append(" ".join(current_sentence))

    with open(output_file, "w", encoding="utf-8") as f:
        for line in converted_lines:
            f.write(line + "\n")

# Example usage
convert_dataset_format("train.bioes", "train.lin.txt")
