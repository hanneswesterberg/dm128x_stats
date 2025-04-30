library(ARTool)

# 1) Read and factor everything that should be categorical
df = read.csv("file.csv")

# Convert the three within-subject variables to factors
df$ID             <- factor(df$ID)
df$audio          <- factor(df$audio)
df$playback_speed <- factor(df$playback_speed)
df$algorithm      <- factor(df$algorithm)

str(df)

m <- art(rank ~ algorithm * audio * playback_speed + (1|ID), data=df)

summary(m)

anova(m)


