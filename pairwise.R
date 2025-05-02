# 1) Read in your data
data <- read.csv("/Users/hanneswesterberg/Desktop/Stuff/Skola/24:25/DM128X Kexet/Kex/friedmanTests/reshaped_file.csv")

# 2) Make sure your grouping variables are factors
data$audio          <- factor(data$audio)
data$playback_speed <- factor(data$playback_speed)
data$algorithm      <- factor(data$algorithm)

# 3) Pairwise t‑tests with Bonferroni adjustment
#    Replace 'audio' with whichever factor you want to explore

# Example: pairwise comparisons of 'audio' levels on the 'rank' scores
pairwise.t.test(data$rank,
                data$audio,
                p.adjust.method = "bonferroni")

# Example: for playback_speed
pairwise.t.test(data$rank,
                data$playback_speed,
                p.adjust.method = "bonferroni")

# Example: for algorithm
pairwise.t.test(data$rank,
                data$algorithm,
                p.adjust.method = "bonferroni")
