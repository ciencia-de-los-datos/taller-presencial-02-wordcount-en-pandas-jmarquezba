"""Taller evaluable"""

import glob

import pandas as pd


def load_input(input_directory):
    filenames = glob.glob(f"{input_directory}/*.txt")

    dataframes = [pd.read_csv(filename, sep = "\t", header = None, names = ["text"]) for filename in filenames]

    concatenated_df = pd.concat(dataframes, ignore_index = True)

    return concatenated_df


def clean_text(dataframe):
    
    dataframe = dataframe.copy()
    dataframe["text"] = dataframe["text"].str.lower()
    dataframe["text"] = dataframe["text"].str.replace(".","")
    dataframe["text"] = dataframe["text"].str.replace(",","")

    return dataframe




def count_words(dataframe):

    dataframe = dataframe.copy()
    dataframe["text"] = dataframe["text"].str.split()
    dataframe = dataframe.explode("text")
    dataframe["count"] = 1

    dataframe = dataframe.groupby("text").agg({"count" : "sum"})
    return dataframe


def save_output(dataframe, output_filename):
    dataframe.to_csv(output_filename, sep = ";", index = True)


#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    save_output((count_words(clean_text(load_input("input")))), "output.txt")


if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
