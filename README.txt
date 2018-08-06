**********************************************************************************************************************************************
README
**********************************************************************************************************************************************

To get the token file from original text, run the below command in command prompt:

./runjava novels/BookNLP -doc data/originalTexts/dickens.oliver.pg730.txt -printHTML -p data/output/dickens -tok data/tokens/dickens.oliver.tokens -f

data/originalTexts/dickens.oliver.pg730.txt -> the path to the input book you want to process.
data/tokens/dickens.oliver.tokens -> the path to the file where you want the processed text to be stored.
data/output/dickens -> the path to the output directory you want to write any other diagnostics to.

**********************************************************************************************************************************************

Path to original text and BookNLP pipeline - https://github.com/dbamman/book-nlp

**********************************************************************************************************************************************

To run personality prediction model: Execute PersonalityPrediction.py
Alter filename PATH, extfile PATH and intfile PATH to execute

**********************************************************************************************************************************************
**********************************************************************************************************************************************