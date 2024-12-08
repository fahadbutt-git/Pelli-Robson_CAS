import random

# Define contrast levels
optotypes = list("ᐱᑎᑭᒧᒋᒥᑯᒧᔨ")
contrast_levels = [0.05, 0.2, 0.35, 0.5, 0.65, 0.8, 0.95, 1.1, 1.25, 1.4, 1.55, 1.7, 1.85, 2.0, 2.15, 2.3]
log_contrast_levels = ["0.05", "0.20", "0.35", "0.50", "0.65", "0.80", "0.95", "1.10", "1.25", "1.40", "1.55", "1.70", "1.85", "2.00", "2.15", "2.30"]
grayscale_levels = [0.0, 0.24, 0.42, 0.56, 0.67, 0.75, 0.81, 0.86, 0.89, 0.92, 0.94, 0.95, 0.96, 0.97, 0.98, 0.98]

# Generate LaTeX rows for 8 rows (2 triplets per row)
rows = []
for row_index in range(8):  # Loop to create 8 rows
    # Maintain a set of used letters for this row
    used_letters = set()

    # First triplet
    triplet1 = "".join(random.sample([l for l in optotypes if l not in used_letters], 3))
    used_letters.update(triplet1)  # Add used letters to the set
    group1_index = row_index * 2
    group1_contrast = contrast_levels[group1_index]
    group1_log = log_contrast_levels[group1_index]
    group1_gray = grayscale_levels[group1_index]

    # Second triplet
    triplet2 = "".join(random.sample([l for l in optotypes if l not in used_letters], 3))
    used_letters.update(triplet2)  # Add used letters to the set
    group2_index = group1_index + 1
    group2_contrast = contrast_levels[group2_index]
    group2_log = log_contrast_levels[group2_index]
    group2_gray = grayscale_levels[group2_index]

    # Append row content with log contrast values on both sides and vertical spacing
    rows.append(
        rf"""
        \noalign{{\vskip 50pt}} % Add vertical spacing
        \textbf{{\LARGE {group1_log}}} &
        \contrast{{{group1_gray}}}{{\optotype{{\optotypesize}}{{{triplet1}}}}} &
        \hspace{{3cm}} &
        \contrast{{{group2_gray}}}{{\optotype{{\optotypesize}}{{{triplet2}}}}} &
        \textbf{{\LARGE {group2_log}}} \\
        """
    )

# Combine rows into the TeX table
tex_content = "\n".join(rows)
print(tex_content)
